# Множества и словари


# Множества и хеш-функции

# Множество – это такой математический объект, где некоторые элементы могут
# присутствовать или не присутствовать. То есть максимум он там может быть
# в одном экземпляре.

'''Но пусть у нас задача, что подается абсолютно любое целое число и опять же нужно каким-то 
образом реализовать множество. Что мы можем сделать? Мы можем придумать функцию, которая отображает 
элемент из большого множества, из множества всех чисел, в какое-то маленькое множество, например, 
в наш список длиной 5. Такая функция называется хеш-функцией от числа x переданного, и она может быть, 
в принципе, любой. Главное, чтобы она имела область значений в нашем случае от 0 до 4. Часто используется 
функция «остаток от деления». Очень простая и быстро вычисляемая функция. В нашем случае k = 5. И в результате 
выполнения вычисления такой функции у нас будут получаться числа как раз от 0 до 4.

Естественно, поскольку наше множество маленькое, а чисел очень много, у нас иногда будет возникать коллизия. 
Что это такое? Это когда два разных элемента имеют одну и ту же хеш-функцию. Эту проблему мы тоже можем решить. 
Для этого достаточно вместо одной ячейки, то есть списка чисел, делать список списков. То есть теперь по индексу 2 
в нашем списке содержится не одно значение, а уже список со всеми значениями, которые содержатся в множестве 
и имеют хеш-функцию 2. Нам достаточно пробежаться по всему списку и проверить есть ли там наше число.

Давайте посмотрим как это позволяет нам заполнять такой небольшой массив большими числами. Точно так же 
мы создаем список, состоящий из пяти элементов с индексами от 0 до 4. И, допустим, теперь нам говорится: 
добавь в множество число 7. Если мы добавляем число 7, то мы считаем остаток от деления на 5, получается 
он равен 2. И мы записываем уже сюда не галочку, а конкретное число. Если, например, мы добавим число 4, 
то оно запишется сюда. И проверка становится чуть сложнее. Теперь нужно посчитать хеш-функцию, пойти в элемент 
с соответствующим индексом и проверить, содержится ли там ровно то число, которое было в нашем запросе. 
Так мы можем, например, поискать 2. Пойти по индексу 2 (хеш-функция от двойки равна 2) и обнаружить там 7. 
Значит 2 в нашем множестве нет.

Например, у нас есть строка из букв a b c a b Нам нужно каким-то образом научиться превращать ее в число. 
Что мы можем сделать? Мы можем просто для каждой буквы взять ее порядковый номер в алфавите. 1 2 3 1 2. 
Все это вместе объединенное будет числом. Вот оно наше число, а что делать с числом – мы уже знаем.

Еще один способ: абсолютно для любого объекта легко придумать хеш-функцию. Наша память компьютерная, 
пока что на нашем уровне абстракции, представляет собой, по сути, один огромный, длинный список из байт. 
И вот в этом списке где-то, в каком-то месте вашей памяти, живет ваш объект абсолютно любой природы. 
И у него есть адрес, где он находится в памяти. Так давайте этот адрес и обозначим за число x. Вот так 
мы получили, по сути, целое число, индекс нашей глобальной памяти. Естественно, здесь возникает такая проблема, 
что если объект изменяемый, то у нас, в принципе, все может стать очень плохо. Объект изменится, а его хеш-функция 
останется той же самой. И мы не сможем, например, быстро сравнить два объекта или как-то поменять его значение в списке. 
Таким образом, что можно сказать? Все неизменяемые объекты в Python имеют хеш, заранее посчитанный. И когда мы хотим его, 
например, положить в множество или сравнить два объекта, то сначала сравниваются их хеши. И только в случае совпадения 
будут сравниваться все сложные объекты целиком. Изменяемые объекты хеша не имеют и поэтому в множество попасть не могут. 

Словарь – это сопоставление ключ-значения, например слово и его перевод, или телефон и имя абонента. У нас есть 
пара key, value – «ключ» и «значение». Например, ключом выступает номер телефона, а значением выступает имя абонента. 
Тогда мы считаем хеш-функцию только от ключа.

Соответственно, мы в этот список хеш посчитаем только от ключа, от телефона 1, а добавим сюда пару — ключ и значение. 

То есть в словаре хеш-функция считается только от ключа, а от значения наша хеш-функция никак не считается 
и это просто дополнительные данные, которые приделаны к ключу. '''


