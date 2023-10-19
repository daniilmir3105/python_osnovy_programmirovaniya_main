# Упорядочить список партий по числу голосов

# Формат входных данных аналогичен предыдущей задаче. Выведите список всех
# партий, участвовавших в выборах, отсортировав его в порядке убывания
# количества голосов избирателей, а при равном количестве голосов - в
# лексикографическом порядке.


def srt(List):
    return -List[1], List[0]


inFile = open('input_task_06_19.txt', 'r', encoding='utf-8')
parties, votes = list(), list()
for line in inFile:
    if line.strip() == "PARTIES:":
        f = False
    elif line.strip() == "VOTES:":
        f = True
    elif not f:
        parties.append(line.strip())
    elif f:
        votes.append(line.strip())
# print(parties)
# print(votes)
p_v = [(parties[i], 0) for i in range(len(parties))]
for i in range(len(parties)):
    p_v[i] = (parties[i], votes.count(parties[i]))
# print(p_v)
p_v.sort(key=srt)
# print(p_v)
outFile = open('output_task_06_19.txt', 'w', encoding='utf-8')
for pv in p_v:
    print(pv[0])
    outFile.write(pv[0] + '\n')
outFile.close()
