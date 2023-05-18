class Vector:
    def __init__(self, val = None) -> None:
        self.values = []
        if type(val) is tuple:
            if len(val) == 2 and val[0] < val[1]:
                for i in range(val[0], val[1]):
                    self.values.append([float(i)])
                self.shape = (len(self.values), 1)
            else:
                raise Exception("Not a valid tuple")
        elif (type(val) is int) and (val > -1):
            for i in range(val):
                self.values.append([float(i)])
            self.shape = (len(self.values), 1)
        elif type(val) is list:
            self.values = val
            if len(val) > 1:
                for i in val:
                    if len(i) > 1:
                        raise Exception("Vector doesn't accept a matrix") 
                self.shape = (len(val), 1)
            elif len(val) == 1:
                self.shape = (1, len(val[0]))
            else:
                raise Exception("Invalid list")
        else:
            raise Exception("Not a valid init value")
    def dot(self, b: type):
        if self.shape != b.shape:
            raise Exception("vectors are not of the same shape")
        dot = 0
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                dot += self.values[0][i] * b.values[0][i]
        else:
            for i in range(len(self.values)):
                dot += self.values[i][0] * b.values[i][0]
        return dot
    def T(self):
        vec = []
        if self.shape[0] == 1:
            for i in self.values[0]:
                vec.append([i])
            self.shape = (self.shape[1], self.shape[0])
        else:
            for i in self.values:
                vec.append(i[0])
            vec = [vec]
            self.shape = (self.shape[1], self.shape[0])
        self.values = vec
        return vec
    def __add__(self, b):
        if self.shape != b.shape:
            raise Exception("vectors are not of the same shape")
        sum = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                sum.append(self.values[0][i] + b.values[0][i])
            sum = [sum]
        else:
            for i in range(len(self.values)):
                sum.append([self.values[i][0] + b.values[i][0]])
        return sum
    def __radd__(self, b):
        if self.shape != b.shape:
            raise Exception("vectors are not of the same shape")
        sum = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                sum.append(b.values[0][i] + self.values[0][i])
            sum = [sum]
        else:
            for i in range(len(self.values)):
                sum.append([b.values[i][0] + self.values[i][0]])
        return sum
    # add & radd : only vectors of same shape.
    def __sub__(self, b):
        if self.shape != b.shape:
            raise Exception("vectors are not of the same shape")
        sub = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                sub.append(self.values[0][i] - b.values[0][i])
            sub = [sub]
        else:
            for i in range(len(self.values)):
                sub.append([self.values[i][0] - b.values[i][0]])
        return sub
    def __rsub__(self, b):
        if self.shape != b.shape:
            raise Exception("vectors are not of the same shape")
        sub = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                sub.append(b.values[0][i] - self.values[0][i])
            sub = [sub]
        else:
            for i in range(len(self.values)):
                sub.append([b.values[i][0] - self.values[i][0]])
        return sub
    # sub & rsub: only vectors of same shape.
    def __truediv__(self, num):
        div = []
        if num == 0:
            raise Exception("Division by 0")
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                div.append(self.values[0][i] / num)
            div = [div]
        else:
            for i in range(len(self.values)):
                div.append([self.values[i][0] / num])
        return div
    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __rtruediv__(self, num):
        div = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                div.append(num / self.values[0][i])
            div = [div]
        else:
            for i in range(len(self.values)):
                div.append([num / self.values[i][0]])
        return div
    # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
    def __mul__(self, num):
        mul = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                mul.append(self.values[0][i] * num)
            mul = [mul]
        else:
            for i in range(len(self.values)):
                mul.append([self.values[i][0] * num])
        return mul
    def __rmul__(self, num):
        mul = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                mul.append(num * self.values[0][i])
            mul = [mul]
        else:
            for i in range(len(self.values)):
                mul.append([num * self.values[i][0]])
        return mul
    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).
    def __str__(self):
        return str(self.values)
    def __repr__(self):
        return self.values
    # must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspondi
