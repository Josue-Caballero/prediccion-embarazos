
from rest_framework.response import Response
from rest_framework.decorators import api_view

from predictor.ServicioPrediccion import ServicioPrediccion

# Create your views here.

servicioPrediccion = ServicioPrediccion()

@api_view(['POST'])
def predictFromRegistersView(req):
    
    predicciones = servicioPrediccion.predecirRegistros(req.POST['registros'])

    return Response({"prediccion": predicciones})


@api_view(['POST'])
def predictFromFileView(req):
    
    predicciones = servicioPrediccion.prediccionArchivo(req.FILES['file'])

    return Response({"prediccion": predicciones})
