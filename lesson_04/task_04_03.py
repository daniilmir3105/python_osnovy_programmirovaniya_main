# Периметр треугольника

# Напишите функцию, вычисляющую длину отрезка по координатам его концов.
# С помощью этой функции напишите программу, вычисляющую периметр треугольника
# по координатам трех его вершин.
#
# На вход программе подается 6 целых чисел — координат x₁, y₁, x₂, y₂, x₃, y₃
# вершин треугольника. Все числа по модулю не превосходят 30 000.
#
# Выведите значение периметра этого треугольника с точностью до 6 знаков после
# десятичной точки.


def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(distance(x1, y1, x2, y2) +
      distance(x1, y1, x3, y3) +
      distance(x2, y2, x3, y3))
