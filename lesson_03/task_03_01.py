# Площадь треугольника

# Даны длины сторон треугольника. Вычислите площадь треугольника.

# Формула Герона:
# S = √p(p - a)(p - b)(p - c), где
# p = (a + b + c)/2

a = float(input())
b = float(input())
c = float(input())
epsilon = 5 * 10**-7

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)

if abs(S - round(S, 5)) < epsilon:
    print(S)
else:
    print('{0:.6f}'.format(S))
