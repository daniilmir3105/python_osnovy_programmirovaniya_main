# Больше своих соседей

# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.

numList = list(map(int, input().split()))
print(len([numList[i] for i in range(1, len(numList) - 1)
           if numList[i - 1] < numList[i] and numList[i] > numList[i + 1]]))
