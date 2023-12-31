# Упорядочить три числа

# Дано три числа. Упорядочите их в порядке неубывания. Программа должна
# считывать три числа a,b,c, затем программа должна менять их значения так,
# чтобы стали выполнены условия a≤b≤c, затем программа выводит тройку a,b,c.
#
# Дополнительные ограничения: нельзя использовать дополнительные переменные
# (то есть единственной допустимой операцией присваивания является обмен
# значений двух переменных типа (a, b) = (b, a).

a = int(input())
b = int(input())
c = int(input())
# (a, b) = (b, a)  # Обмен значений перменных
if b > c:
    (b, c) = (c, b)
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
print(a, b, c)
