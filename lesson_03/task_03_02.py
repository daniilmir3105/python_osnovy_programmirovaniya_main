# Сумма ряда

# По данному числу n вычислите сумму 1+(1 / 2²)+(1 / 3²)+...+(1 / n²).

n = int(input())
epsilon = 5 * 10**-7

sumSquare = 0
i = 1
while i <= n:
    sumSquare += 1 / i ** 2
    i += 1
# print(sumSquare)

if abs(sumSquare - round(sumSquare, 5)) < epsilon:
    print(sumSquare)
else:
    print('{0:.6f}'.format(sumSquare))
