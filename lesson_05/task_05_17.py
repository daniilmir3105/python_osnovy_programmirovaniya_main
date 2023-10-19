# Больше предыдущего

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.

numList = list(map(int, input().split()))
print(*[numList[i] for i in range(1, len(numList))
        if numList[i] > numList[i - 1]])
