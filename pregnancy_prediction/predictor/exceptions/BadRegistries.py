
from rest_framework.exceptions import APIException

class BadRegistries(APIException):

    status_code = 404
    default_code = 'Registros incorrectos'
    
    def __init__(self, message = 'Los registros suministrados contenian errores'):
        
        self.default_detail = message

