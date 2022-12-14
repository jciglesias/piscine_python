from NumPyCreator import NumPyCreator
import numpy

if __name__ == "__main__":
    nc = NumPyCreator()
    tmp = [4, 3, 2, 1]
    tp = (4, 3, 2, 1)
    it = iter(tmp)
    print(nc.from_list(tmp, dtype=float))
    print(nc.from_tuple(tp))
    print(nc.from_iterable(it, dtype=float))
    print(nc.from_shape((3,4), 42))
    print(nc.random((3,4)))
    print(nc.identity(4, dtype=float))