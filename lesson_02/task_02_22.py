# Котлеты*

# На сковородку одновременно можно положить k котлет. Каждую котлету нужно
# с каждой стороны обжаривать m минут непрерывно. За какое наименьшее время
# удастся поджарить с обеих сторон n котлет?
#
# Программа получает на вход три числа: k, m, n.
#
# Программа должна вывести одно число: наименьшее количество минут.

k = int(input())
m = int(input())
n = int(input())

# 2 * n - сторон /жарки/
# k котлет за раз /m минут/
# (2 * n) // k - сковородок
if k >= n:
    print(2 * m)
else:
    print(int((2 * n - 0.01) // k + 1) * m)
