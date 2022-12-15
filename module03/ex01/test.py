"""Test ImageProcessor"""
from ImageProcessor import ImageProcessor as IP

if __name__=="__main__":
    processor = IP()
    lst = processor.load("no_image.png")
    print(lst)
    processor.display([])
    lst = processor.load("squirtle.png")
    print(lst)
    processor.display(lst)
