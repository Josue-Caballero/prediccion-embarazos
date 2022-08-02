
from rest_framework.exceptions import APIException

class BadFile(APIException):

    status_code = 404
    default_code = 'Archivo corrupto'
    
    def __init__(self, message = 'El archivo suministrado contenia errores'):
        
        self.default_detail = message

