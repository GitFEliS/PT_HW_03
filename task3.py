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


class HashMixin:
    def __hash__(self):
        """Считает хеш как XOR елементов матрицы, если всречаем такой-же как текущий, пропускаем, чтобы не обнулиться"""
        cur = 0
        for row in self.data:
            for elem in row:
                if cur == hash(elem):
                    continue
                cur ^= hash(elem)

        return cur


class Matrix(OpsMixin, FileWriterMixin, ReprMixin, GetSetMixin, HashMixin):
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Wrong input")
        self.data = data


if __name__ == "__main__":
    A = Matrix([[55, 44], [33, 22]])
    C = Matrix([[22, 33], [44, 55]])
    if (hash(A) != hash(C)):
        raise ValueError("hash not colide")

    B = Matrix([[1, 2], [3, 4]])
    D = Matrix([[1, 2], [3, 4]])

    A.write_to_file("A.txt")
    B.write_to_file("B.txt")
    C.write_to_file("C.txt")
    D.write_to_file("D.txt")

    (A@B).write_to_file("AB.txt")
    (C@D).write_to_file("CD.txt")

    with open("hash.txt", "w") as f:
        f.write(f"hash AB:{hash(A@B)}\n")
        f.write(f"hash CD:{hash(C@D)}\n")
