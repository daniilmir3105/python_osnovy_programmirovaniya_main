# Теорема Лагранжа

# Теорема Лагранжа утверждает, что любое натуральное число можно представить
# в виде суммы четырех точных квадратов. По данному числу n найдите такое
# представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых
# дают в сумме данное число.
#
# Программа получает на вход одно натуральное число n < 10000.
#
# Программа должна вывести от 1 до 4 натуральных чисел, квадраты которых дают
# в сумме данное число.


def Lagrang(n, k):  # k - максимальное количество слагаемых
    s = 0
    i = int(n * (1 / 2))
    if n - i**2 > 0:
        Lagrang()
        i -= 1



n = int(input())
Lagrang(n, 4)
