# Четные элементы

'''Выведите все четные элементы списка.

Вводится список чисел. Все числа списка находятся на одной строке.
Выведите ответ на задачу.'''

numList = list(map(int, input().split()))
print(*[numList[i] for i in range(len(numList)) if numList[i] % 2 == 0])
