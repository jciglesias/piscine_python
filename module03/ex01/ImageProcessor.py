"""
Process images
"""
# %matplotlib inline
import matplotlib.image as img
import matplotlib.pyplot as plt

class ImageProcessor:
    """
    open image
    """
    def __init__(self) -> None:
        pass
    def load(self, path):
        """
        opens the PNG file specified by the path
        argument and returns an array with the RGB values
        of the pixels image. It must display a message
        specifying the dimensions of the image (e.g. 340 x 500).
        """
        try:
            lst = img.imread(path)
            print(f"Loading image of dimensions {lst.shape[0]} x {lst.shape[1]}")
            return lst
        except FileNotFoundError:
            print("Exception: FileNotFoundError -- strerror: No such file or directory")
            return None
    def display(self, array):
        """
        takes a numpy array as an argument and displays the
        corresponding RGB image.
        """
        try:
            plt.imshow(array)
            plt.show()
        except TypeError:
            print("Exception: OSError -- strerror: None")
