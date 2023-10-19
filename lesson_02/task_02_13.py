# Тип треугольника

# Даны три стороны треугольника a,b,c. Определите тип треугольника
# с заданными сторонами. Выведите одно из четырех слов:
# rectangular для прямоугольного треугольника,
# acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника
# или impossible, если треугольника с такими сторонами не существует.

a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("impossible")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("rectangular")
elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
    print("obtuse")
else:
    print("acute")
