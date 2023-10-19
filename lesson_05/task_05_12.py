# Замечательные числа - 4

# Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа
# на отрезке от A до B, запись которых является палиндромом.


def palindrom4(x):
    return str(x)[:2] == str(x)[:-3:-1]

A = int(input())
B = int(input())

for i in range(A, B + 1):
    if palindrom4(i):
        print(i)
