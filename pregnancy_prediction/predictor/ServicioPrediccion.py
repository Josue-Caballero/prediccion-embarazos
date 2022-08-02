
from predictor.ModeloPrediccion import ModeloPrediccion
from predictor.PreprocesadorDatos import PreprocesadorDatos

from predictor.exceptions.BadFile import BadFile

class ServicioPrediccion:

    def __init__(self):

        self.modeloPrediccion = ModeloPrediccion()
        self.preprocesador = PreprocesadorDatos()

    def predecirRegistros(self, registros):
        
        regValidos = self.preprocesador.validarRegistros(registros)

        return self.modeloPrediccion.predecirRegistros(regValidos)
    
    
    def prediccionArchivo(self, archivo):

        if(not archivo):
            raise BadFile("No se brindo archivo alguno")

        dataFrame = self.preprocesador.serializarArchivo(archivo)

        return self.modeloPrediccion.predecirRegistros(dataFrame)

