# Удалить каждый третий символ

# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
# Символы строки нумеруются, начиная с нуля.
#
# Ввод и вывод осуществлять с помощью файлов

s = input()
news = ""
i = 0
while i <= len(s) - 1:
    if i % 3 != 0:
        news += s[i]
    i += 1
print(news)
