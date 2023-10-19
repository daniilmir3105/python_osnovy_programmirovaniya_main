# Максимальный балл не-победителя

# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся
# школьники, которые набрали наибольший балл среди всех участников в данном
# классе.
#
# Для каждого класса определите максимальный балл, который набрал школьник,
# не ставший победителем в данном классе.
#
# Выведите три целых числа.


inFile = open('input_task_06_16.txt', 'r', encoding='utf-8')
scores = list()
for line in inFile:
    d = tuple(line.strip().split())
    scores.append((int(d[-2]), int(d[-1])))
inFile.close()
scores.sort(key=lambda l: (l[0], -l[1]))
# print(scores)
cl, max, res = 8, 0, ''
for score in scores:
    if score[0] > cl:
        max = score[1]
        cl = score[0]
        flag = True
    elif flag and score[1] < max:
        print(score[1], end=' ')
        res += str(score[1]) + ' '
        flag = False
with open('output_task_06_16.txt', 'w', encoding='utf-8') as outFile:
    outFile.write(res)
