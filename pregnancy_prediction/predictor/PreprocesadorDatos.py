
import pickle
import numpy as np
import pandas as pd

class PreprocesadorDatos:
    
    scaler = pickle.load(open('model_assets/scaler.sav', 'rb'))
    featuresEncoder = pickle.load(open('model_assets/featuresEncoder.sav', 'rb'))
    columnas = ['prov','f2_s1_101','f2_s6_601_1','f2_s6_601_2','f2_s6_601_3','f2_s6_602_3','f2_s6_601_4','f2_s6_602_4','f2_s6_601_5','f2_s6_602_5','f2_s6_601_6','f2_s6_602_6','f2_s6_601_7','f2_s6_602_7','f2_s6_601_8','f2_s6_602_8','f2_s6_601_9','f2_s6_602_9','f2_s6_601_10','f2_s6_602_10','f2_s6_603_9','f2_s6_603_10','f2_s6_603_11','f2_s6_603_12','f2_s6_611','f2_s6_614','f2_s6_618','f2_s6_627','f2_s8_800a','f2_s8_800b','f2_s8_800c','f2_s8_800d','f2_s8_800e','f2_s8_800f','f2_s8_801f','f2_s8_800g','f2_s8_800h','f2_s8_804','f2_s8_806','f2_s8_807','f2_s8_808','f2_s8_809','f2_s8_814','f2_s8_821','f2_s8_844','f2_s8_845','gedad_anios','nivins','estrato','f2_s2_207','f2_s2_200']
    omisiones = [
        'prov', 'f2_s6_601_1', 'f2_s6_603_12', 'f2_s8_804', 
        'f2_s8_806', 'f2_s8_807', 'f2_s8_808', 'f2_s8_809',
        'f2_s8_814', 'f2_s8_821', 'gedad_anios', 'estrato',
        'f2_s2_200', 'f2_s2_207'
    ]

    def validarRegistros(self, registros):

        tmpRegisters = []
        registros = registros.split('\n')
        
        for register in registros:
            tmpRegisters.append(register.split(','))
        
        registros = np.array(tmpRegisters)
        registros = np.where(registros == '', None, registros)

        dataFrame = pd.DataFrame(registros, columns=list(self.columnas)).drop(self.omisiones, axis=1)
        
        return self.__codificarRegistros(dataFrame)
    

    def serializarArchivo(self, file):
        
        tmpFile = open('tmpData.csv', 'wb')
        tmpFile.write(file.read())
        tmpFile.close()
        
        data = pd.read_csv('tmpData.csv', encoding='utf8').drop(self.omisiones, axis=1)

        return self.__codificarRegistros(data)


    def __codificarRegistros(self, data):

        for x in data.columns:
            data[x] = data[x].fillna('no sabe / no responde')
        
        xData = np.concatenate(
            ( 
            self.featuresEncoder.transform(data[data.columns[1:]]).toarray(), 
            self.scaler.transform( pd.DataFrame(data['f2_s1_101']) )
            ),
            axis=1
        )

        return xData

