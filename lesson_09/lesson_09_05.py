# Обработка ошибок


# Итак, нам нужно сообщать пользователю какую-то более подробную информацию о том, что он сделал не так,
# чтобы он мог у себя взять и исправить эту ошибку.


# Например, вместо числа в умножении ввели строку.


# Что такое исключение? Это какая-то ошибочная ситуация, которая вообще в принципе может быть обработана,
# то есть она не должна сразу взять и завалить вашу программу, но не на том уровне логики, на котором вы находитесь.

# То есть на более внешнем каком-то уровне, может быть, на интерфейсе пользователя. Вы поняли, что у вас где-то
# в глубине вашей программы произошла ошибка, но она возникла в результате того, что пользователь ввел что-то не то.
# Ну, ломаться не нужно, нужно просто попросить пользователя ввести заново, например.


# Для ошибок у нас используется класс. То есть что происходит, когда мы выбрасываем исключения?
# У нас прерывается работа всех запущенных функций, которые расположены в стеке, до тех пор,
# пока мы не наткнемся на обработчика ошибок. А этот обработчик ошибок поймает, собственно,
# объект класса ошибочного.


# Ошибка будет возникать при умножении комплексного числа на что-то плохое, на что мы не умеем умножать
# комплексное число. Так давайте сообщим ему и комплексное число, с которым возникла эта проблема,
# ну потому что у пользователя их может быть много, по значению он быстрее его найдет, и, собственно,
# на что он пытался умножить — так он тоже быстрее поймет, откуда у него это взялось, может быть, увидит
# что-то знакомое, поймет, что опечатался и умножил случайно не ту переменную, перепутал название. То есть
# в общем-то нам нужно два параметра: первое для комплексного числа, второе на что оно умножалось.

# Куда мы это будем складывать? Давайте просто в структуре создадим поля. Ну давайте назову их first и second
# с таким намеком на универсальный обработчик чего угодно. Давайте я лучше назову это класс ComplexError,
# чтобы уж совсем все было понятно, к чему он относится.


class ComplexError(BaseException):
    def __init__(self, complex, other): # Конструктор ошибочноого класса
        self.first = complex
        self.second = other


# Теперь нам нужно в какой-то момент сконструировать объект класса Error, ошибку, записать в него нужную информацию,
# при каких условиях эта ошибка возникла, и вызвать исключение, которое как раз будет распутывать наш стек, пока мы
# не натолкнемся на обработчик.

# Где это нужно сделать? В нашей функции умножения у нас описан if и elif. Для комплексных чисел, для целых вещественных.
# Во всех остальных случаях мы не знаем, что делать.


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep

    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)

    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.re * other.im
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        else:
            error = ComplexError(self, other) # Создаем объект ошибки, конструируем его. С какими параметрами?
            # Параметры мы договорились, что у нас будет комплексное число, а затем, на что оно пыталось умножиться.
            # То есть, по сути, сейчас это self комплексное число, и other, на что мы пытались умножить.
            raise error # Исключения мы бросаем комендой raise - "вызвать исключение"
            # Собственно, указывается, какой класс мы хотим отправить в обработчик. Вот этот самый класс с описанием ошибки.
            # После этого работа метода прерывается, ну и если он был вызван из каких-то функций и так далее, и так далее,
            # оно выходит, выходит, выходит до момента обработчика.
        return Complex(newRe, newIm)

    __rmul__ = __mul__


a = Complex(1, 2)
b = Complex(3, -4.5)


# Обработчик
try: # Попробуй
    print('abc' * b) # блок действий, которые надо попробовать сделать
# except: # Except — это если не получилось.
#     print("Error!") # что делать, если у нас в процессе выполнения команд в try возникла какая-то ошибка,
# какое-то исключение было брошено
except ComplexError as ce:
    print('Multiplication error, first param:', ce.first, ', second param: ', ce.second)


# У except кроме вот такой примитивной формы, что какая-то ошибка возникла, и тогда делай что-то,
# есть более совершенные формы. А именно, можно указать класс ошибок, которые мы будем ловить этим except'ом.

# В принципе, у вас может быть несколько except'ов. То есть если у вас может возникать несколько разных типов ошибок,
# выбрасываться несколько разных исключений, то вы можете на каждое последовательно написать свой except, и будет
# вызываться именно тот, какой класс вы выбросите.

# У нас возникла ошибка TypeError: catching classes that do not inherit from BaseException is not allowed
# Ловить классы, которые не являются наследниками base exception, нельзя.


# Таким образом вы можете обрабатывать разные исключительные ситуации. Это не совсем ошибка. То есть если ваша программа
# может не сломаться, если есть шанс, что на каком-то более верхнем слое логики во взаимодействии с пользователем,
# например, вы можете эту ошибку как-то исправить, или, например, попытаться еще раз умножить, вдруг со второй попытки
# получится, так бывает, например, при доступе к файлам или каким-то ресурсам, которые заняты были, а через некоторое время
# попробовали, они уже свободны. В таких ситуациях имеет смысл бросать исключения.

