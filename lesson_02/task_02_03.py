# Максимум трех чисел
#
# Даны три целых числа. Найдите наибольшее из них
# (программа должна вывести ровно одно целое число).
#
# Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

A = int(input())
B = int(input())
С = int(input())

if A > B:
    if A > С:
        print(A)
    else:
        print(С)
else:
    if B > С:
        print(B)
    else:
        print(С)
