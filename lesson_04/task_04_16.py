# Сократите дробь

# Даны два натуральных числа n и m. Сократите дробь (n / m), то есть выведите
# два других числа p и q таких, что (n / m) = (p / q) и дробь (p / q) —
# несократимая. Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел.


def god(a, b):
    if a % b > 0:
        return god(b, a % b)
    else:
        return b


def ReduceFraction(n, m):
    div = god(n, m)
    return n // div, m // div


n = int(input())
m = int(input())
print(ReduceFraction(n, m)[0], ReduceFraction(n, m)[1])
