# Номер числа Фибоначчи

# Последовательность Фибоначчи определяется так:
# F[0]=0, F[1]=1, ..., F[n]=F[n-1]+F[n-2].
# Дано натуральное число A. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что F[n]=A.
# Если А не является числом Фибоначчи,выведите число -1.

A = int(input())
if A == 0:
    n = 0
elif A == 1:
    n = 1
else:
    i = 2
    Fn_2 = 0
    Fn_1 = 1
    Fn = 1
    while Fn < A:
        # print(i, ":", Fn, Fn_1, Fn_2)
        (Fn, Fn_1, Fn_2) = (Fn + Fn_1, Fn, Fn_1)
        i = i + 1
    else:
        if Fn == A:
            n = i
        else:
            n = -1
print(n)