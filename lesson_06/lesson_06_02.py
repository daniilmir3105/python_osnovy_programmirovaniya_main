# Именованный параметр key

# Итак, мы хотим хотим отсоритовать по убыванию роста, но внутри по имени - в алфавитном порядке
# Для этого можно произвести некоторую модификацию. Для этого рост заменим на отрицательное, но такое же
# по модулю, число
# Тогда отсортировка будет давать нормальный результат
# Затем, конечно же, данные нужно будет вернуть в исходный вид

p = [(-172, 'Vasya'),
     (-180, 'Petya'),
     (-172, 'Fedya')]
p.sort()
print(*p)

for i in range(len(p)):
    # Поскольку у нас кортеж - неизменяемый - нам придется конструировать новый кортеж
    p[i] = (-p[i][0], p[i][1])
print(*p)
# Что и требовалось получить

# Так делать не очень удобно, поэтому в Питоне существует способ решать эту проблему по другому

# Пусть хотим отсортировать список по длине строки
ls = ['abcd', 'bc', 'xyz']
ls.sort(key=len)
# key - ключ - это функция, которая будет применяться к каждому объекту списка,
# и считать от него некоторое значение, по которым будет происходить сравнение

# У нас для каждого элемента будет вызываться функция len, и по этим значениям уже отсортируется
print(*ls)

# Пусть есть строки одинаковой длины
ls = ['abcd', 'bc', 'xyz', '1234']
ls.sort(key=len)
print(*ls)
# Та строка, которая стояла раньше в исходном списке, так же оказалась раньше
# Т.е. взаимный порядок одинаковых по ключу элементов сохранился
# Это свойство называется устойчивостью сортировки
# И в Питоне стандартная сортировка устойчивая
# Т.е. если ключи для каких-то объектов одинаковые, то они расположатся точно так же,
# как стояли в исходном списке

# Сортировка точек по возрастанию расстояния от начала координат до этой точки
points = [
    (1, 1),
    (10, 1),
    (5, 5)
]
# points.sort(key=) # В качестве ключа будем передавать функцию, считающую расстояние от нуля до точки
# Есть функция подсчета гипотенузы в math, но там результат - вещественное число, что плохо
# Если |a| < |b|, то a^2 < b^2
def sqrDist(point):
    return point[0]**2 + point[1]**2
points.sort(key=sqrDist)
print(*points)
# Теперь можно писать свои функции и не портить данные

# Вернемся к сортировке людей
p = [(172, 'Vasya'),
     (180, 'Petya'),
     (172, 'Fedya')]
p.sort()
print(*p)
# Нужно придумать функцию, которая будет возвращать измененный кортеж
def makeTuple(man): # Получаем кортеж
    return [-man[0], man[1]] # Возвращаем так же кортеж
p.sort(key=makeTuple)
print(*p)

# Таким образом, с помощью параметра key мы можем передавать функцию, модифицирующую данные,
# и при этом не заниматься тем, чтобы испортить данные, отсортировать, восстановить данные

# Функция, которая возвращает ключ сравнения, может возвращать что угодно сравнимое - строку,
# число, вещественное число, кортеж, кортеж сложной структуры и т.д. Главное, чтобы они были
# сравнимы между собой


# Примеры в учебном тексте
n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    manData = (int(tempManData[0]), tempManData[1])
    peopleList.append(manData)
peopleList.sort()
for manData in peopleList:
    print(' '.join(map(str, manData)))

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    manData = (-int(tempManData[0]), tempManData[1])
    peopleList.append(manData)
peopleList.sort()
for badManData in peopleList:
    manData = (-badManData[0], badManData[1])
    print(' '.join(map(str, manData)))

n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print('\n'.join(sorted(strings, key=len)))

def dist(point):
    return point[0] ** 2 + point[1] ** 2

n = int(input())
points = []
for i in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
points.sort(key=dist)
for point in points:
    print(' '.join(map(str, point)))



# "Структуры" в Питоне

# В ЯП Питон кортежии предназначены для хранения разнородных данных
# Пока немного данных, помнить содержание структуры не сложно
# Но если структура сложная, то помнить тяжело

