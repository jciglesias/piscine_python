"""Class to create NumPy arrays"""
import random
import numpy

def validate(obj, dtype):
    """
    validate list and tuple input
    """
    if isinstance(obj, dtype):
        for i in range(len(obj) - 1):
            if not isinstance(obj[i], type(obj[i + 1])):
                return False
            if isinstance(obj[i], (list, tuple)) and len(obj[i]) != len(obj[i + 1]):
                return False
    else:
        return False
    return True

class NumPyCreator:
    """
    Creates a NumPy array
    """
    def from_list(self, lst, dtype = None):
        """
        takes a list or nested lists and returns its corresponding
        Numpy array.
        """
        return numpy.array(lst, dtype=dtype) if validate(lst, list) else None
    def from_tuple(self, tpl, dtype = None):
        """
        takes a tuple or nested tuples and returns its corresponding
        Numpy array.
        """
        return numpy.array(tpl, dtype=dtype) if validate(tpl, tuple) else None
    def from_iterable(self, itr, dtype = None):
        """
        takes an iterable and returns an array which contains all
        its elements.
        """
        try:
            tmp = [i for i in itr]
            return numpy.array(tmp, dtype=dtype) if validate(tmp, list) else None
        except TypeError:
            return None
    def from_shape(self, shape, value = 0, dtype = None):
        """
        returns an array filled with the same value. The first
        argument is a tuple which specifies the shape of the array,
        and the second argument specifies the value of the elements.
        This value must be 0 by default.
        """
        if len(shape) == 2 and shape[0] >= 0 and shape[1] >= 0:
            return numpy.full(shape=shape, fill_value=value, dtype=dtype)
        return None
    def random(self, shape, dtype = None):
        """
        returns an array filled with random values. It takes as an
        argument a tuple which specifies the shape of the array.
        """
        try:
            if len(shape) == 2 and shape[0] >= 0 and shape[1] >= 0:
                return numpy.array([[random.random() for _ in range(shape[1])] for _ in range(shape[0])], dtype = dtype)
            return None
        except TypeError:
            return None
    def identity(self, _n, dtype = None):
        """
        returns an array representing the identity matrix of size n.
        """
        try:
            if _n >= 0:
                return numpy.array([[1 if _y == _x else 0 for _x in range(_n)] for _y in range(_n)], dtype = dtype)
            return None
        except TypeError:
            return None
