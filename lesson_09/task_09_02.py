# Добавить, умножить

# Добавьте в предыдущий класс следующие методы:
# __add__ принимающий вторую матрицу того же размера и возвращающий сумму матриц
# __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр
# __rmul__ делающий то же самое, что и __mul__. Этот метод будет вызван в том случае,
# аргумент находится справа. Можно написать __rmul__ = __mul__

# Например:
# В этом случае вызовется __mul__: Matrix([[0, 1], [1, 0]) * 10
# В этом случае вызовется __rmul__ (так как у int не определен __mul__ для матрицы справа):
# 10 * Matrix([[0, 1], [1, 0])
# Разумеется, данные методы не должны менять содержимое матрицы.

from sys import stdin


class Matrix():
    def __init__(self, matrix):
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
        result = list()
        for i in range(self.size()[0]):
            line = list()
            for j in range(self.size()[1]):
                line.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(line[:])
        return Matrix(result)

    def __mul__(self, other):
        result = list()
        for i in range(self.size()[0]):
            line = list()
            for j in range(self.size()[1]):
                line.append(self.matrix[i][j] * other)
            result.append(line[:])
        return Matrix(result)

    def __rmul__(self, other):
        return self * other


# exec(stdin.read())

# Task 2 check 1
m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m.size())
print()

# print(Matrix())
# Task 2 check 2
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
print()

# Task 2 check 3
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print()
print(alpha * m)
print()


r1 = [1, 0]
r2 = [0, 1]
m = Matrix([r1, r2])
print(m)
r1[0] = 1234567890
print(m)
print()


A1 = [1, 2]
A2 = [3, 4]
M1 = [A1, A2]
print(M1)
A1[0] = 'one'
print(M1)