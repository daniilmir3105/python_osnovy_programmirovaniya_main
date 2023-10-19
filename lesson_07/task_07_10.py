# Пересадки

# На Новом проспекте для разгрузки было решено пустить два новых автобусных
# маршрута на разных участках проспекта. Известны конечные остановки каждого
# из автобусов. Определите количество остановок, на которых можно пересесть
# с одного автобуса на другой.

# Вводятся четыре числа, не превосходящие 100, задающие номера конечных
# остановок. Сначала для первого, потом второго автобуса (см. примеры
# и рисунок).
#
# Ваша программа должна выводить одно число – искомое количество остановок.
#
# Примечания
# Пояснения. Первый пример (см. рисунок): первый автобус ходит с 3-й остановки
# по 6-ю и обратно, а второй с 2-й по 4-ю и обратно. Пересесть с одного
# автобуса на другой можно на 3-й и 4-й остановках. Их две. Второй пример:
# автобусы не имеют общих остановок.


l1, r1, l2, r2 = tuple(map(int, input().split()))
set1 = set(range(min(l1, r1), max(l1, r1) + 1))
set2 = set(range(min(l2, r2), max(l2, r2) + 1))
print(len(set1 & set2))
