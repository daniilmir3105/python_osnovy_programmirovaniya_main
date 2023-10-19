# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.


numList = list(map(int, input().split()))
numList.append(0)
i = 0
flag = True
while i <= len(numList) - 1 and flag:
    if numList[i] == 0:
        flag = False
        for j in range(i, len(numList) - 1):
            if numList[j] > 0:
                flag = True
            numList[j] = numList[j+1]
        i -= 1
    i += 1
numList.pop()
print(" ".join(map(str, numList)))
