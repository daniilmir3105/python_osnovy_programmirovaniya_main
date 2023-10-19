# Переставить соседние

# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

numList = list(map(int, input().split()))
end = (len(numList) // 2) * 2
if end != len(numList):
    end -= 1
for i in range(0, end, 2):
    numList[i], numList[i+1] = numList[i+1], numList[i]
print(' '.join(map(str, numList)))
