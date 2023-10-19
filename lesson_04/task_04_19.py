# Сумма последовательности

# Дана последовательность целых чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.


def sum(a, b):
    if a != 0:
        return sum(0, b) + a
    if b != 0:
        return sum(a, 0) + b
    return 0


def suminput():
    n = int(input())
    if n != 0:
        return sum(suminput(), n)
    else:
        return 0


sumn = suminput()
# inputn()
print(sumn)
