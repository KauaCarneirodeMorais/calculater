from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import DriveHandleInterface
from src.errors.http_unprocessable_entity import HttpUnprocesableEntityError

class Calculate4():
    def __init__(self, drive_handle: DriveHandleInterface) -> None:
        self._drive_handle = drive_handle

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body =  request.json
        input_data = self.__validate_body(body)
    
        average = self._calculate_average(input_data)
        formated_responseve = self.__format_response(average)
        return formated_responseve
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocesableEntityError("Body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def _calculate_average(self, numbers: List[float]) -> float:
        average = self._drive_handle.average(numbers)
        return float(average)
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": average,
                "Sucess": True
            }
        }