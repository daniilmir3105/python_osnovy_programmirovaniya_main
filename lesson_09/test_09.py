lst = [1, 2, 3]
newLst = lst.copy()
lst[1] = 5
print(newLst)
print(lst)



class Matrix(list):
    pass

a = Matrix([10,20,50])
print(a)


# Ошибки, транспонирование

# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий
# внутри self поля matrix1 и matrix2 (ссылки на матрицы).

# В класс Matrix внесите следующие изменения:
# Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы
# при попытке сложить матрицы разных размеров было выброшено исключение
# MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
# аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для
# сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
# (данный метод модифицирует экземпляр класса Matrix).
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий
# транспонированную матрицу.
# Пример статического метода.
# https://ru.wikipedia.org/wiki/
# Объектно-ориентированное_программирование_на_Python
