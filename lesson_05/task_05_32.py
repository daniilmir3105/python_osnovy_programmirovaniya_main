# Циклический сдвиг вправо

# Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1],
# A[1] на место A[2], ..., последний элемент переходит на место A[0]).
# Используйте минимально возможное количество операций присваивания.

numList = list(map(int, input().split()))
numList.append(0)
# numList = [numList[i-1] for i in range(len(numList)-1, 0, -1)] Разворачивает
for i in range(len(numList) - 1, 0, -1):
    numList[i] = numList[i - 1]
numList[0] = numList[len(numList) - 1]
numList.pop()
print(*numList)
