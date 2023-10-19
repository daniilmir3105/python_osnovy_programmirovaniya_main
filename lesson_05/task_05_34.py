# Наибольшее произведение двух

# Дан список, заполненный произвольными целыми числами. Найдите в этом списке
# два числа, произведение которых максимально. Выведите эти числа в порядке
# неубывания.
#
# Решение должно иметь сложность O(n), где n - размер списка.

numList = list(map(int, input().split()))
# negative number - отрицательное число, positive number - положительное число
# negMin1, negMin2, posMax1, posMax2 = 0, 0, 0, 0
min1, min2, max1, max2 = 0, 0, 0, 0
for num in numList:
    if num <= min1:
        min1, min2 = num, min1
    elif min1 <= num <= min2:
        min2 = num
    elif num >= max2:
        max1, max2 = max2, num
    elif max1 <= num <= max2:
        max1 = num
if min1 * min2 <= max1 * max2:
    print(max1, max2)
else:
    print(min1, min2)
