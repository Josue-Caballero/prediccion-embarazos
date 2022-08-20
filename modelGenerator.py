import pickle
import numpy as np
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder

# Load data
##############################################################################
data = pd.read_csv('data.csv', encoding='utf-8')

subsetYes = data[data['f2_s2_200'] == 'si'].sample(frac=1) # Yes registries
subsetYes.reset_index(inplace=True, drop=True)

subsetTestYes = subsetYes[1364:] # Registries to test the system
subsetYes = subsetYes[:1364]

subsetNo = data[data['f2_s2_200'] == 'no'].sample(frac=1) # No registries
subsetNo.reset_index(inplace=True, drop=True)

subsetTestNo = subsetNo[1364:1464] # Registries to test the system
subsetNo = subsetNo[:1364]

data = pd.concat([subsetYes, subsetNo], axis=0).sample(frac=1)
data.reset_index(inplace=True, drop=True)

dataTest = pd.concat([subsetTestYes, subsetTestNo], axis=0)
dataTest.reset_index(inplace=True, drop=True)
dataTest.to_csv('registriesToTest.csv', index=None)

# Preprocesing
##############################################################################
Xenc = OneHotEncoder()
scaler = StandardScaler()
lencoder = LabelEncoder()
omisiones = [
    'prov', 'f2_s1_101', 'f2_s6_601_1', 'f2_s6_603_12',
    'f2_s8_804', 'f2_s8_806', 'f2_s8_807', 'f2_s8_808', 
    'f2_s8_809','f2_s8_814', 'f2_s8_821', 'gedad_anios', 
    'estrato', 'f2_s2_200', 'f2_s2_207'
]

for x in data.columns:
    data[x] = data[x].fillna('no sabe / no responde')
    
X = data.drop(omisiones, axis=1)

y = lencoder.fit_transform(data['f2_s2_200'])

Xenc = Xenc.fit(X)

XE = Xenc.transform(X).toarray()
XE = np.concatenate(
    (XE, scaler.fit_transform(pd.DataFrame(data['f2_s1_101']))), 
    axis=1
)

xTrain, xTest, yTrain, yTest = train_test_split(
    XE, y, test_size=0.30, random_state= 0
)

# Training
#############################################################################
classifier = LogisticRegression(solver='liblinear')
classifier.fit(xTrain, yTrain)

# Predictions
##############################################################################
predictions = classifier.predict(xTest)
print(classifier.score(xTest, yTest))

# Saving model and encoders
##############################################################################
pickle.dump(scaler, open('scaler.sav', 'wb'))
pickle.dump(Xenc, open('featuresEncoder.sav', 'wb'))
pickle.dump(classifier, open('classifier.pkl', 'wb'))
