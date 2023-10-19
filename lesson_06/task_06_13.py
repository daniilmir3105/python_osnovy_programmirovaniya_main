# Количество победителей по классам

# В условиях предыдущей задачи определите количество школьников, ставших
# победителями в каждом классе. Победителями объявляются все, кто набрал
# наибольшее число баллов по данному классу. Гарантируется, что в каждом
# классе был хотя бы один участник.
#
# Выведите три числа: количество победителей олимпиады по 9 классу,
# по 10 классу, по 11 классу.


def est(list):
    return list[2], -list[3]


# scores = list()
# d = tuple(input().split())
# while d != ():
#     print(d)
#     scores.append((d[0], d[1], int(d[2]), int(d[3])))
#     d = tuple(input().split())
inFile = open('input_task_06_13.txt', 'r', encoding='utf-8')
# inFile = open('input.txt', 'r', encoding='utf-8')
scores = list()
for line in inFile:
    d = tuple(line.strip().split())
    scores.append((d[0], d[1], int(d[2]), int(d[3])))
inFile.close()
scores.sort(key=est)
# print(scores)
cl, count, maxScore = 0, 0, 0
outFile = open('output_task_06_13.txt', 'w', encoding='utf-8')
# outFile = open('output.txt', 'w', encoding='utf-8')
for sc in scores:
    if sc[2] != cl:
        if count != 0:
            print(count, end=' ')
            print(count, end=' ', file=outFile)
        cl = sc[2]
        maxScore = sc[3]
        count = 1
    elif maxScore == sc[3]:
        count += 1
print(count)
print(count, file=outFile)