# Конечно, исключение бросается очень долго, это тяжелая операция распутывания стека, но в некоторых ситуациях
# это имеет смысл, чтобы ваша программа просто не обвалилась молча, не перестала работать. Ну и диагностику, конечно,
# нужно делать как можно более подробную, чтобы сразу человек взглянул, одним взглядом посмотрел и понял, где у него ошибка,
# и исправил ее.



'''Время от времени в программах возникают ошибочные ситуации, которые не могут быть обработаны в том месте, 
где возникла ошибка, а должны быть обработаны тем или иным образом в более внешней части программы.

Например, если на этапе выполнения промежуточной логики обнаружилось, что вы пытаетесь записать строку в то, 
что должно быть числом, то вы ничего не можете с этим сделать. В таком случае нужно вываливаться из стека вызовов функций или 
методов промежуточной логики до тех пор, пока мы не дойдем до фронтенда, который сообщит пользователю о том, 
что он ввел недопустимое значение и попросит, например, ввести его заново.

Наверняка вы сталкивались с ситуацией заполнения огромной формы, попытка отправить которую приводила к тому, 
что появлялось окошко со словом "ошибка" без каких-либо уточнений. Это плохой стиль, сообщение об ошибке должно быть информативным, 
чтобы позволить быстро её найти и исправить. Таким образом, при создании ошибки нужно передавать исчерпывающую инфорамацию о ней.

В нашем примере с вещественными числами мы можем рассмотреть такой пример ошибки: умножение комплексного числа на что-то, 
отличное от целого, вещественного или комплексного числа. Когда мы дошли до этапа умножения - мы уже ничего не можем 
предпринять для исправления этой ошибки, кроме как просигнализировать о ней в то место, откуда была вызвана наша операция умножения.

При этом на этапе вызова операции умножения мы уже можем предпринять какие-то действия. Например, сообщить пользователю о том, 
какую фигню он ввел и попросить ввести все-таки комплексное число. Или, если мы обрабатываем последовательность, 
из которой нужно вычленить и перемножить комплексные числа - просто перейти к следующему элементу последовательности. 
На этапе когда мы дошли до неудачного выполнения операция умножения мы не знаем и не можем знать как должна себя вести 
конкретная программа при возникновении такой ошибки.

Когда мы дойдем до ошибочной операции мы можем сконструировать специальный класс, содержащий подробное описание ошибки 
и выбросить его в то место, которое способно его обработать.

Выбрасывается ошибка с помощью команды raise, а ловится блоком try-except. Для случая умножения комплексного числа на мусор 
мы можем сконструировать класс ошибки, содержащий в себе ссылку как на комплексное число, так и на второй аргумент 
метода умножения.

Класс для ошибки должен быть наследником стандартного класса BaseError. Пока для нас это значит только то, что при создании 
описания класса ошибки мы должны написать в скобках после его названия BaseError. Потенциально ошибочные действия должны 
выполняться в блоке try, а команды для обработки ошибки должны быть в блоке except. Пример с обработкой ошибки будет выглядеть так:'''

class ComplexError(BaseException):
    def __init__(self, Complex, other):
        self.arg1 = Complex
        self.arg2 = other

class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep
    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)
    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.re * other.im
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        else:
            raise ComplexError(self, other)
        return Complex(newRe, newIm)
    __rmul__ = __mul__

a = Complex(1, 2)
try:
    res = a * 'abcd'
except ComplexError as ce:
    print('Error in mul with args:', ce.arg1, ce.arg2)

# Вывод этой программы будет: Error in mul with args: 1+2i abcd

'''По нему легко понять, что ошибка возникает при операции умножения и увидеть, что было передано в неё 
в качестве аргументов.

После команды except мы можем указать имя класса ошибки, который он должен обрабатывать, затем написать ''as'' 
и указать имя переменной, в которую попадет объект с описанием конкретной ошибки.

Блоков except может быть несколько для обработки ошибок разных типов. Првоерки выполняются последовательно, 
будет выполнен тот блок команд, у которого имя класса совпадает с именем класса ошибки или является его предком 
в дереве иерархии наследования.'''


'''Статический метод
Статические методы в Python являются синтаксическими аналогами статических функций в основных языках программирования. 
Они не получают ни экземпляр (self), ни класс (cls) первым параметром. Для создания статического метода (только «новые» 
классы могут иметь статические методы) используется декоратор staticmethod
>>> class D(object):  
       @staticmethod
       def test(x):
           return x == 0
...
>>> D.test(1)    # доступ к статическому методу можно получать и через класс
False
>>> f = D()
>>> f.test(0)    # и через экземпляр класса
True
Статические методы реализованы с помощью свойств (property).
https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_Python#.D0.A1.D1.82.D0.B0.D1.82.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.B8.D0.B9_.D0.BC.D0.B5.D1.82.D0.BE.D0.B4
'''