from vector import Vector

if __name__=="__main__":
    try:
        print("Example 0:")
        print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
        # Expected output
        # (4,1)
        print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
        # Expected output
        # [[0.0], [1.0], [2.0], [3.0]]
        print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
        # Expected output
        # (1,4)
        print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
        # Expected output
        # [[0.0, 1.0, 2.0, 3.0]]
        print("Example 1:")
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        print(v1.shape)
        # Expected output:
        # (4,1)
        print(v1.T())
        # Expected output:
        # [[0.0, 1.0, 2.0, 3.0]]
        print(v1.shape)
        # Expected output:
        # (1,4)
        print("Example 2:")
        print(v1.shape)
        # Expected output:
        # (1,4)
        print(v1.T())
        # Expected output:
        # Vector([[0.0], [1.0], [2.0], [3.0]])
        print(v1.shape)
        # Expected output:
        # (4,1)
        print("Example 3:")
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        print(v1.dot(v2))
        # Expected output:
        # 18.0
        v3 = Vector([[1.0, 3.0]])
        v4 = Vector([[2.0, 4.0]])
        print(v3.dot(v4))
        # Expected output:
        # 14.0
        print(v1)
        # Expected output: to see what __repr__() should do
        # [[0.0, 1.0, 2.0, 3.0]]
        print(v1.values)
        # Expected output: to see what __str__() should do
        # [[0.0, 1.0, 2.0, 3.0]]
        print("Example 4:")
        print(v1 + v2)
        print(v1 - v2)
        print(v1 * 10)
        print(10 / v2)
    except Exception as e:
        print(e)
