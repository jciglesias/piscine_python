import numpy, random

class NumPyCreator:
    def from_list(self, lst, dtype = None):
        """
        takes a list or nested lists and returns its corresponding
        Numpy array.
        """
        return numpy.array(lst, dtype=dtype)
    def from_tuple(self, tpl, dtype = None):
        """
        takes a tuple or nested tuples and returns its corresponding
        Numpy array.
        """
        return numpy.array(tpl, dtype=dtype)
    def from_iterable(self, itr, dtype = None):
        """
        takes an iterable and returns an array which contains all
        its elements.
        """
        try:
            tmp = []
            for i in itr:
                tmp.append(i)
            return numpy.array(tmp, dtype=dtype)
        except Exception:
            return None
    def from_shape(self, shape, value = 0, dtype = None):
        """
        returns an array filled with the same value. The first
        argument is a tuple which specifies the shape of the array,
        and the second argument specifies the value of the elements.
        This value must be 0 by default.
        """
        return numpy.full(shape=shape, fill_value=value, dtype=dtype)
    def random(self, shape, dtype = None):
        """
        returns an array filled with random values. It takes as an
        argument a tuple which specifies the shape of the array.
        """
        try:
            y, x, tmp = 0, 0, []
            while y < shape[0]:
                tmp.append([])
                while x < shape[1]:
                    tmp[y].append(random.random())
                    x += 1
                x = 0
                y += 1
            return numpy.array(tmp, dtype = dtype)
        except Exception:
            return None
    def identity(self, n, dtype = None):
        """
        returns an array representing the identity matrix of size n.
        """
        try:
            y, x, tmp = 0, 0, []
            while y < n:
                tmp.append([])
                while x < n:
                    if y == x:
                        tmp[y].append(1)
                    else:
                        tmp[y].append(0)
                    x += 1
                x = 0
                y += 1
            return numpy.array(tmp, dtype = dtype)
        except Exception:
            return None
