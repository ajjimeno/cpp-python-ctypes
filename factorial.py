import ctypes
lib = ctypes.cdll.LoadLibrary('./libfactorial.so')
class Factorial(object):
    def __init__(self):
        lib.Factorial_new.argtypes = []
        lib.Factorial_factorial.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.Factorial_factorial.restype = ctypes.c_long
        self.obj = lib.Factorial_new()

    def factorial(self, val):
        return lib.Factorial_factorial(self.obj, val)