# Слияние списков

# Даны два списка A и B упорядоченных по неубыванию. Объедините их в один
# упорядоченный список С (то есть он должен содержать len(A)+len(B)
# элементов). Решение оформите в виде функции merge(A, B), возвращающей
# новый список. Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается. Использовать функцию
# sorted и метод sort запрещается.


def merge(A, B):
    i, j, k = 0, 0, 0
    C = [0 for k in range(len(A) + len(B))]
    while i < len(A) or j < len(B):
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C[k] = A[i]
                i += 1
            else:
                C[k] = B[j]
                j += 1
        elif i >= len(A):
            C[k] = B[j]
            j += 1
        elif j >= len(B):
            C[k] = A[i]
            i += 1
        k += 1
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(" ".join(map(str, merge(A, B))))
