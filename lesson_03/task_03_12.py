# Система линейных уравнений - 1

# Даны вещественные числа a, b, c, d, e, f.
# Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение.
# Выведите два числа x и y, являющиеся решением этой системы.

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (e * d - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)
print(x, y)
