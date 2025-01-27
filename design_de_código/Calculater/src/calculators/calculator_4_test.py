from src.drivers.numpy_handler import NumpyHandler
from .calculator_4 import Calculate4
from typing import Dict
# pytest -s -v Calculater/src/calculators/calculator_4_test.py

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({ "numbers": [1,2,3,4,5,6,7,8,9] })
    calculate_4 = Calculate4(NumpyHandler())

    response = calculate_4.calculate(mock_request)
    print()
    print(response)


