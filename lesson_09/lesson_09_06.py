# Наследование и полиморфизм

# Одна из прелестей объектно-ориентированного программирования состоит в наследовании. То есть если вы уже
# что-то определили и хотите теперь немножко более уточненный объект какой-то создать, то это очень легко сделать.

# Если вы определили, что такое мячик, то какими он свойствами обладает, что он шарообразный и прыгает,
# если по нему стукнуть его об пол, то вам уже описывать баскетбольные мячи, футбольные, волейбольные и так далее
# гораздо проще. Какие-то базовые свойства описаны, вы описываете только особенности, отличия или дополнительную
# какую-то функциональность.

# С нашим классом комплексных чисел тоже такая история может произойти. Как я рисовал на доске, у нас комплексное
# число очень похоже на точку на плоскости. Давайте введем класс «точка», будем иметь в виду, что она на плоскости,
# которая пронаследует все методы, которые определены для комплексных чисел, и добавит что-нибудь свое.

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


# Мы создаем новый класс, называем его, новое имя даем — point, и в скобках, как мы это делали для исключений,
# указываем, от кого он наследуется. В нашем случае не от стандартного какого-то base exception, а от нашего класса
# «комплексное число.
# Теперь наш point, наша точка умеет абсолютно все то же самое, что умело комплексное число,
class Point(Complex):
    # Хотим определить метод, считающий длину вектора от начала координат, от 00, до нашей точки.
    def length(self):
        return (self.re ** 2 + self.im ** 2)**0.5

    def __str__(self):  # Здесь у нас даже подсказка появилась, что это переопределенный метод
        return str((self.re, self.im))


p1 = Point(1, 2) # Конструктор не описан в классе point, поэтому вызовется конструктор для предка
print(p1.length())

p2 = Complex(1, 2)
# print(p1.length())  # Ошибка, ибо для комплексного числа метод длины не определен

p3 = p1 + p2 # Вызывается метод сложения для более глобального класса, возвращающий соответствующий класс
# print(p3.length()) # Вернулось комплексное число, длины у него нет

print(p3)

print(p1) # Напечаталось как для комплаексного числа, но для точки мы хотим делать это по другому

# Поэтому мы можем взять и переопределить метод вывода. Как печатаются точки обычно? Давайте печатать ее в круглых скобках,
# как кортеж по сути, то есть сначала x координата, потом y координата.
#
# Переопределение методов — это и есть в некотором смысле то, что называется полиморфизм, изменчивость объекта.
# У нас у родительского класса есть метод превращения объекта в строку. У нас произошел полиморфизм, и теперь
# у наследника этого класса метод переопределен.
# def __str__(self) в классе point():



'''Операции сложения и умножения на вещественное или целое число для комплексных чисел очень похожи на поведение 
свободных векторов на плоскости. Они соответствуют сложению векторов или умножение вектора на число, где действительная часть 
комплексного числа является x-координатой вектора, а мнимая - y-координатой.

Кроме того, свободный вектор обладает некоторыми операциями, которые характерны только для него, но не для вещественного числа. 
Например, это может быть метод length, вычисляющий длину вектора. Нам не хотелось бы засорять код для описания комплексного числа 
методами для работы со свободным вектором, но с другой стороны не хотелось бы заново переписывать методы сложения и умножения 
для свободных векторов.

В такой ситуации разумно создать новый класс для описания свободного вектора (или точки на плоскости, что то же самое), 
который унаследовал бы все методы комплексных чисел и добавил бы новый метод length.

Мы уже знаем, что для того, чтобы пронаследовать класс от другого достаточно в описании класса указать в круглых скобках, от кого 
он наследуется. Таким образом, мы можем записать наше описание класса Point с определенным методом length так:'''
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

class Point(Complex):
    def length(self):
        return (self.re**2 + self.im**2)**(1/2)

a = Point(3, 4)
b = Complex(1, 2)
print(a.length())
c = a + b
print(c)

'''Вывод этой программы будет:
5.0
4+6i

Здесь мы не только убедились в том, что свежесозданный метод работает, но и сделали довольно странную вещь: 
сложили точку на плоскости с комплексным числом. Дело в том, что объекта класса Point также одновременно является 
и объектом типа Complex, т.к. Point пронаследован от Complex. Point лишь расширяет и дополняет Complex, а значит Point 
может смело быть интерпретирован как Complex, но не наоброт.
В этом примере будут истинны выражения isinstance(a, Point) и isinstance(a, Complex), но будет ложно выражение 
isinstance(b, Point).'''



'''Переопределение методов

Если мы попытаемся напечатать объект типа Point, то он напечатается как комплексное число. Нам хотелось бы, 
чтобы точки на плоскости печатались в виде (x, y), а не x+yi.

В языке Питон любой метод можно переопределить в наследнике, что мы и сделаем для метода __str__ для класса Point:'''

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

class Point(Complex):
    def length(self):
        return (self.re**2 + self.im**2)**(1/2)
    def __str__(self):
        return str((self.re, self.im))

a = Point(3, 4)
print(a)

'''Наш метод обязан возвращать строку, но мы можем воспользоваться функцией str от кортежа, которая выдаст нам нужный результат.'''



'''Проектирование структуры классов

Структура описания классов представляет собой дерево (на самом деле в Питоне - ациклический граф), 
пронаследованный от единого корня - базового пустого класса.

С помощью грамотно спроектированной структуры классов можно добиться легкой читаемости и максимального 
повторного использования кода, обеспечения единого интерфейса и множество других радостей.

Однако, внесение фичи или изменение на высоком уровне иерархии классов может привести к необходимости выполнить 
огромное количество работы по модификации всех потомков этого класса, а также к полной несовместимости 
с предыдущей версией. Многочисленные изменения такого рода приводят к уродливым конструкциям, которые невозможно понимать 
и отлаживать.

В то же время, закладывание перспективных фичей в структуру классов ведет к переусложнению и сводит на нет 
все повторное использование кода за счет громоздкости конструкций. Кроме того, перспективные фичи могут быть 
недостаточно обдуманы и приведут к еще большему уродству, когда дело дойдет до их реальной реализации (если дойдет).

Таким образом, грамотное проектирование системы классов требует не только хорошего знания паттернов проектирования, 
но и большого практического опыта. На начальном этапе стоит обучаться проектированию систем, в которые не планируется 
внесение изменений.'''