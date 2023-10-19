# Сумма последовательности

# Дана последовательность целых чисел, завершающаяся числом 0.
# Найдите сумму всех этих чисел, не используя цикл.


def sum(a, b):
    if a != 0:
        return sum(0, b) + a
    if b != 0:
        return sum(a, 0) + b
    return 0


# С ипользованием глобальной переменной!
def inputn():
    global sumn
    n = int(input())
    if n != 0:
        sumn = sum(sumn, n)
        inputn()


sumn = 0
inputn()
print(sumn)
