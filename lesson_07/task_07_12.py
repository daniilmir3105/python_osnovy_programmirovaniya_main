# Телефонные номера

# Телефонные номера в адресной книге мобильного телефона имеют один
# из следующих форматов: +7<код><номер>, 8<код><номер><номер>, где <номер> —
# это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
# Если код не указан, то считается, что он равен 495. Кроме того, в записи
# телефонного номера может стоять знак “-” между любыми двумя цифрами
# (см. пример). На данный момент в адресной книге телефона Васи записано
# всего три телефонных номера, и он хочет записать туда еще один. Но он
# не может понять, не записан ли уже такой номер в телефонной книге.
# Помогите ему! Два телефонных номера совпадают, если у них равны коды
# и равны номера. Например, +7(916)0123456 и 89160123456 — это один и тот же
# номер.

# В первой строке входных данных записан номер телефона, который Вася хочет
# добавить в адресную книгу своего телефона. В следующих трех строках записаны
# три номера телефонов, которые уже находятся в адресной книге телефона Васи.
# Гарантируется, что каждая из записей соответствует одному из трех
# приведенных в условии форматов.

# Для каждого телефонного номера в адресной книге выведите YES (заглавными
# буквами), если он совпадает с тем телефонным номером,который Вася хочет
# добавить в адресную книгу или NO (заглавными буквами) в противном случае.


def numberTranslate(number):
    plus = False
    numberNow = ""
    for num in number:
        if num == "+":
            plus = True
        elif num.isdigit():
            if plus and int(num) == 7:
                num = "8"
                plus = False
            numberNow += num
    if len(numberNow) < 11:
        numberNow = "8495" + numberNow
    return numberNow


number = numberTranslate(input())
for i in range(3):
    if number == numberTranslate(input()):
        print("YES")
    else:
        print("NO")
