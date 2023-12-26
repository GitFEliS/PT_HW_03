import numpy as np


class OpsMixin:
    def __add__(self, rhs):
        return self.__class__(np.add(self.data, rhs.data).tolist())

    def __mul__(self, rhs):
        return self.__class__(np.multiply(self.data, rhs.data).tolist())

    def __matmul__(self, rhs):
        return self.__class__(np.matmul(self.data, rhs.data).tolist())

    def __sub__(self, rhs):
        return self.__class__(np.subtract(self.data, rhs.data).tolist())


class FileWriterMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.__str__())


class ReprMixin:
    def __str__(self):
        return "[[" + "], \n[".join([", ".join(map(str, row)) for row in self.data]) + "]]"


class GetSetMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val


class Matrix(OpsMixin, FileWriterMixin, ReprMixin, GetSetMixin):
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Wrong input")
        self.data = data


if __name__ == "__main__":
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    m2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    (m1+m2).write_to_file("matrix+.txt")
    (m1*m2).write_to_file("matrix*.txt")
    (m1@m2).write_to_file("matrix@.txt")
