# Количество положительных

# Найдите количество положительных элементов в данном списке.

numList = list(map(int, input().split()))
print(len([numList[i] for i in range(len(numList)) if numList[i] > 0]))
