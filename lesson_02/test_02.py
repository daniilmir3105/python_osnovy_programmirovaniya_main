# Подсчет суммы и оператор continue
print("Подсчет суммы и оператор continue")

# Найти сумму последовательности

# Мы не знаем, сколько в последовательности будет чисел. Знаем, что если ноль
# - последовательность заканчивается. Найти максимальное число в последовательности.

sumSeq = 0
now = int(input())
while now != 0:
    sumSeq += now # +=, -=, *=, **=
    now = int(input())
print(sumSeq)
print()


# Требуется вывести только положительные числа
sumSeq = 0
now = int(input())
while now != 0:
    if now > 0:
        print(now)
    now = int(input())
print()


# continue выполняет цикл с нового шага
# Т.е. проверяем новое условие
# В отличие от break, который вырубает цикл полностью

now = -1
while now != 0:
    now = int(input())
    if now <= 0:
        continue
    print(now)
print()
