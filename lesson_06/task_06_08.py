# Отсортировать список участников по алфавиту

# Известно, что фамилии всех участников — различны. Сохраните
# в массивах список всех участников и выведите его, отсортировав по фамилии
# в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием
# кодировки utf8.
# Например, для чтения откройте файл с помощью
# open('input.txt', 'r', encoding='utf8')


inFile = open('input_task_06_08.txt', 'r', encoding='utf8')
participantList = list()
i = 0
for line in inFile:
    lineData = line.strip().split()
    participantList.append(['', '', 0])
    participantList[i][0] = lineData[0]
    participantList[i][1] = lineData[1]
    participantList[i][2] = lineData[3]
    i += 1
inFile.close()
participantList.sort()
outFile = open('output_task_06_08.txt', 'w', encoding='utf8')
for part in participantList:
    print(' '.join(map(str, part)), file=outFile)
# outFile.write(' '.join([...) for i in range(3)]))
outFile.close()
