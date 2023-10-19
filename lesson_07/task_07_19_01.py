# Выборы Президента

# В выборах Президента Российской Федерации побеждает кандидат, набравший
# свыше половины числа голосов избирателей. Если такого кандидата нет, то во
# второй тур выборов выходят два кандидата, набравших наибольшее число голосов.

# Каждая строка входного файла содержит имя кандидата, за которого отдал голос
# один избиратель. Известно, что общее число кандидатов не превосходит 20, но
# в отличии от предыдущих задач список кандидатов явно не задан. Читайте
# данные из файла input.txt с указанием кодировки utf8.
#
# Если есть кандидат, набравший более 50% голосов, программа должна вывести
# его имя. Если такого кандидата нет, программа должна вывести имя кандидата,
# занявшего первое место, затем имя кандидата, занявшего второе место.
# Выводите данные в файл output.txt с указанием кодировки utf8.

candDict = dict()
candList = list()
voices = 0
with open("input_task_07_19.txt", "r", encoding='utf-8') as inFile:
    for line in inFile:
        cand = line.strip()
        candDict[cand] = candDict.get(cand, 0) + 1
        voices += 1
for cand in candDict:
    candList.append((cand, candDict[cand]))
candList.sort(key=lambda p: (-p[1], p[0]))
print(candList[0][0])
if candList[0][1] / voices <= 0.5:
    print(candList[2][0])
with open("output_task_07_19.txt", "w", encoding='utf-8') as outFile:
    outFile.write(candList[0][0] + '\n')
    if candList[0][1] / voices <= 0.5:
        outFile.write(candList[2][0])