# В других ЯП есть объект структура /в Pascal - record/
# В Питоне в чистом виде такого нет
# Но есть несколько способов сделать что-то похожее

# Способ первый. Используем класс как структуру
# Создаем новый тип объекта. И здесь /в сл. описания структуры объекта/ принято
# писать с большой буквы
class Man:
  height = 0
  name = ''

# В Питоне все списки состоят из ссылок
p = []
n = int(input())
for i in range(n):
    h, n = input().split() # рост, имя
    h = int(h)
    man = Man() # Пустые скобки т.к. без параметров
    # Теперь мы можем обращаться к полям нашего класса, нашей структуры
    man.height = h
    man.name = n
    p.append(man)
# Теперь есть список людей, каждый из которых описан в виде класса /на самом деле в виде структуры/
# Пишем функцию, возвращающую ключ для сортировки
def makeTuple():
    return (man.height, man.name)  # Круглые скобки пишем, чтобы было понятно, что это - кортеж
p.sort(key=makeTuple)
for now in p:  # Перебираем элементы итерируемого списка
    print(now.heigth, now.name)

# Когда очень много полей, это очень удобно
# Код становится гораздо более читабельным и понятным

# Кроме того, структуры можно поддерживать через словари. Или через named tuple - именованный кортеж.


'''Для хранения сложных записей во многих языках есть специальные типы данных, такие как struct в C++ или record в Паскале.
Переменная типа структура содержит в себе несколько именованных полей. Например, возвращаясь 
к задаче сортировки людей по убыванию роста, нам было бы удобно хранить описание каждого человека в виде структуры 
с двумя полями: ростом и именем.
В чистом виде типа данных "структура" в стандарте языка Питон нет. Есть несколько способов реализации аналога структур: 
namedtuple из библиотеки collections, использование словарей (будет рассмотрено в следующих лекциях) 
или использование классов в качестве структур. Рассмотрим на примере последний способ.
Напомним условие задачи: людей нужно упорядочить по убыванию роста, но в случае одинакового роста они 
должны быть упорядочены по фамилии. Решение с использованием классов в качестве структур будет выглядеть так:'''
class Man:
    height = 0
    name = ''

def manKey(man):
    return (-man.height, man.name)

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[0])
    man.name = tempManData[1]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.height, man.name)

'''Для того чтобы пользоваться классами как структурами мы создаем новый тип данных Man. В описании класса 
мы перечисляем имена всех полей и их значения по-умолчанию.
В дальнейшем мы можем создавать объекты класса Man (это делается строкой man = Man()), которые сначала 
проинициализируют свои поля значениями по умолчанию. Доступ к полям класса осуществляется через точку.
Функция сравнения принимает объект класса и генерирует ключ, по которому эти объекты будут сравниваться при сортировке.
Использование структур для описания сложных объектов намного предпочтительнее, чем использование кортежей. 
При количестве параметров больше двух использование кортежей запутывает читателя и писателя кода, т.к. 
совершенно невозможно понять что хранится в badNamedTuple[13] и легко понять что хранится в goodNamedStruct.goodNamedField.'''



# Лямбда-функции

# Когда функция нужна только один раз, но она обязана быть, придумали лямбда-функции
points = [(1, 1),
          (5, 1),
          (10, 10)
          ]
def sqrDist(p):
    return p[0]**2 + p[1]**2
points.sort(key=sqrDist)
print(*points)

# Мы хотим избавиться от данной функции, потому что она нам больше не пригодится
# Но передавать нужно функцию

# Здесь мы воспользуемся лямбда-функцией
points.sort(key=lambda p: p[0]**2 + p[1]**2) # p - передаваемый параметр
print(*points)

# Функция в Питоне так же является объектом
# И мы можем сохранить ее в переменную
# И эта переменная будет вести себя как функция
# По сути мы можем дать имя для функции

# Дать имя для лямбда-функции мы тоже можем
# Более того, мы можем дать ей имя, как раньше называлась наша функция
# И теперь использовать имя функции
sqrDiat=lambda p: p[0]**2 + p[1]**2
points.sort(key=sqrDiat)

