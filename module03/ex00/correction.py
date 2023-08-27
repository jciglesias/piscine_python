from NumPyCreator import NumPyCreator
npc = NumPyCreator()

print(npc.from_list([[],[]]))
# array([], shape=(2, 0), dtype=float64)
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
# array([[1, 2, 3],
    #   [6, 3, 4],
    #   [8, 5, 6]])
print(npc.from_tuple(("a","b","c")))
# array(['a', 'b', 'c'], dtype='<U1')
print(npc.from_iterable(range(5)))
# array([0, 1, 2, 3, 4])
print(npc.from_shape((0, 0)))
# array([], shape=(0, 0), dtype=float64)
print(npc.from_shape((3, 5)))
# array([[0., 0., 0., 0., 0.],
    #   [0., 0., 0., 0., 0.],
    #   [0., 0., 0., 0., 0.]])
print(npc.random((3, 5)))
# array([[0.74819604, 0.32295616, 0.27371925, 0.57171326, 0.92582071],
    #   [0.70307642, 0.94846695, 0.12465384, 0.25146454, 0.11179953],
    #   [0.38326719, 0.26179493, 0.88157011, 0.29978869, 0.72677049]])`
print(npc.identity(4))
# array([[1., 0., 0., 0.],
    #   [0., 1., 0., 0.],
    #   [0., 0., 1., 0.],
    #   [0., 0., 0., 1.]])
print("Error management:")
print(npc.from_list("toto"))
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1,5,8),(7,5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))