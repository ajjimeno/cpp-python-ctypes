import ctypes
import numpy as np
from numpy.ctypeslib import load_library

from numpyctypes import c_ndarray

lib = ctypes.cdll.LoadLibrary('./libtest.so')

class Runner(object):
    def __init__(self):
        lib.Runner_new.argtypes = []
        lib.Runner_new.restype = ctypes.c_void_p
        lib.Runner_print.argtypes = [ctypes.c_void_p]
        lib.Runner_print.restype = ctypes.c_void_p
        lib.Runner_setOutput.argtypes = [ctypes.c_void_p, ctypes.Structure]
        lib.Runner_setOutput.restype = ctypes.c_void_p

        self.obj = lib.Runner_new()

    def getPrint(self):
        lib.Runner_print(self.obj)

    def setOutput(self, array):
        lib.Runner_setOutput(self.obj, array)