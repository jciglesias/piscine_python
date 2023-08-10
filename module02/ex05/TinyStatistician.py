import math, numpy

class TinyStatistician:
    def mean(self, x):
        """
        computes the mean of a given non-empty list or array x, using a
        for-loop. The method returns the mean as a float, otherwise
        None if x is an empty list or array.
        """
        if isinstance(x, (numpy.ndarray, list)) and len(x):
            total = 0
            for n in x:
                total += n
            return float(total / len(x))
        return None
    def median(self, x: list):
        """
        computes the median of a given non-empty list or array x.
        The method returns the median as a float, otherwise None
        if x is an empty list or array.
        """
        if isinstance(x, (numpy.ndarray, list)) and len(x):
            tmp = x.copy()
            tmp.sort()
            return float(tmp[int(len(tmp) / 2)])
        return None
    def quartiles(self, x):
        """
        computes the 1st and 3rd quartiles of a given non-empty array x.
        The method returns the quartile as a float, otherwise None if x
        is an empty list or array.
        """
        if isinstance(x, (numpy.ndarray, list)) and len(x):
            tmp = x.copy()
            tmp.sort()
            quarter = len(tmp) / 4
            return [float(tmp[int(quarter)]), float(tmp[int(quarter * 3)])]
        return None
    def var(self, x):
        """computes the variance of a given non-empty list or array x,
        using a for-loop. The method returns the variance as a float,
        otherwise None if x is an empty list or array.
        """
        if isinstance(x, (numpy.ndarray, list)) and len(x):
            v = 0
            m = self.mean(x)
            for i in x:
                v += (i - m) * (i - m)
            return v / len(x)
        return None
    def std(self, x) :
        """
        computes the standard deviation of a given non-empty list or array
        x, using a for-loop. The method returns the standard deviation as
        a float, otherwise None if x is an empty list or array.
        """
        if isinstance(x, (numpy.ndarray, list)) and len(x):
            return math.sqrt(self.var(x))
        return None