'''В языке Питон множества имеют тот же смысл, что и в математике: набор объектов без определенного порядка. 
В множество можно добавлять и удалять объекты, проверять принадлежность объекта множества и перебирать все объекты множества.

Также над множествами можно совершать групповые операции, например, пересекать и объединять два множества.

Проверка принадлежности элемента множеству, а также операции удаления и добавления элементов, осуществляются за O(1) 
(если бы мы хранили элементы в списке и хотели бы проверить принадлежность элемента списку, то нам потребовалось бы 
O(N) операций, где N - длина списка).

Такая скорость достигается использованием хеш-таблиц. Хеш-таблица - это массив достаточно большого размера (назовем 
этот размер K). Каждому неизменяемому объекту можно сопоставить по некоторому правилу число M от 0 до K и поместить 
этот объект в ячейку списка с индексом M. Например, для целых чисел таким правилом сопоставления может быть просто 
подсчет остатка от деления целого числа на K. Операцию взятия остатка будет нашей хеш-функцией.

Теперь если нам нужно проверить, принадлежит ли некоторое число множеству, мы просто считаем хеш-функцию от него 
и проверяем, лежит ли в ячейке с индексом, равным результату вычисления хеш-функции наш объект или нет. Для других 
типов данных можно применить такой подход: любой объект так или иначе является последовательностью байт. Будем 
интерпретировать эту последовательность байт как число и подсчитаем хеш-функцию для этого числа.

Естественно, может оказаться, что несколько объектов дают один и тот же хеш (отображение между огромным множеством 
различных объектов и скромным размером множества допустимых хешей не может быть биективным). Такие проблемы можно 
разрешить, не ухудшая асимптотическую сложность. Подробнее такие методы вы будете изучать на курсе алгоритмов.

Поскольку, например, числа, могут быть достаточно длинными, то операция подсчета хеш-функции при каждой операции 
с этим объектов в множестве может быть очень медленной. Поэтому каждый неизменяемый объект в Питоне имеет заранее 
насчитанный хеш, который подсчитывается один раз при его создании. Кстати, с помощью этих же хешей можно понимать, 
есть ли уже объект в памяти и не создавать новых объектов, а просто подвешивать еще одну ссылку на уже 
существующий объект.

Изменяемые типы, такие как список, не имеют заранее насчитанных хешей. Изменение всего одного элемента в списке 
привело бы к полному пересчету хеша для всего списка, что катастрофически замедлило бы работу со списками. 
Поэтому у изменяемых объектов нет хеша и они не могут быть добавлены в множество.

Само множество также является изменяемым объектом и не может быть, например, элементом другого множества.

Существуют также неизменяемые множества, которые создаются с помощью функции frozenset.'''



'''Создание множеств'''

fSet = {1, 2, 3}
aSet = {3, 1, 2}
print(fSet == aSet)

# Можно задать множество через функцию set()

myList = list(map(int, input().split()))
# В множество элементы входят по одному разу
mySet = set(myList)
print(mySet)

# 1. Печатается точно так же, как задается в тексте программы: фигурные скобки с элементами множества через запятую
# 2. Никаких повторов нет
# 3. Порядок не присутствует - числа идут вперемешку. /Возможно, что маленькие числа будут упорядочены, т.к.
# если берем остаток по модулю не очень большого числа, то все числа, меньше его, будут упорядочены. Но в целом
# рассчитывать на это нельзя./

myList = map(int, input().split())
mySet = set(myList)
print(mySet)

# Функцию set() можно брать от чего угодно итерируемого. /map, string, tuple, range и пр./
# map возвращает iterable

# Что можно класть и что нельзя класть?
# Можно класть не изменяемые объекты
# Причем класть их можно в абсолютно каких угодно сочетаниях.

mySet = {1, 3.14, 'abc', (1, 2)}
print(mySet)

# При этом изменяемые объекты класть нельзя, т.к. они не имеют хэша

# Множество при этом тоже является изменяемым объектом. Т.е. внутри множества не может быть другого множества.

# Но есть frozenset /frozen - замороженный/
mySet = {1, 3.14, 'abc', frozenset((1, 2))}
# frozenset - неизменяемое множество
# Поскольку он создается только один раз и не меняется, его хэш может быть подсчитан, а поэтому он может быть элементом
# множества

# Во frozenset точно так же не может быть изменяемых объектов. По той же причине - после изменения сета необходимо
# пересчитывать его хэш.

print(frozenset(mySet))

# Хотим вывести множество в нормальном виде
mySet = {1, 2, 3, 4, 1, 2, 4000000}
print(*mySet)

# Хотим вывести в отсортированном виде
print(*sorted(list(mySet)))

# Подсчет количества различных букв в строке
mySet = set('abcdeabc')
print(len(mySet))

# Таким образом, от чего угодно итерируемого можно вызвать функцию set(), и все повторяющиеся элементы исчезнут,
# останутся только уникальные.


'''Множество в теле программы может быть создано с помощью записи элементов через запятую в фигурных скобках:'''
mySet = {3, 1, 2}
print(mySet)
'''Вывод с помощью print осуществляется в том же формате. Порядок элементов в множестве может быть случайным, 
т.к. хеш функция не гарантирует, что если A>B, то h(A) > h(B).
Если при задании множества присутствовало несколько одинаковых элементов, то они попадут в множество в единственном экземпляре:'''
firstSet = {1, 2, 1, 3}
secondSet = {3, 2, 1}
print(firstSet == secondSet)
'''Эта программы выведет True (множества можно сравнивать на равенство).'''

'''Также множества можно создавать с помощью функции set, которая может принимать в качестве параметра что угодно итерируемое:'''
setFromList = set([1, 2, 3])
print(setFromList)
setFromTuple = set((4, 5, 6))
print(setFromTuple)
setFromStr = set("lol")
print(setFromStr)
setFromRange = set(range(2, 22, 3))
print(setFromRange)
setFromMap = set(map(abs, (1, 2, 3, -2, -4)))
print(setFromMap)
setFromSet = set({1, 2, 3})
print(setFromSet)

