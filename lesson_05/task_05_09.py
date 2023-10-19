# Диофантово уравнение - 2

# Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел
# от 0 до 1000, которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0,
# и выведите их количество.


def IsRoot(a, b, c, d, e, x):
    if x - e == 0:
        return False
    elif (a*x**3 + b*x**2 + c*x + d)/(x-e) == 0:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = 0
for x in range(0, 1001):
    count += IsRoot(a, b, c, d, e, x)
print(count)
