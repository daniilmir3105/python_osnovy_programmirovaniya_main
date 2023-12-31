# Встроенные функции для работы с последовательностями

# sum - суммирование любого iterable
# max, min
# map - умеет применять функцию к каждому элементу iterable
# sorted - функция, возвращающая отсортированную последовательность
sum()
max()
min()
sorted()
map()

# И новые функции:
filter()
# В каком порядке писать параметры?
# filter позволяет отфильтровать элементы последовательности

# Например, нужно считать последовательность чисел и напечатать только положительные числе
numbers = map(int, input().split())
print(*filter(lambda x: x > 0, numbers)) # Вернет True при x > 0 и False в противном случае

# Как писать совсем в функциональном стиле. В функциональном программировании стараются
# использовать исключительно неизменяемые объекты и вообще-то часто не используют переменные совсем.

print(*filter(lambda x: x > 0, map(int, input().split()))) # Вернет True при x > 0 и False в противном случае

# Попробуем навести порядок
# Идея: каждый параметр будет на новой строке;
# Если параметров в функции несколько, то они будут с тем же отступом написаны.
# Если это бо́льшие вложения, то с бо́льшим отступом.

print(
    *filter(
        lambda x: x > 0,
        map(
            int,
            input().split()
        )
    )
)
# Теперь строк стало 9 вместо 1, но какое-то понимание появилось


# У нас отступами обозначаются фактически новые вложенные функции. Читать это нужно с более
# вложенных к менее вложенным. Если вдруг вам на работе, например, в проекте попадется любитель
# функционального программирования, даже если вы сами не пишете в таком стиле, то хотя бы понять,
# что он написал, было бы очень полезно. Как это читать? Начинаем с наиболее вложенного. Вот оно, map.
# Что мы здесь можем увидеть? В принципе, достаточно понятно. Мы делаем список чисел. Затем берем
# следующий по вложенности уровень — filter. Мы знаем, что такое filter. Вот у нас первый параметр —
# это функция, когда у нас все хорошо. И вот второй параметр — список чисел, мы уже знаем, то есть мы
# отфильтровали положительные числа. Переходя к самому внешнему уровню, мы понимаем, что там у нас находится
# print — печать, то есть мы печатаем результат фильтрации. Вот так вот мы прочитали функциональную программу,
# не то чтобы даже снизу вверх, а с наиболее вложенного к наименее вложенному. Такой порядок чтения.


# Еще одна функция - enumerate - занумеровать
enumerate()
# Нужна для нумерации элементов последовательности
# Единственный параметр, который она принимает, это сама последовательность.
# И необязательный параметр — с какого числа начинать нумеровать.

print(*enumerate('abcde'))
# Мы получаем кортежи. В начале стоит номер - нумерация с нуля, а затем стоит очередной элемент,
# взятый из того, что мы передали в качестве параметра.
# Таким образом, мы можем что-то занумеровать, и иногда это бывает полезно.


# Еще две полезные функции — это any и all. Что такое any и all?
# Any возвращает истину, если хотя бы один элемент из iterable, который должен состоять из bool,
# из логических значений, истинный, хотя бы один.

print(any((True, False, True)))  # True, если хотя бы один элемент истинный
print(all((True, False, True)))  # True, если все элементы истинны

# Когда применяется?

# Пусть мы хотим узнать: все ли числа в нашей последовательности положительны?

print(
    all(
        map(
            lambda x: x > 0,
            map(
                int,
                input().split()
            )
        )
    )
)


# Разумно писать, начиная с конца


'''В языке Питон есть много функций, которые принимают в качестве параметра iterable и могут сделать что-то полезное. 
С некоторыми из них, такими как sorted или map мы уже немного знакомы. Рассмотрим еще некоторые из них:
sum - находит сумму всех элементов iterable.
min, max - находит минимум и максимум в последовательности iterable.
map - умеет принимать более двух параметров. Например, такая запись map(f, iterA, iterB) 
вернет iterable со значениями f(iterA[0], iterB[0]), f(iterA[1], iterB[2]), ...
filter(predicate, iterable)- применяет функцию predicate ко всем элементам iterable и возврщает iterable, 
который содержит только те элементы, которые удовлетворяли предикаты (т.е. функция predicate вернула True). '''

'''Например, так может выглядеть решение задачи о поиске минимального положительного элемента в списке:'''
print(min(filter(lambda x: x > 0, map(int, input().split()))))
'''Здесь в качестве предиката использована лямбда-функция, которая возвращает True при значении параметра 
больше 0, а в качестве входного iterable - результат вызова map для функции int и нарезанного на слова ввода. 
Функция min применена к тому iterable, который был возвращен функцией filter.'''

'''enumerate - возвращает кортежи из номера элемента (при нумерации с нуля) и значения очередного элемента. 
С помощью enumerate, например, удобно перебирать элементы iterable (доступ по индексу в которых невозможен) 
и выводить номера элементов, которые обладают некоторым свойством:'''
f = open('data.txt', 'r', encoding='utf8')
for i, line in enumerate(f):
    if line.strip() == '':
        print('Blank line at line', i)

'''any, all - возвращают истину, если хотя бы один или все элементы iterable истинны соответствнно. 
Например, так можно проверить, не превышают ли все члены последовательности 100 по модулю:'''
print(all(map(lambda x: abs(int(x)) <= 100, input().split())))

'''zip(iterA, iterB, ...) - конструирует кортежи из элементов (iterA[0], iterB[0], ...), (iterA[1], iterB[1], ...), ...'''


