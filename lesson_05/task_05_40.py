# Сжатие списка

# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые
# элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список
# использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.


numList = list(map(int, input().split()))
length = len(numList)
i = 0
while i <= len(numList) - 1:
    if numList[i] == 0:
        del numList[i]
        # numList.pop(i)
        i -= 1
    i += 1
for i in range(len(numList), length):
    numList.append(0)
print(" ".join(map(str, numList)))
