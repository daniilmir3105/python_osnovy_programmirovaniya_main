# Частотный анализ

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
# строку. Слова должны быть отсортированы по убыванию их количества появления
# в тексте, а при одинаковой частоте появления — в лексикографическом порядке.

# Указание.
# После того, как вы создадите словарь всех слов, вам захочется отсортировать
# его по частоте встречаемости слова. Желаемого можно добиться, если создать
# список, элементами которого будут кортежи из двух элементов: частота
# встречаемости словаи само слово. Например,
# [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом
# кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче.


txt = ""
wordDict = dict()
wordList = list()
with open("input_task_07_18.txt") as inFile:
    for line in inFile:
        for word in line.split():  # .strip() + ' '
            wordDict[word] = wordDict.get(word, 0) + 1
for word in wordDict:
    wordList.append([word, wordDict[word]])
wordList = sorted(wordList, key=lambda p: (-p[1], p[0]))
for word in wordList:
    print(word[0])
