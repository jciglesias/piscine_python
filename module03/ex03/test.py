import numpy as np
from matplotlib import pyplot as plt

from ColorFilter import ColorFilter
cf = ColorFilter()

# for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
arr = plt.imread("assets/42AI.png")
plt.title("Original")
plt.imshow(arr)
plt.show()
	# plt.imshow(f(arr))
	# plt.show()
# Output :
# Loading image of dimensions 200 x 200

# print(arr.shape)
plt.title("Invert")
plt.imshow(cf.invert(arr))
plt.show()
plt.title("Green")
plt.imshow(cf.to_green(arr))
plt.show()
plt.title("Red")
plt.imshow(cf.to_red(arr))
plt.show()
plt.title("Blue")
plt.imshow(cf.to_blue(arr))
plt.show()
plt.title("Celluloid")
plt.imshow(cf.to_celluloid(arr))
plt.show()
plt.title("Grayscale")
plt.imshow(cf.to_grayscale(arr, 'm'), cmap="gray")
plt.show()
plt.title("Grayscale weight")
plt.imshow(cf.to_grayscale(arr, 'weight', weight = [0.2, 0.3, 0.5]), cmap="gray")
plt.show()