# Длина отрезка

# Даны четыре действительных числа: x₁, y₁, x₂, y₂. Напишите функцию
# distance(x1, y1, x2, y2), вычисляющую расстояниемежду точкой (x₁,y₁)
# и (x₂,y₂). Считайте четыре действительных числа и выведите результат работы
# этой функции.


def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
