# task_01_01 - Hello, %username!

name = input()
print('Hello, ', name, sep='', end="!")


# task_01_02 - Пингвины

quantity = input()
print('   _~_    ' * int(quantity))
print('  (o o)   ' * int(quantity))
print(' /  V  \  ' * int(quantity))
print('/(  _  )\\ ' * int(quantity))
print('  ^^ ^^   ' * int(quantity))


# task_01_03 - Дележ яблок - 1

N = int(input())  # Количество школьников
K = int(input())  # Количество яблок

print(K // N)  # Сколько яблок достанется каждому школьнику


# task_01_04 - Дележ яблок - 2

N = int(input())  # Количество школьников
K = int(input())  # Количество яблок

print(K % N)  # Сколько яблок останется в корзинке


# task_01_05 - Степень двойки

N = int(input())
print(2 ** N)


# task_01_06 - Последняя цифра

N = int(input())
print(N % 10)


# task_01_07 - Первая цифра двузначного числа

N = int(input())
print(N // 10)


# Вtask_01_08 - торая справа цифра

N = int(input())
print((N % 100) // 10)


# task_01_09 - Сумма цифр трехзначного числа

N = int(input())
print((N // 100) + ((N % 100) // 10) + (N % 10))


# task_01_10 - 100A

print('A' * 100)


# task_01_11 - Электронные часы - 1

N = int(input())
print((N // 60) % 24, N % 60)


# task_01_12 - Стоимость покупки

# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# Программа получает на вход три числа:
# A, B, N — целые, неотрицательные, не превышают 10000.

A = int(input())
B = int(input())
N = int(input())

totalCost = (A * 100 + B) * N

print(totalCost // 100, totalCost % 100)


# task_01_13 - Следующее и предыдущее

number = int(input())
# The next number for the number 179 is 180.
# The previous number for the number 179 is 178.
print('The next number for the number', number, 'is', number + 1, end=".")
print()
print('The previous number for the number', number, 'is', number - 1, end=".")


# task_01_14 - 0 в 1 и наоборот

n = int(input())
print(1 - n)


# task_01_15 - Следующее четное

N = int(input())
print(((N // 2) + 1) * 2)


# task_01_16 - 100 раз подряд в квадрате

N = input()
print(int(N*100)**2)


# task_01_17 - МКАД

# Длина Московской кольцевой автомобильной дороги — 109 километров.
# Байкер Вася стартует с нулевого километра МКАД
# и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?

# Программа получает на вход значение v и t.
# Если v>0, то Вася движется в положительном направлении по МКАД,
# если же значение v<0, то в отрицательном.
# (Гарантируется, что исходные числа — целые
# и находятся в промежутке от -1000 до +1000).
# Программа должна вывести целое число от 0 до 108 —
# номер отметки, на которой остановится Вася.

v = int(input())
t = int(input())

print((v * t) % 109)


# task_01_18 - Электронные часы - 2

# Электронные часы показывают время в формате h:mm:ss,
# то есть сначала записывается количество часов,
# потом обязательно двузначное количество минут,
# затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются
# до двузначного числа нулями.

# С начала суток прошло N секунд. Выведите, что покажут часы.

# Примечания
# Вывести числа можно поциферно.

N = int(input())
sec = N % 60
hour = N // (3600)
min = N // 60 - hour * 60
day = hour // 24
hour = hour - day * 24

# print(day, hour, min, sec)
print(hour, ':', min // 10, min % 10, ':', sec // 10, sec % 10, sep='')
# print(day * 24 * 3600 + hour * 3600 + min * 60 + sec)


# task_01_19 - Разность времен

# Даны два момента времени в пределах одних и тех же суток.
# Для каждого момента указан час, минута и секунда.
# Известно, что второй момент времени наступил не раньше первого.
#
# Определите сколько секунд прошло между двумя моментами времени.
#
# Программа на вход получает шесть целых чисел через перевод строки.
# Первые три целых числа соответствуют часам, минутам и секундам первого
# момента, следующие три числа соответствуют второму моменту.
#
# Часы задаются числом от 0 до 23 включительно. Минуты и секунды — от 0 до 59.
#
# Выведите число секунд между этими моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

passTime = t2 - t1
print(passTime)


# task_01_20 - Автопробег

# За день машина проезжает N километров.
# Сколько дней нужно, чтобы проехать маршут длиной M километров?

N = int(input())
M = int(input())

print((M - 1) // N + 1)


# task_01_21 - Улитка*

# Улитка ползет по вертикальному шесту высотой H метров,
# поднимаясь за день на A метров, а за ночь спускаясь на B метров.
# На какой день улитка доползет до вершины шеста?

# Программа получает на вход натуральные числа H, A, B.
# Гарантируется, что A>B, A<H.

# Программа должна вывести одно натуральное число.

H = int(input())
A = int(input())
B = int(input())

# h = A - B  # Проползет за целые сутки
# print(H, h)
# H - A # Расстояние, после которого доползет за день
# H - A - (A - B) * n # Расстояние, после которого доползет за n + 1 сутки

print((H - A - 1) // (A - B) + 2)


# task_01_22 - Симметричное число

# Дано четырехзначное число.
# Определите, является ли его десятичная запись симметричной.
# Если число симметричное, то выведите 1,
# иначе выведите любое другое целое число.
# Число может иметь меньше четырех знаков, тогда нужно считать,
# что его десятичная запись дополняется слева незначащими нулями.

n = int(input())
n1 = n // 1000
n2 = n // 100 - n1 * 10
n3 = n // 10 - n2 * 10 - n1 * 100
n4 = n % 10

# print(n1, n2, n3, n4)

# 10 * n1 + n2
# 10 * n4 + n3

print((10 * n1 + n2) - (10 * n4 + n3) + 1)


# task_01_23 - Максимум из двух*

# Напишите программу, которая считывает два целых числа A и B
# и выводит наибольшее значение из них. Числа — целые от 1 до 1000.

# При решении задачи можно пользоваться только целочисленными
# арифметическими операциями. Нельзя пользоваться нелинейными
# конструкциями: ветвлениями, циклами, функциями.

A = int(input())
B = int(input())

# print(A // B) # 0, если A < B
# print(int((A // B)/(A // B - 0.1)))
# 1 и 1, если A = B, итого - 2

# То же самое, что и выше
# print(int((A - B + 1)/(A - B + 0.99))*int((B - A + 1)/(B - A + 0.99)))

sign1 = int((A // B)/(A // B - 0.1))
sign2 = int((B // A)/(B // A - 0.1))

print(sign1 * A + sign2 * B - sign1 * sign2 * A)


# task_01_24 - Проверка на делимость*

# В этой задаче необходимо проверить, делится ли число A на число B нацело.
# Использовать можно только арифметические операции, использование любых
# видов ветвлений, функций и т.п. запрещено.

# Вводятся два натуральных числа A и B.

# Выведите "YES", если A кратно B и "NO" в противном случае.

A = int(input())
B = int(input())

# A % B # 0, если кратно
# A % B + 1 # 1, если кратно
# (A % B + 1) * "YES"
# print(int(1 / (A % B + 1)))
mult = int(1 / (A % B + 1))
print(mult * "YES" + (1 - mult) * "NO")
