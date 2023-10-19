# Наибольшее произведение трех чисел

# В данном списке из n≤10⁵ целых чисел найдите три числа, произведение
# которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# Выведите три искомых числа в любом порядке.


def extremum(numList):
    extr = [0 for i in range(6)]
    for num in numList:
        if num != 0:
            if num <= extr[0]:
                extr[0], extr[1], extr[2] = num, extr[0], extr[1]
            elif extr[0] < num <= extr[1]:
                extr[1], extr[2] = num, extr[1]
            elif extr[1] < num <= extr[2]:
                extr[2] = num
            elif extr[5] <= num:
                extr[3], extr[4], extr[5] = extr[4], extr[5], num
            elif extr[4] <= num < extr[5]:
                extr[3], extr[4] = extr[4], num
            elif extr[3] <= num < extr[4]:
                extr[3] = num
    return extr

def findMaхMultipl(extreme):
    l = len(extreme)
    maxValue = extreme[0] * extreme[1] * extreme[2]
    val1, val2, val3 = extreme[0], extreme[1], extreme[2]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if i != j and i != k and j != k and extreme[i] * extreme[j] * extreme[k] > maxValue:
                    val1, val2, val3 = extreme[i], extreme[j], extreme[k]
    return val1, val2, val3


numList = list(map(int, input().split()))
extreme6 = extremum(numList)
print(extreme6)
n = 0
for num in numList:
    if num in extreme6:
        n += 1
print(n)
# val1, val2, val3 = findMaхMultipl(extreme6)
# if 0 in numList and val1 * val2 * val3 < 0
# print(findMaхMultipl(extreme))
