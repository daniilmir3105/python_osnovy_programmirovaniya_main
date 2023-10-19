# Количество различных элементов

# Дан список, упорядоченный по неубыванию элементов в нем. Определите,
# сколько в нем различных элементов.

numList = list(map(int, input().split()))
count = 1
current = numList[0]
for num in numList:
    if current != num:
        count += 1
        current = num
print(count)
