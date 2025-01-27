from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculate4

def calculate4_factory():
    numpy_handle = NumpyHandler()
    calc = Calculate4(numpy_handle)
    return calc