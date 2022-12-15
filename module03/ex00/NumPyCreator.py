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
        if validate(lst, list):
            return numpy.array(lst, dtype=dtype)
        return None
    def from_tuple(self, tpl, dtype = None):
        """
        takes a tuple or nested tuples and returns its corresponding
        Numpy array.
        """
        if validate(tpl, tuple):
            return numpy.array(tpl, dtype=dtype)
        return None
    def from_iterable(self, itr, dtype = None):
        """
        takes an iterable and returns an array which contains all
        its elements.
        """
        try:
            tmp = []
            for i in itr:
                tmp.append(i)
            if validate(tmp, list):
                return numpy.array(tmp, dtype=dtype)
            return None
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
            _y, _x, tmp = 0, 0, []
            while _y < shape[0]:
                tmp.append([])
                while _x < shape[1]:
                    tmp[_y].append(random.random())
                    _x += 1
                _x = 0
                _y += 1
            if len(shape) == 2 and shape[0] >= 0 and shape[1] >= 0:
                return numpy.array(tmp, dtype = dtype)
            return None
        except TypeError:
            return None
    def identity(self, _n, dtype = None):
        """
        returns an array representing the identity matrix of size n.
        """
        try:
            _y, _x, tmp = 0, 0, []
            while _y < _n:
                tmp.append([])
                while _x < _n:
                    if _y == _x:
                        tmp[_y].append(1)
                    else:
                        tmp[_y].append(0)
                    _x += 1
                _x = 0
                _y += 1
            if _n >= 0:
                return numpy.array(tmp, dtype = dtype)
            return None
        except TypeError:
            return None
