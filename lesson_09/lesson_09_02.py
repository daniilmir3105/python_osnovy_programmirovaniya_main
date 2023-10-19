# Инкапсуляция и конструкторы

class Complex:  # Название классов с большой буквы, коннкретные объекты с маленькой буквы

    # Если здесь создаем какие-то переменные и кладеем туда значения, то они доступны из всех объектов класса
    # Например, если re = 1, то абсолютно во всех экземплярах классов re= 1
    # Такие переменные называются статическими. То есть они статически определены и разделяются между всеми
    # объектами класса. Если мы их где-то поменяем, то они поменяются во всех объектах.


    # В классе должен быть метод.
    # Метод - это, по сути, функции внутри класса
    def __init__(self, re=0, im=0):
    # Это конструктор класса — то есть то, что будет вызываться, когда мы создаем новый объект нашего класса.
        self.re = re
        self.im = im

# Итак, теперь мы хотим создать комплексное число.
a = Complex()
b = Complex(1)
c = Complex(2, 3)


print(b.re, b.im)
print(c.re, c.im)


# В классе обязательно должен быть метод.
# Метод — это, по сути, функция, описанная внутри класса. И методом мы часто пользовались.
# Например, мы писали какую-нибудь строку, название конкретной строковой переменной, точка и название метода.
# Этот метод применялся к нашей строке. Зачем так сделано? Чтобы и код, и данные хранились в одном месте,
# и обрабатывать их было удобнее и описывать их тоже было удобнее.

# __init__ - это конструктор класса — то есть то, что будет вызываться, когда мы создаем новый объект нашего класса.
# Что нам нужно для конструктора? Во-первых, абсолютно любой метод класса принимает первый параметр self.
# self — в некотором смысле «свой», «я» — это именно тот объект класса, с которым вы сейчас работаете.
# Кроме этого, могут быть и другие методы.

# Если же что-то передано, то мы должны записать это в соответствующие поля класса. Делается это так: self, точка, re.
# Как в структуре. Поэтому просто раскладываем это как поля структуры.

# Статические переменные обычно применяются для сохранения каких-то констант.
# Например, вы пишете математическую библиотеку какую-то или физическую, и там есть константы — вы можете их сохранить
# как статические переменные. Или для внутренней организации, для подсчета какой-то статистики. Например, вы хотите знать,
# сколько комплексных чисел использовалось в вашей программе. Тогда вы можете сделать статический счетчик,
# который будет изменяться в конструкторе. Каждый раз, когда создаете объект, просто увеличивайте счетчик на единичку.

# Мы описали класс. Класс представляет собой набор каких-то полей, данных, которые хранятся, и набор методов,
# то есть как с этими данными работать. Методы предоставляют пользователю интерфейс, через который он может
# взаимодействовать с классом.

# Конечно, мы могли бы не пользоваться, например, конструктором и описать какие-то конструкции в стиле...
# Не писать вообще, не создавать этот метод init, а писать, что c равно пустой Complex. Если бы не было у нас init,
# то создался бы совсем пустой класс, в котором не было бы полей. И потом в нем руками раскладывать, как мы это делали
# в структуре, какие-то значения такие же. В общем-то, это было бы абсолютно то же самое, что у нас написано сейчас.



'''Мы уже использовали ключевое слово class для создания структур - набора именованных полей, совокупность которых 
описывает объект. Однако, мы пользовались для их обработки отдельно лежащими функциями или кусками кода.

Было бы намного удобнее, если бы описание структуры объекта и методов работы с ним лежало рядом, для удобства изучения, 
модификации и использования.

Мы будем рассматривать элементы ООП на примере комплексных (ударение на "е") чисел. Это математический объект, 
который состоит из действительной (real) и мнимой (imaginary) части. Запись это числа выглядит как re + im * i, 
где i это квадратный корень из -1$. Глубокое математическое понимание комплексных чисел нам не понадобится: 
достаточно понимать, что это структура с двумя полями re и im, где оба эти поля - вещественные числа.

Для создания новых объектов класса используется специальный метод, который называется "конструктор". 
Методы класса записываются внутри описания класса как функции, конструктор должен называться __init__. 
В качестве первого параметра они должны принимать переменную self - конкретный объект класса, с которым они работают.'''

'''Рассмотрим класс для вещественного числа, вызов конструктора и печать полей объекта:'''


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

a = Complex(1, 2)
b = Complex(3)
c = Complex()
print(a.re, a.im)
print(b.re, b.im)
print(c.re, c.im)


'''Здесь конструктор содержит три параметра: 
self - пустой объект класса Complex, 
re и im, по умолчанию равные нулю. 
Вызов конструктора осуществляется с помощью написания названия класса, 
в скобках указываются параметры конструктора (все, кроме self). 
Названия классов принято записывать с большой буквы, а объекты - с маленькой.
Вывод этой программы будет:
1 2
3 0
0 0'''


'''Обратите внимание, что мы меняем переменные конкретного объекта класса, который передан в качестве параметра self. 
Если мы создали какие-то переменные в описании класса, то их значения были бы доступны во всех объектах этого класса 
и их можно было бы даже изменить, перечислив их имена в начале метода после выражения nonlocal. Такие переменные 
называются статическими, обычно они предназначены для хранения каких-то констант (что очень удобно если вы, 
например, описываете какой-то класс для физических вычислений). Их изменение может понадобится в экзотических ситуациях, 
например, при подсчете количества объектов класса. Мы не будем заострять на них внимание.'''
