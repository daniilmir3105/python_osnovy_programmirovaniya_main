# Проходной балл

# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов
# в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При
# этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку)
# по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют
# в конкурсе по сумме баллов за три экзамена.
#
# В конкурсе участвует N человек, при этом количество мест равно K. Определите
# проходной балл, то есть такое количество баллов, что количество участников,
# набравших столько или больше баллов не превосходит K, а при добавлении к ним
# абитуриентов, набравших наибольшее количество баллов среди непринятых
# абитуриентов, общее число принятых абитуриентов станет больше K.

# Программа получает на вход количество мест K. Далее идут строки с
# информацией об абитуриентах, каждая из которых состоит из имени (текстовая
# строка содержащая произвольное число пробелов) и трех чисел от 0 до 100,
# разделенных пробелами.
#
# Используйте для ввода файл input.txt с указанием кодировки utf8.

# Программа должна вывести проходной балл в конкурсе. Выведенное значение
# должно быть минимальным баллом, который набрал абитуриент, прошедший по
# конкурсу.
#
# Также возможны две ситуации, когда проходной балл не определен.
#
# Если будут зачислены все абитуриенты, не имеющие неудовлетворительных
# оценок, программа должна вывести число 0.
#
# Если количество абитуриентов, имеющих равный максимальный балл больше чем K,
# программа должна вывести число 1.
#
# Используйте для вывода файл output.txt с указанием кодировки utf8.


inFile = open('input_task_06_14.txt', 'r', encoding='utf-8')
K = int(inFile.readline().strip())
data, est = list(), list()
for line in inFile:
    d = tuple(line.strip().split())
    # print(d)
    if int(d[-3]) >= 40 and int(d[-2]) >= 40 and int(d[-1]) >= 40:
        # data.append((d[:-3], int(d[-3]), int(d[-2]), int(d[-1]),
        # (int(d[-3]) + int(d[-2]) + int(d[-1]))))
        est.append(int(d[-3]) + int(d[-2]) + int(d[-1]))
inFile.close()
# data.sort(key=lambda tpl: -tpl[-1])
# print(data)
# est.sort(key=lambda p: -p)
est.sort(reverse=True)
# print(est)
count = len(est)
if count <= K:  # Нормально сдало экзамен не больше человек, чем имеется мест
    res = 0
elif K == 0:  # Количество мест равно нулю
    res = 1
elif est[K] == est[0]:  # K + 1 челове сдали на максимум
    res = 1
elif est[K] < est[K-1]:  # Следующий имеет меньший балл, все Ok
    res = est[K-1]
elif est[K] == est[K-1]:  # Следующий имеет такой же балл, нужно ограничивать
    i = 1
    while est[K] == est[K-i]:
        i += 1
    res = est[K-i]
# else:
#     print("Внимание! Пропустили!")
outFile = open('output_task_06_14.txt', 'w', encoding='utf-8')
outFile.write(str(res))
outFile.close()
# print(str(res))
