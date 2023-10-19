# Самое частое число

# Дан список. Не изменяя его и не используя дополнительные списки, определите,
# какое число в этом списке встречается чаще всего. Если таких чисел
# несколько, выведите любое из них.

numList = list(map(int, input().split()))
n = numList[0]
count = numList.count(n)
for i in range(1, len(numList)):
    ni = numList[i]
    if ni != n:
        counti = numList.count(ni)
        if counti > count:
            n = ni
            count = counti
print(n)
