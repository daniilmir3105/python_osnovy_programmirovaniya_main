# Алгоритм Евклида

# Для быстрого вычисления наибольшего общего делителя двух чисел используют
# алгоритм Евклида. Он построен на следующем соотношении: НОД(a,b)=НОД(b,a%b).
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
#
# Вводится два целых числа.
# Выведите ответ на задачу.


def god(a, b):
    if a % b > 0:
        return god(b, a % b)
    else:
        return b


a = int(input())
b = int(input())
print(god(a, b))
