# Соседи одного знака

'''Дан список чисел. Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов одного знака нет - не выводите
ничего. Если таких пар соседей несколько - выведите первую пару.'''

numList = list(map(int, input().split()))
flag = False
for i in range(1, len(numList)):
    if not(flag) and numList[i] * numList[i-1] >= 0:
        print(numList[i-1], numList[i])
        flag = True
