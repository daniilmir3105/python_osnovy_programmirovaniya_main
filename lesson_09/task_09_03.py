# Ошибки, транспонирование

# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2
# (ссылки на матрицы).

# В класс Matrix внесите следующие изменения:
# Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы
# разных размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError
# стало первым аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует
# экземпляр класса Matrix)
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.
# Пример статического метода. https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование_на_Python


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
        for i in range(self.size()[0]):
            line = list()
            for j in range(self.size()[1]):
                line.append(self.matrix[i][j] * other)
            result.append(line[:])
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



# Task 3 check 1
# Check exception to add method
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)

print()


# Task 3 check 2
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
m1 = m.transpose()
print(m)
print(m1)
print()


# Task 3 check 3
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
print(Matrix.transposed(m))
print(m)
print()
m = Matrix()
# print(m.transpose([[10, 10], [0, 0], [1, 1]]))
print()

'''
r1 = [1, 0]
r2 = [0, 1]
m = Matrix([r1, r2])
print(m)
r1[0] = 1234567890
print(m)
'''