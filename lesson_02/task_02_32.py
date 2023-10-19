# Сумма квадратов

# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

# n = int(input("Введите натуральное n: "))
n = int(input())

sumSquare = 0
i = 1
while i <= n:
    sumSquare += i**2
    i += 1
# print("Сумма квадратов равна:", sumSquare)
print(sumSquare)
