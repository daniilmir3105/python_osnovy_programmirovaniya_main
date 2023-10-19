# Уникальные элементы

# Дан список. Выведите те его элементы, которые встречаются в списке только
# один раз. Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

numList = list(map(int, input().split()))
checked = set()
for i in range(len(numList)):
    num = numList[i]
    if num not in checked:
        tail = numList[i+1:]
        if num not in tail:
            print(num, end=" ")
        checked.add(num)
