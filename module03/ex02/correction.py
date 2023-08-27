import numpy as np
from ScrapBooker import ScrapBooker
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
# array([[ 5],
    #   [10],
    #   [15]])
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,0))
# array([['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H'],
#       ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')
arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
print(spb.thin(arr3,3,1))
# array([['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
#       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
#       ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
#       ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
#       ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']], dtype='<U1')
arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(spb.juxtapose(arr4, 2, 0))
# array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print("Errors:\n", spb.crop(not_numpy_arr, (1,2)), spb.juxtapose(arr4, -2, 0), spb.mosaic(arr4, (1, 2, 3)))