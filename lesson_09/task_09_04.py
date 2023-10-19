# Умножение

# Внесите следующие изменения в предыдущую программу:

# Измените метод __mul__ таким образом, чтобы матрицы можно было умножать
# как на скаляры, так и на другие матрицы. В случае, если две матрицы
# перемножить невозможно, то тогда выбросьте ошибку MatrixError. Первая матрице
# в ошибке — это self, вторая — это второй операнд умножения.


from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = list()
        for i in range(len(matrix)):
            self.matrix.append(matrix[i][:])

    def __str__(self):
        strMatrix = ""
        for i in range(len(self.matrix)-1):
            strMatrix += "\t".join(map(str, self.matrix[i])) + "\n"
        strMatrix += "\t".join(map(str, self.matrix[len(self.matrix)-1]))
        return strMatrix

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if self.size() == other.size():
            result = list()
            for i in range(self.size()[0]):
                line = list()
                for j in range(self.size()[1]):
                    line.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(line[:])
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = list()
        if isinstance(other, int) or isinstance(other, float):
            for i in range(self.size()[0]):
                line = list()
                for j in range(self.size()[1]):
                    line.append(self.matrix[i][j] * other)
                result.append(line[:])
        elif isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            rangeI = range(self.size()[0])
            rangeJ = range(other.size()[1])
            rangeK = range(self.size()[1])
            for i in rangeI:
                # line = list()
                line = []
                for j in rangeJ:
                    sum = 0
                    for k in rangeK:
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    line.append(sum)
                result.append(line[:])
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    # def __rmul__(self, other):
    #     return self * other

    __rmul__ = __mul__

    def transpose(self):
        self.matrix = \
            [[self.matrix[j][i]
              for j in range(self.size()[0])]
                for i in range(self.size()[1])]
        return Matrix(self.matrix)

    @staticmethod
    def transposed(object):
        return Matrix(
            [[object.matrix[j][i]
              for j in range(object.size()[0])]
                for i in range(object.size()[1])])


exec(stdin.read())



''''# Task 4 check 3
mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(5 * m2)
print(m2 * (120 * mid * m1))'''


'''mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(0.5 * m2)
print(m2 * (0.5 * mid * m1))'''



# Task 4 check 1
mid = Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
m1 = Matrix([[3, 2], [-10, 0], [14, 5]])
m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])
print(mid * m1)
print()
print(mid * m2)
print()
print(m2 * m1)
print()
try:
    m = m1 * m2
    print("WA It should be error")
    print()
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)