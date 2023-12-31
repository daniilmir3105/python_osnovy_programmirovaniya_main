# Исключающее ИЛИ

# Напишите функцию xor(x, y), реализующую функцию "Исключающее ИЛИ"
# двух логических переменных x и y.
#
# Функция xor должна возвращать True, если ровно один из ее аргументов
# x или y, но не оба одновременно равны True.

# Вводится 2 числа - x и y (x и y равны 0 или 1, 0 соответствует значению
# False, 1 соответствует значению True).
# Необходимо вывести 0 или 1 - значение функции от x и y.


def xor(x, y):
    return x * (1 - y) + (1 - x) * y


x = int(input())
y = int(input())

xorxy = xor(x, y)
print(xorxy * True + (1 - xorxy) * False)
