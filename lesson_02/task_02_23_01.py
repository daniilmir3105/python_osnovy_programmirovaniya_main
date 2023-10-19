# Спички*

# Вдоль прямой выложены три спички. Необходимо переложить одну из них так,
# чтобы при поджигании любой спички сгорали все три. Для того чтобы огонь
# переходил с одной спички на другую, необходимо чтобы эти спички
# соприкасались (хотя бы концами).
#
# Требуется написать программу, определяющую, какую из трех спичек
# необходимо переместить.
#
# Вводятся шесть целых чисел : l₁,r₁,l₂,r₂,l₃,r₃ –– координаты первой, второй
# и третьей спичек соответственно (0 ≤ lᵢ < rᵢ ≤ 100). Каждая спичка
# описывается координатами левого и правого концов по горизонтальной оси OX.
#
# Выведите номер искомой спички. Если возможных ответов несколько, то выведите
# наименьший из них. В случае, когда нет необходимости перемещать какую-либо
# спичку, выведите 0. Если же требуемого результата достигнуть невозможно,
# то выведите -1.

l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

# answer = start1 <= finish2 and start2 <= finish1

cross12 = l1 <= r2 and l2 <= r1
cross13 = l1 <= r3 and l3 <= r1
cross23 = l2 <= r3 and l3 <= r2

len1 = r1 - l1
len2 = r2 - l2
len3 = r3 - l3

if cross12 and cross13 and cross23:
    print(0)
elif cross12 and (cross13 or cross23):
    print(0)
elif cross13 and cross23:
    print(0)
elif cross23:
    print(1)
elif cross13:
    print(2)
elif cross12:
    print(3)  # Возможно стоит подвинуть пересекающиеся спички!
# Далее - не пересекаются, кроме 12
else:
    if l1 <= l2 <= l3:
        if l3 - r2 <= len1:
            print(1)
        elif l2 - r1 <= len3:
            print(3)
        else:
            print(-1)
    elif l1 <= l3 <= l2:
        if l2 - r3 <= len1:
            print(1)
        elif l3 - r1 <= len2:
            print(2)
        else:
            print(-1)
    elif l2 <= l1 <= l3:
        if l3 - r1 <= len2:
            print(2)
        elif l1 - r2 <= len3:
            print(3)
        else:
            print(-1)
    elif l2 <= l3 <= l1:
        if l3 - r2 <= len1:
            print(1)
        elif l1 - r3 <= len2:
            print(2)
        else:
            print(-1)
    elif l3 <= l1 <= l2:
        if l1 - r3 <= len2:
            print(2)
        elif l2 - r1 <= len3:
            print(3)
        else:
            print(-1)
    else:
        print(-1)
