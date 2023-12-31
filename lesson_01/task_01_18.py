# Электронные часы - 2

# Электронные часы показывают время в формате h:mm:ss,
# то есть сначала записывается количество часов,
# потом обязательно двузначное количество минут,
# затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются
# до двузначного числа нулями.

# С начала суток прошло N секунд. Выведите, что покажут часы.

# Примечания
# Вывести числа можно поциферно.

N = int(input())
sec = N % 60
hour = N // (3600)
min = N // 60 - hour * 60
day = hour // 24
hour = hour - day * 24

# print(day, hour, min, sec)
print(hour, ':', min // 10, min % 10, ':', sec // 10, sec % 10, sep='')
# print(day * 24 * 3600 + hour * 3600 + min * 60 + sec)
