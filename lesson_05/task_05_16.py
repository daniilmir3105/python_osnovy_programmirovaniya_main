# Последний максимум

'''Найдите наибольшее значение в списке и индекс последнего элемента,
который имеет данное значение за один проход по списку, не модифицируя
этот список и не используя дополнительного списка.'''

numList = list(map(int, input().split()))
max = numList[0]
maxIndx = 0
for i in range(1, len(numList)):
    if numList[i] >= max:
        max = numList[i]
        maxIndx = i
print(max, maxIndx)
