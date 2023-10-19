# Принадлежит ли точка области

# Проверьте, принадлежит ли точка данной закрашенной области.

# Если точка принадлежит области (область включает границы), выведите слово
# YES, иначе выведите слово NO. Решение должно содержать функцию
# IsPntInArea(x, y), возвращающую True, если точка принадлежит области и
# False, если не принадлежит. Основная программа должна считать координаты
# точки, вызвать функцию IsPntInArea и в зависимости от возвращенного
# значения вывести на экран необходимое сообщение. Функция IsPntInArea
# не должна содержать инструкцию if.


def IsPntInAngle(x, y):
    return (y >= -x) * (y >= 2 * x + 2) + (y <= -x) * (y <= 2 * x + 2)


def IsPntInCircle(x, y, xc, yc, r):
    return (y >= 0) * ((x - xc) ** 2 + (y - yc) ** 2 <= r ** 2) + \
           (y < 0) * ((x - xc) ** 2 + (y - yc) ** 2 < r ** 2)


def IsPntInArea(x, y):
    return (y > 0) * IsPntInAngle(x, y) * IsPntInCircle(x, y, -1, 1, 2) + \
           (y < 0) * IsPntInAngle(x, y) * (1 - IsPntInCircle(x, y, -1, 1, 2))


x = float(input())
y = float(input())

ipia = IsPntInArea(x, y)
print(ipia * "YES" + (1 - ipia) * "NO")
