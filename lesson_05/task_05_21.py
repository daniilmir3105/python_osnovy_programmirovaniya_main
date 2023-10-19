# Наибольший элемент

'''Дан список чисел. Выведите значение наибольшего элемента в списке, а затем
индекс этого элемента в списке. Если наибольших элементов несколько, выведите
индекс первого из них.'''

numList = list(map(int, input().split()))
max = numList[0]
maxIndx = 0
for i in range(1, len(numList)):
    if numList[i] > max:
        max = numList[i]
        maxIndx = i
print(max, maxIndx)
