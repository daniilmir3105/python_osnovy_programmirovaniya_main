# Сортировка подсчетом

# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
# от 0 до 100.
#
# Отсортируйте этот список в порядке неубывания элементов. Выведите
# полученный список.
#
# Решение оформите в виде функции CountSort(A), которая модифицирует
# передаваемый ей список.
# Использовать встроенные функции сортировки нельзя.


def CountSort(A):
    numCount = [0 for i in range(101)]
    numSort = list()
    for num in numList:
        numCount[num] += 1
    # return numCount
    for i in range(len(numCount)):
        # print((str(i) + ' ') * numCount[i])
        for count in range(numCount[i]):
            numSort.append(i)
    return numSort


numList = list(map(int, input().split()))
result = CountSort(numList)
print(' '.join(map(str, result)))
