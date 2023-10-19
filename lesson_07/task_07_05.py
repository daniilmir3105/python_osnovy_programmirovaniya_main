# Кубики

# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них
# свой набор и в каждом наборе все кубики различны по цвету. Однажды дети
# заинтересовались, сколько существуют цветов таких, что кубики каждого цвета
# присутствуют в обоих наборах. Для этого они занумеровали все цвета
# случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается
# помочь им в оставшейся части. Номер любого цвета — это целое число
# в пределах от 0 до 10⁹.

# В первой строке входного файла записаны числа N и M — количество кубиков
# у Ани и Бори соответственно. В следующих N строках заданы номера цветов
# кубиков Ани. В последних M строках номера цветов кубиков Бори.
#
# Выведите сначала количество, а затем отсортированные по возрастанию номера
# цветов таких, что кубики каждого цвета есть в обоих наборах, затем
# количество и отсортированные по возрастанию номера остальных цветов у Ани,
# потом количество и отсортированные по возрастанию номера остальных цветов
# у Бори.


N, M = tuple(map(int, input().split()))
NSet, MSet = set(), set()
NSet = {int(input()) for i in range(N)}
MSet = {int(input()) for i in range(M)}
NMSet = NSet & MSet
print(len(NMSet))
print(*sorted(NMSet))
NSetMinusNMSet = NSet - NMSet
print(len(NSetMinusNMSet))
print(*sorted(NSetMinusNMSet))
MSetMinusNMSet = MSet - NMSet
print(len(MSetMinusNMSet))
print(*sorted(MSetMinusNMSet))