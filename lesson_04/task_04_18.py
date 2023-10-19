# Число сочетаний

# По данным целым числам n и k (0≤k≤n) вычислите C из n по k. Для решения
# используйте рекуррентное соотношение
# C(n,k) = C(n-1,k) + C(n-1,k-1).
#
# Решение оформите в виде функции C(n, k).


def C(n, k):
    if n == 0 or n == 1 or n == k or k == 0:
        return 1
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


n = int(input())
k = int(input())
print(C(n, k))
