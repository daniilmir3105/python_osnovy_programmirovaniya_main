# Создание архива

# Системный администратор вспомнил, что давно не делал архива пользовательских
# файлов. Однако, объем диска, куда он может поместить архив, может быть
# меньше, чем суммарный объем архивируемых файлов.
#
# Известно, какой объем занимают файлы каждого пользователя.
#
# Напишите программу, которая по заданной информации о пользователях и
# свободному объему на архивном диске определит максимальное число
# пользователей, чьи данные можно поместить в архив, при этом используя
# свободное место как можно более полно.
#
# Программа получает на вход в одной строке число S – размер свободного места
# на диске (натуральное, не превышает 10000), и число N – количество
# пользователей (натуральное, не превышает 100), после этого идет N чисел -
# объем данных каждого пользователя (натуральное, не превышает 1000),
# записанных каждое в отдельной строке.
#
# Выведите наибольшее количество пользователей, чьи данные могут быть помещены
# в архив.


S, N = list(map(int, input().split()))
v = [int(input()) for i in range(N)]
# for i in range(N):
#    v[i] = int(input())
v.sort()
i = 0
while i < len(v) and S >= v[i]:
    S -= v[i]
    i += 1
print(i)
