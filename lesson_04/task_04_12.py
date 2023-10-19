# Отрицательная степень

# Дано действительное положительное число a и целоe число n. Вычислите aⁿ.
# Решение оформите в виде функции power(a, n). Стандартной функцией
# возведения в степень пользоваться нельзя.


def power(a, n):
    i = 0
    pow = 1
    while i < abs(n):
        i += 1
        pow *= a
    if n < 0:
        pow = 1 / pow
    return pow


a = float(input())
n = int(input())
print(power(a, n))
