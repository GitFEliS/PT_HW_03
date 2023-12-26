import numpy as np


class Matrix:
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Wrong input")
        self.data = data

    def __add__(self, rhs):
        if len(self.data[0]) != len(rhs.data[0]) or len(self.data) != len(rhs.data):
            raise ValueError("Can't sum, matricies with different sizes")

        res = []

        for i, _ in enumerate(self.data):
            res.append([])
            for j, _ in enumerate(self.data[0]):
                res[i].append(self.data[i][j] + rhs.data[i][j])

        return Matrix(res)

    def __mul__(self, rhs):
        if len(self.data[0]) != len(rhs.data[0]) or len(self.data) != len(rhs.data):
            raise ValueError("Can't mul, matricies with different sizes")

        res = []

        for i, _ in enumerate(self.data):
            res.append([])
            for j, _ in enumerate(self.data[0]):
                res[i].append(self.data[i][j] * rhs.data[i][j])

        return Matrix(res)

    def __matmul__(self, rhs):
        if len(self.data[0]) != len(rhs.data):
            raise ValueError(
                "Can't matmul, matricies with incomplitable sizes")

        res = []

        for i, _ in enumerate(self.data):
            res.append([])
            for j, _ in enumerate(rhs.data[0]):
                res[i].append(sum([self.data[i][k] * rhs.data[k][j]
                              for k, _ in enumerate(self.data[0])]))

        return Matrix(res)

    def __str__(self):
        return "[[" + "], \n[".join([", ".join(map(str, row)) for row in self.data]) + "]]"


if __name__ == "__main__":
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    m2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    with open("matrix+.txt", "w") as f:
        f.write(str(m1 + m2))

    with open("matrix*.txt", "w") as f:
        f.write(str(m1 * m2))

    with open("matrix@.txt", "w") as f:
        f.write(str(m1 @ m2))