# Но если функция используется несколько раз, рекомендуется ее описывать через def

# Пусть есть последовательность чисел. И мы хотим получить последовательность
# квадратов этих чисел
x = [1, 5, 2, 3]
# Функция map в качестве функции может применять не только стандартную функцию, но и пользовательскую
y = list(map(lambda x: x**2, x))
print(*y)


'''Отличие лямбда-функции также заключается в том, что у неё нет имени и, следовательно, 
вызов её по имени невозможен. Пока единственным применением лямбда-функций для нас 
может служить их передача в качестве параметра в такие функции как sort или map. Например, 
с помощью лямбда-функции мы можем вывести список квадратов всех чисел от 1 до 100 всего в одну строку:'''
print(' '.join(map(lambda x: str(x**2), range(1, 101))))

'''Лямбда-функция может принимать несколько параметров (тогда после слова lambda нужно записать 
их имена через запятую), однако при использовании их в sort или map параметр должен быть всегда один.'''

'''В языке Питон функция также является объектом и мы можем создать ссылку на объект типа функция. 
Например, две записи функции возведения в квадрат эквивалентны:'''
def traditionalSqr(x):
    return x**2
lambdaSqr = lambda x: x**2

print(traditionalSqr(3))
print(lambdaSqr(3))
'''Такой подход позволяет переиспользовать лямбда-функции, но в подавляющем большинстве случаев 
стоит пользоваться стандартным объявлением функции - это упрощает чтение и отладку программы'''



# Именованные параметры и неопределенное число параметров

# Пусть мы хотим сделать функцию печати списка с использованием разделителя
def printList(lst, mySep=' '):
    for i in range(len(lst) - 1):
        print(lst[i], mySep, sep='', end='')
    print(lst[-1], sep='')  # Последний элемент надо напечатать отдельно
printList([1, 2, 3]) # Используется только for, поэтому можно передать в функцию не только список, но и что угодно итерируемое
printList([5, 6, 7])
# Мы хотим напечатать перевод строки в конце списка. Нужно просто print() в конце списка
# Однако есть еще одна проблема - после последнего элемента в списке тоже печатается разделитель
# Для ее решения последний элемент списка напечатем отдельно

# Хотим, чтобы пробел в качестве второго параметра подставлялся автоматически
# Для этого можно сделать именованный параметр со значенимем по умолчанию
# def printList(lst, mySep=' '):
# mysep - именованный параметр

'''Именованный параметр в объявлении функции должен идти после основных параметров. В списке параметров 
записывается его имя, а затем значение по-умолчанию (т.е. то значение, которое будет подставляться на место 
соответствующего параметра, если он не был передан при вызове функции).'''


# Пусть мы хотим написать функцию, которая умеет суммировать любое количество переданных ей параметров
# def mySum(*args):
# *args - список всех переданных ей параметров, т.е. параметры упакуются в список, и этот список придет на вход функции
def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4))
print(mySum(1))

# Стандартная функция суммирования sum работает максимум с двумя параметрами
# Наша же функция принимает произвольное число параметров, упаковывает их в список, и уже от одного параметра,
# от списка, вызывает станартную функцию sum

# Без вызова sum
def mySum(*args):
    nowSum = 0
    for now in args:
        nowSum += now
    return nowSum
print(mySum(1, 2, 3, 4))
print(mySum(1))

# Пусть есть и просто аргумент, и неопределенное количество аргументов
# Например, мы хотим считать минимум из последовательности
def myMin(first, *others): # Параметры со звездочкой могут быть только последними
    nowMin = first
    for now in others:
        if now < nowMin:
            nowMin = now
    return nowMin
print(myMin(10, 5, 3, 4))
print(myMin(1))

# Таким образом, можно принимать как некоторое количество фиксированных,
# так и некоторое количество определенных параметров.
# В начале некоторое количество обязательных, а затем - не обязательных параметров.

# Так же можно намешать именнованных параметры, описывая их в конце списка получаемых параметров.
# /Например, как в функции print./

'''Параметр со звездочкой всегда должен быть последним, за исключением ситуации, когда в функции 
также определены именованные параметры.'''


