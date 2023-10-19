# Количество элементов, больше предыдущего

# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности
# больше предыдущего элемента.
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само
# число 0 в последовательность не входит, а служит как признак ее окончания).
#
# Выведите ответ на задачу.

n = int(input())
countElem = 0
k = n
while n != 0:
    if k < n:
        countElem += 1
    k = n
    n = int(input())
print(countElem)
