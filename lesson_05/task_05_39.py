# Ферзи

# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли
# среди них пара бьющих друг друга.
#
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
# координаты 8 ферзей.
#
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

n = 8
Queen = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    Queen[i][0], Queen[i][1] = map(int, input().split())
# print(Queen)
flag = True
while flag:
    for i in range(n):
        for j in range(i+1, n):
            diff1 = Queen[i][0] - Queen[j][0]
            diff2 = Queen[i][1] - Queen[j][1]
            if diff1 == 0 or diff2 == 0 or abs(diff1) == abs(diff2):
                flag = False
                break
    else:
        break
print((1 - flag) * "YES" + flag * "NO")