'''Множество также является итерируемым объектом (еще раз: объекты идут в "случайном" порядке, не по возрастанию!).

Множество может содержать в себе объекты разных типов:'''
mixedSet = {1, 3.14, (1, 2, 3), "i have no idea why i'm here"}
print(mixedSet)

'''По аналогии со строками, списками и кортежами, количество элементов в множестве можно узнать с помощью функции len.

Из множества можно сделать список или кортеж с помощью функций list и tuple соответственно. Применение функции str 
к множеству даст нам текстовое представление (элементы в фигурных скобках, разделенные запятыми).

Частой операцией является вывод упорядоченных элементов множества. Это можно сделать, применив функцию sorted 
сразу к множеству (ведь оно итерируемо):'''
mySet = {'abba', 'a', 'long string'}
print(', '.join(mySet))
'''К множеству можно применять функцию map.'''
print(', '.join(sorted(mySet)))


# Работа с множествами

# Хотим перебрать все объекты множества
mySet = {1, 2, 3, 40000}
for elem in mySet:
    print(elem)
# Порядок будет случайным

# Необходимо проверить, входит ли элементв множество или не входит
primes = {2, 3, 5, 7, 11, 13}
n = int(input())
if n in primes:  # in позволяет проверять принадлежность множеству
    print('In set')
else:
    print('Not in set')

# Проверяем отрицание
# if not n in primes:  # in позволяет проверять принадлежность множеству
if n not in primes:
    print('Not in set')
else:
    print('In set')


# Работа с элементами множества

# Добавление элемента в множество
primes.add(17)
print(*primes)

# Удаление элемента из множества
primes.remove(13) # Если элемента в множестве нет, то ломается!!!
primes.discard(13)
print(*primes)

# Т.е. если нужно проверять, есть ли элемент в множестве, - remove
# Если не нуэно проверять - discard

# Обычно подразумевается, что элемент в множестве был, поэтому лучше пользоваться remove,
# т.к. позволяет отловить программистские ошибки

# Замена элемента - через удаление старого и добавление нового


# Работа с целыми множествами

a = {1, 2, 3, 4}
b = {1, 3}  # b является подможеством a
print(a == b)
print(a != b)
print(a < b)
# Одно множество меньше другого, если все элементы множества входят во второе, причем во втором есть
# еще какие-то элементы кроме нашего подмножества, т.е. они не равны межлу собой
print(a > b)
# При этом если множества содержат различные элементы, то a < b и b < a одновременно

b = {1, 3, 10, 12}

# Объединение двух множеств - или
print(a | b)
# Пересечение множеств
print(a & b)
# Вычитание множества
print(a - b)
# Симметрическая разность: все элементы, входящие в объединение множеств, но не входящие в их пересечение
print(a ^ b)


'''Работа с элементами множеств

Чтобы создать пустое множество нужно написать:'''
emptySet = set()

'''Писать пустые фигурные скобки нельзя.

Добавление элемента в множество осуществляется с помощью метода add, если элемент уже был в множестве, то оно не изменится.

Перебрать элементы множества можно с помощью for (for умеет ходить по любым итерируемым объектам):'''
mySet = {1, '2', 2, '1'}
for elem in mySet:
    print(elem, end=' ')
'''Вывод такой программы будет ''1 1 2 2'', но упорядоченность является чистой случайностью.'''

'''Чтобы проверить, входит ли элемент X в множество A достаточно написать X in A. Результатом 
этой операции будет True или False. Чтобы проверить, что элемент не лежит в множестве можно писать 
not X in A, или, более по-человечески X not in A.'''
mySet = {1, 2, 3}
if 1 in mySet:
    print('1 in set')
else:
    print('1 not in set')
x = 42
if x not in mySet:
    print('x not in set')
else:
    print('x in set')

'''Чтобы удалить элемент из множества, можно воспользоваться одним из двух методов: discard или remove. 
Если удаляемого элемента в множестве не было, то discard не изменит состояния множества, а remove выпадет с ошибкой.'''


'''Групповые операции над множествами

В Питоне можно работать не только с отдельными элементами множеств, но и с множествами в целом. 
Например, для множеств определены следующие операции:

Операция	Описание
A | B	Объединение множеств
A & B	Пересечение множеств
A - B	Множество, элементы которого входят в A, но не входят в B
A ^ B	Элементы входят в A | B, но не входят в A & B

В результате этих операций создается новое множество, однако для них определена и 
сокращенная запись: |=, &=, -= и ^=. Такие операции изменяют множество, находящееся слева от знака операции.

Для множеств также определены операции сравнения:
Операция	Описание
A == B	Все элементы совпадают
A != B	Есть различные элементы
A <= B	Все элементы A входят в B
A < B	A <= B и A != B
Также определены операции > и >=. Все групповые операции и сравнения проводятся над множествами за время, 
пропорциональное количеству элементов в множествах.'''

