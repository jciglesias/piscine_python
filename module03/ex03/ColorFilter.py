import numpy as np

class ColorFilter:
    """
    A tool that can apply a variety of color filters on images.
    methods:
        invert
        to_blue
        to_green
        to_red
        to_celluloid
        to_grayscale
    """

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr = array.copy()
            for row in arr:
                for column in row:
                    column[0] = 1 - column[0]
                    column[1] = 1 - column[1]
                    column[2] = 1 - column[2]
            return arr
        return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr = array.copy()
            for row in arr:
                for column in row:
                    column[0] = 0
                    column[1] = 0
                    # column[2]
            return arr
        return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr = array.copy()
            for row in arr:
                for column in row:
                    column[0] *= 0.1
                    # column[1]
                    column[2] *= 0.1
            return arr
        return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr = array.copy()
            for row in arr:
                for column in row:
                    # column[0]
                    column[1] = 0
                    column[2] = 0
            return arr
        return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr = array.copy()
            for row in arr:
                for column in row:
                    tmp = np.linspace(column.min(), column.max(), 3)
                    for i in range(3):
                        arr[i] = tmp[i]
            return arr
        return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
            For filter = 'mean'/'m': performs the mean of RBG channels.
            For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) and filter in ['m','mean','w','weight']:
            arr = array.copy()
            for row in arr:
                for column in row:
                    if filter in ['m', 'mean']:
                        tmp = np.sum(column) / 3
                        column[0] = tmp
                        column[1] = tmp
                        column[2] = tmp
                    else:
                        column[0] *= kwargs[filter][0]
                        column[1] *= kwargs[filter][1]
                        column[2] *= kwargs[filter][2]
            return arr
        return None
