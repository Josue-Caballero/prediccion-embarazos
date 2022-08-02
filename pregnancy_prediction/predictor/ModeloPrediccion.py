
import pickle


class ModeloPrediccion:

    def __init__(self):
        self.modelo = pickle.load(open('model_assets/classifier.pkl', 'rb'))

    def predecirRegistro(self, registro):
        
        return self.modelo.predict(registro)

    def predecirRegistros(self, registros):
        
        return self.predecirRegistro(registros)
