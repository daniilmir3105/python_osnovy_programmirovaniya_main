# Номер появления слова

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось
# в этом тексте ранее.


inFile = open("input_task_07_14.txt")
wordsDict = dict()
for line in inFile.readlines():
    wordsLine = line.split()
    for word in wordsLine:
        count = wordsDict.get(word, 0)
        print(count, end=' ')
        wordsDict[word] = count + 1
inFile.close()
