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
    C = [0 for i in range(len(A) + len(B))]
    i, j, k = 0, 0, 0
    while i <= len(A) - 1 and j <= len(B) - 1:
        if A[i] == B[j]:
            if k == 0 or k > 0 and A[i] != C[k-1]:
                C[k] = A[i]
                k += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
    i = len(C) - 1
    while i >= 0 and C[i] == 0:
        C.pop()
        i -= 1
    if 0 in A and 0 in B and A[len(A) - 1] == 0:
        C.append(0)
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(" ".join(map(str, Intersection(A, B))))
