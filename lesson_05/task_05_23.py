# Наименьший нечетный

# Выведите значение наименьшего нечетного элемента списка,
# гарантируется, что хотя бы один нечётный элемент в списке есть.

numList = list(map(int, input().split()))
min = ""
for i in range(len(numList)):
    if numList[i] % 2 == 1:
        if min == "":
            min = numList[i]
        elif numList[i] < min:
            min = numList[i]
print(min)
