import numpy as np
from matplotlib import pyplot as plt

from ColorFilter import ColorFilter
cf = ColorFilter()

arr = plt.imread("assets/elon_canaGAN.png")
plt.title("Original")
plt.imshow(arr)
plt.show()
for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert, cf.to_celluloid]:
	plt.title(f.__name__)
	plt.imshow(f(arr))
	plt.show()
# Output :
# Loading image of dimensions 200 x 200

plt.title("Grayscale")
plt.imshow(cf.to_grayscale(arr, 'm'), cmap="gray")
plt.show()
plt.title("Grayscale weight")
plt.imshow(cf.to_grayscale(arr, 'weight', weight = [0.2, 0.3, 0.5]), cmap="gray")
plt.show()