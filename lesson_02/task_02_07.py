# Цвет клеток шахматной доски

# Заданы две клетки шахматной доски. Если они покрашены в один цвет,
# то выведите слово YES, а если в разные цвета – то NO.

cellR1 = int(input())
cellC1 = int(input())
cellR2 = int(input())
cellC2 = int(input())

if (cellR1 + cellC1 + cellR2 + cellC2) % 2 == 0:
    print("YES")
else:
    print("NO")
