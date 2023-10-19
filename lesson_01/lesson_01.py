# Неделя 1

# Типы данных и функции вывода
print('Типы данных и функции вывода')

print("Hello, world!")
print("Hello, Python!")
print(2 + 3)
print('2 + 3 =', 2 + 3) # Выражения в принте разделяются запятыми
print('1', '2', '3', sep = ' + ', end = ' ') # sep /separator/ - разделитель между элементами строки, end - символ в конце строки
print('=', 1 + 2 + 3)
# Если нам нужно сделать несколько разных разделителей для разных частей строк, то не остается другого выбора, кроме как использовать несколько подряд идущих функций print.
print()

print(1, 2, 3, 4, sep = ' + ')
print(' = ', 1 + 2 + 3 + 4, sep = '')

print(1, 2, 3, 4, sep=' + ', end='')
print(' = ', 1 + 2 + 3 + 4, sep='')

print()
print('############################################################################')
############################################################################
print()

# Переменные и арифметические выражения
print('Переменные и арифметические выражения')

print(11 + 6)
print(11 - 6)
print(11 * 6)
print(11 ** 6) # Возведение в степень
print(11 // 6) # Целочисленное деление
print(11 % 6) # Остаток от деления

# Остаток от деления
print((23 + 8) % 24) # Сколько времени покажут часы через 8 часов
print((7 - 8) % 24)# Что было за 8 часов до 7 утра

speed = 108
time = 12
dist = time * speed
print(dist)

time1 = 5
time2 = 8
dist = (time1 + time2) * speed


print(-15 // -7)
print(-15 % -7)

# ----------------------------------------------------------------------------#
# Пусть заданы два числа A и B, причем B > 0. Обозначим за C целую часть от деления A на B, C = A // B, а за D - остаток от деления A на B, D = A % B.
# Тогда должны выполняться следующие утверждения:
# A = B × C + D
# 0 ≤ D < B
# В случае, если B < 0, выполняются следующие утверждения:
# A = B × C + D
# B < D ≤ 0
# ----------------------------------------------------------------------------#

print()
print('############################################################################')
############################################################################
print()

# Операции над строками
print('Операции над строками')

phrase = 'Hasta la vista'
who = '"baby"'
print(phrase, ', ', who, '!', sep="")

# Превращаем число в строку
# Функция str
ans = 2 + 3
expr = '2 + 3 = '
# Конкатенация. Операция склеивания объектов линейной структуры, обычно строк.
# Например, конкатенация слов «микро» и «мир» даст слово «микромир».
print(expr + str(ans))
print(ans + 1)
# PEP 8 - требования к оформлению программ

goodByePhrase = 'Hasta la vista'
person = 'baby'
print(goodByePhrase + ', ' + person + '!')

answer = '2 + 3 = ' + str(2 + 3)
print(answer)

print()
print('############################################################################')
############################################################################
print()

# Чтение данных
print('Чтение данных')

print('abc' * 3)
print()

# Для чтения данных существует функция input()
# name = input() Считывает все символы до перевода строки в string
# line - строка, оканчивающаяся переводом строки
# print('Hello,', name)

# a = int(input())
# b = int(input())
#print(a + b)
# int - преобразование строки в число - сокращение от английского integer, "целое число"

print(int('10'*10))
print(int('10'*10) ** 2)


word = 'Bye'
phrase = word * 3 + '!'
print(phrase)

print()
print('Введите имя')
name = input()
print('I love', name)

print()
print('Введите два числа')
a = int(input())
b = int(input())
print(a + b)

# В строках могут быть не только буквы, цифры и прочие знаки препинания, но и, например, символы табуляции и перевода строки.
# Чтобы использовать эти символы в константной строке в коде программы необходимо записывать их как \t и \n соответственно.
# Использование бэкслеша перед символом называется экранирование.
# Также существуют и другие символы, которые требуют бэкслеша перед собой.
# Например, это кавычки \' и \'' (использование бэкслеша просто необходимо, если в строке используются оба типа кавычек),
# а также, собственно, символ бэкслеша, который надо записывать как \\.
# В случае считывания с помощью input символы в консоли экранировать не нужно.

print()
print('############################################################################')
############################################################################
print()

# Примеры решения задач
print('Примеры решения задач')

print()
print('Введите две суммы денег /по два числа/')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
cost1 = a * 100 + b
cost2 = c * 100 + d
totalCost = cost1 + cost2
print(totalCost // 100, totalCost % 100)

print()
print('Введите количество заработанных жизней')
n = int(input())
print(n % 256)

print()
print('############################################################################')
############################################################################
print()

# Еще примеры решения задач
print('Еще примеры решения задач')

print()
print('Введите число и количество цифр, которые необходимо отрезать')
n = int(input())
k = int(input())
print(n // 10**k)

a = int(input())
b = int(input())
print((a - 1) // b + 1) # Мое
print((a + b - 1) // b) # Преподавателя

print()
print('############################################################################')
############################################################################
print()

# Как переменные устроены внутри
print('Как переменные устроены внутри')

# В языке Питон все переменные являются ссылками на объекты. Каждый объект имеет тип (нам известны int и str)
# и содержимое, в нашем случае конкретное число или последовательность символов.
#
# Переменные (ссылки) в языке Питон удобно представлять себе как ярлычки на веревочке,
# которые привязаны к какому-то объекту. Вообще говоря, к одному объекту может быть привязано сколь угодно много ярлыков.
# Различные переменные с одинаковым значением фактически являются ярлычками, привязанными к одному и тому же объекту.
#
# Типы int и str в Питоне являются неизменяемыми. Любое присваивание в Питоне не может изменить неизменяемый тип,
# а может только изменить место, на которое указывает ссылка (и, при необходимости, сконструировать новый объект).
#
# Например, команда x = 2, приведет сначала к созданию объекта типа "целое число" со значением 2 в памяти,
# а затем к созданию переменной x, которая будет являться ссылкой на этот объект.
#
# Если после этого написать y = 2, то новый объект со значением 2 создаваться не будет,
# а создастся только новая ссылка с именем y, показывающая на тот же самый объект, что и ссылка x.
#
# Если теперь написать строку x = 3, то с объектом со значением 2 ничего не случится, ведь он не неизменяемый.
# Создастся новый объект со значением 3, ссылка x отвяжется от объекта со значением 2 и привяжется к новому объекту 3.
# При этом к объекту 2 останется привязана ссылка y.
#
# Если изменить и значение переменной y, то у объекта 2 не останется ссылок на него.
# Поэтому он может быть безболезненно уничтожен при сборке мусора, ведь получить к нему доступ уже невозможно -
# на него не ссылается ни одна переменная.
#
# Константные значения в программе (например, явно заданные числа в исходном коде программы)
# также являются ссылками на объекты, содержимое которых совпадает со значением этих констант.
# Однако эти ссылки не могут быть изменены и не могут участвовать в присваивании с левой стороны от знака =.