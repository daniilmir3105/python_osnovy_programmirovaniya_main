# Переставить min и max

# В списке все элементы различны. Поменяйте местами минимальный и максимальный
# элементы этого списка.


numList = list(map(int, input().split()))
# minim = min(numList)
# maxim = max(numList)
# minInd = numList.index(minim)
# maxInd = numList.index(maxim)
min, minInd, max, maxInd = numList[0], 0, numList[0], 0
for i in range(1, len(numList)):
    if numList[i] < min:
        min = numList[i]
        minInd = i
    elif numList[i] > max:
        max = numList[i]
        maxInd = i
numList[minInd], numList[maxInd] = numList[maxInd], numList[minInd]
print(" ".join(map(str, numList)))
