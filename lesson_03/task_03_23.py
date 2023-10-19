# Замена внутри фрагмента

# Дана строка. Замение в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

s = input()
pos1 = s.find("h")
pos2 = s.rfind("h")
if pos1 >= -1 and pos2 >= -1 and pos1 != pos2:
    print(s[:pos1+1] + s[pos1+1:pos2].replace("h", "H") + s[pos2:])
else:
    print(s)
