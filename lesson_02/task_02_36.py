# Количество четных элементов последовательности

# Определите количество четных элементов в последовательности,
# завершающейся числом 0.

n = int(input())
countEvenElem = 0
while n != 0:
    if n % 2 == 0:
        countEvenElem += 1
    n = int(input())
print(countEvenElem)
