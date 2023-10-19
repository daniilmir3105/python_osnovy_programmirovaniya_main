# Пересечение множеств

# Даны два списка, упорядоченных по возрастанию (каждый список состоит
# из различных элементов).
#
# Найдите пересечение множеств элементов этих списков, то есть те числа,
# которые являются элементами обоих списков. Алгоритм должен иметь
# сложность O(len(A)+len(B)).
#
# Решение оформите в виде функции Intersection(A, B). Функция должна
# возвращать список пересечения данных списков в порядке возрастания
# элементов. Модифицировать исходные списки запрещается.


def Intersection(A, B):
    R, T = set(), set()
    for elem in A:
        T.add(elem)
    for elem in B:
        T.add(elem)
    for elem in T:
        if elem in A and elem in B:
            R.add(elem)
    C = [0 for i in range(len(R))]
    i = 0
    if len(A) <= len(B):
        for elem in A:
            if elem in R:
                C[i] = elem
                i += 1
    else:
        for elem in B:
            if elem in R:
                C[i] = elem
                i += 1
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(" ".join(map(str, Intersection(A, B))))
