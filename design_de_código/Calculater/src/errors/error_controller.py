from typing import Dict
from .http_unprocessable_entity import HttpUnprocesableEntityError
from .http_bad_request import HttpBadRequestError

def handle_error(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocesableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "Erros": [{
                    "title": error.name,
                    "detail": error.message
            }]}
        }
    return {
        "status_code": 500,
        "body": {
            "Erros" :[{
                "title": "Server error",
                "detail": str(error)
        }]}
    }
