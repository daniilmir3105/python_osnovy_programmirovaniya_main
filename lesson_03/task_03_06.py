# Проценты

# Процентная ставка по вкладу составляет P процентов годовых, которые
# прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите
# размер вклада через год. При решении этой задачи нельзя пользоваться
# условными инструкциями и циклами.

P = int(input())
X = int(input())
Y = int(input())

Z = (X * 100 + Y) * (100 + P) / 100
print(int(Z / 100), int(Z % 100))
