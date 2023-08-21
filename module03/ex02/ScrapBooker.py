"""Manipulation and initiation to slicing method on numpy arrays."""
import numpy as np

class ScrapBooker:
    """
    The first coordinate is counted along the vertical axis starting
    from the top, and that the second coordinate is counted along
    the horizontal axis starting from the left. Indexing starts from 0.
    """
    def __init__(self) -> None:
        pass
    def crop(self, array: np.ndarray, dim: tuple, position:tuple=(0,0)):
        """
        Crops the image as a rectangle via dim arguments
        (being the new height and width of the image)
        from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) and type(dim) == tuple == type(position) and len(dim) == 2 == len(position):
            newarray = []
            count_rows = 0
            count_colums = 0
            for i in range(array.shape[0]):
                if i >= position[0] and count_rows < dim[0]:
                    count_rows += 1
                    newarray.append([])
                for j in range(array.shape[1]):
                    if i >= position[0] and j >= position[1] and count_rows <= dim[0] and count_colums < dim[1]:
                        newarray[count_rows - 1].append(array[i][j])
                        count_colums += 1
                count_colums = 0
                if count_rows == dim[0]:
                    break
            return(np.array(newarray))
        return None
    def thin(self, array, _n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: Horizontal, 1: Vertical)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number
               of row/column of the array (depending of axis value).
            axis: positive non null integer.
        Return:
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) and isinstance(_n, int) and isinstance(axis, int) :
            if _n < 0 or axis < 0 or axis > 1 or _n > array.shape[~axis]:
                print(array.shape)
                return None
            newarray = []
            for i in range(array.shape[0]):
                if not axis or (axis and (i + 1) % _n):
                    newarray.append([])
                    [newarray[newarray.__len__() - 1].append(array[i][j]) for j in range(array.shape[1]) if axis or (not axis and (j + 1) % _n)]
            return(np.array(newarray))
    def juxtapose(self, array: np.ndarray, _n: int, axis: int):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
            This function should not raise any Exception.
        """
        if not axis :
            return np.array([y for _ in range(_n) for y in array])
        return np.array([[i for _ in range(_n) for i in array[x]] for x in range(array.shape[0])])
    def mosaic(self, array: np.ndarray, dim: tuple):
        """
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Return:
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) and isinstance(dim, tuple) and len(dim) == 2:
            return np.array([[j for _ in range(dim[1]) for j in array[i]] for _ in range(dim[0]) for i in range(array.shape[0])])
        return None
