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
            return 1 - array 
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
                    column[0] *= 0.5
                    column[1] *= 0.5
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
                    column[0] *= 0.5
                    # column[1]
                    column[2] *= 0.5
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
                    column[1] *= 0.5
                    column[2] *= 0.5
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
                    if np.sum(column) < 1.0:
                        column *= 0.5
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
                        tmp = np.sum(column)
                        column[0] = tmp / 3
                        column[1] = tmp / 3
                        column[2] = tmp / 3
                    else:
                        column[0] *= kwargs[filter][0]
                        column[1] *= kwargs[filter][1]
                        column[2] *= kwargs[filter][2]
            return arr
        return None
