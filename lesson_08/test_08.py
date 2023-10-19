def myRange(n):
    i = 0
    while i < n:
        yield i**2
        i += 1

for i in myRange2(100):
    temp = i
    print(temp)


def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1
for i in myRange(10):
    print(i)