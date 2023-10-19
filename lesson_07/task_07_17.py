# Самое частое слово

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом
# порядке.


txt = ""
wordDict = dict()
wordList = list()
with open("input_task_07_17.txt") as inFile:
    for line in inFile:
        txt += line  # .strip() + ' '
for word in txt.split():
    wordDict[word] = wordDict.get(word, 0) + 1
for word in wordDict:
    wordList.append([word, wordDict[word]])
wordList = sorted(wordList, key=lambda p: (-p[1], p[0]))
print(wordList[0][0])
