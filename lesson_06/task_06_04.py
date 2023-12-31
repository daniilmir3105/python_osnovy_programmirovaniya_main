# Обувной магазин

# В обувном магазине продается обувь разного размера. Известно, что одну пару
# обуви можно надеть на другую, если она хотя бы на три размера больше.
# В магазин пришел покупатель.Требуется определить, какое наибольшее
# количество пар обуви сможет предложить ему продавец так, чтобы он смог
# надеть их все одновременно.
#
# Сначала вводится размер ноги покупателя (обувь меньшего размера он надеть
# не сможет), в следующей строке — размеры каждой пары обуви в магазине
# через пробел. Размер — натуральное число, не превосходящее 100.
#
# Выведите единственное число — максимальное количество пар обуви, которое
# сможет надеть покупатель.

size = int(input())
sizes = list(map(int, input().split()))
sizes.sort()
i = 0
while i < len(sizes) and sizes[i] < size:
    i += 1
count = 0
while i < len(sizes):
    if size <= sizes[i]:
        count += 1
        cs = sizes[i]
        while i < len(sizes) and cs + 3 > sizes[i]:
            i += 1
print(count)
