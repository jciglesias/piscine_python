"""Test for NumPyCreator"""
from NumPyCreator import NumPyCreator
import numpy as np

if __name__ == "__main__":
    nc = NumPyCreator()
    tmp = [4, 3, 2, 1]
    tp = (4, 3, 2, 1)
    it = iter(tmp)
    print(f"numpy: {np.array(tmp, dtype=float)}\nclass: {nc.from_list(tmp, dtype=float)}")
    print(f"numpy: {np.array(tp)}\nclass: {nc.from_tuple(tp)}")
    print(f"numpy: {np.array(tmp, dtype=float)}\nclass: {nc.from_iterable(it, dtype=float)}")
    print(nc.from_shape((3,4), 42))
    print(nc.random((3,4)))
    print(nc.identity(4, dtype=float))
    print("\nerror management:")
    print(nc.from_list("toto"))
    print(nc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
    print(nc.from_tuple(3.2))
    print(nc.from_tuple(((1,5,8),(7,5))))
    print(nc.from_shape((-1, -1)))
    print(nc.from_iterable(1))
    print(nc.identity(-1))
