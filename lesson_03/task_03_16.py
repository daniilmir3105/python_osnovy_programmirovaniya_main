# Удаление фрагмента

# Дана строка, в которой буква h встречается минимум два раза. Удалите
# из этой строки первое и последнее вхождение буквы h, а также все символы,
# находящиеся между ними.

s = input()
pos1 = s.find('h')
pos2 = s[::-1].find('h')
pos2 = len(s) - pos2 - 1
news = s[:pos1]+s[pos2+1:]
print(news)
