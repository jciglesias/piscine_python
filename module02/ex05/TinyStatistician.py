import math, numpy

class TinyStatistician:
    def mean(self, x):
        """
        computes the mean of a given non-empty list or array x, using a
        for-loop. The method returns the mean as a float, otherwise
        None if x is an empty list or array.
        """
        size = 0
        if type(x) is list:
            size = len(x)
        elif type(x) is numpy.ndarray:
            size = x.size
        if size == 0:
            return None
        sum = 0
        for i in x:
            sum += i    
        return sum / size
    def median(self, x: list):
        """
        computes the median of a given non-empty list or array x.
        The method returns the median as a float, otherwise None
        if x is an empty list or array.
        """
        size = 0
        if type(x) is list:
            size = len(x)
        elif type(x) is numpy.ndarray:
            size = x.size
        if size == 0:
            return None
        x.sort()
        return float(x[int(size / 2)])
    def quartiles(self, x):
        """
        computes the 1st and 3rd quartiles of a given non-empty array x.
        The method returns the quartile as a float, otherwise None if x
        is an empty list or array.
        """
        size = 0
        if type(x) is list:
            size = len(x)
        elif type(x) is numpy.ndarray:
            size = x.size
        if size == 0:
            return None
        x.sort()
        quarter = size / 4
        return [float(x[int(quarter)]), float(x[int(quarter * 3)])]
    def var(self, x):
        """computes the variance of a given non-empty list or array x,
        using a for-loop. The method returns the variance as a float,
        otherwise None if x is an empty list or array.
        """
        size = 0
        if type(x) is list:
            size = len(x)
        elif type(x) is numpy.ndarray:
            size = x.size
        if size == 0:
            return None
        sum = 0
        mean = self.mean(x)
        for i in x:
            sum += (i - mean) * (i - mean)
        return float(sum / size)
    def std(self, x) :
        """
        computes the standard deviation of a given non-empty list or array
        x, using a for-loop. The method returns the standard deviation as
        a float, otherwise None if x is an empty list or array.
        """
        size = 0
        if type(x) is list:
            size = len(x)
        elif type(x) is numpy.ndarray:
            size = x.size
        if size == 0:
            return None
        return math.sqrt(self.var(x))