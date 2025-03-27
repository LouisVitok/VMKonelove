n = int(input())
m = int(input())

r = len(str(n * m))
for i in range(n):
    if i % 2 == 0:
        for j in range(m - 1):
            print((r - len(str(i * m + j + 1))) * ' ', end='')
            print(i * m + j + 1, end=' ')
        print((r - len(str(i * m + m))) * ' ', end='')
        print(i * m + m)
    else:
        for j in range(m - 1):
            print((r - len(str((i + 1) * m - j))) * ' ', end='')
            print((i + 1) * m - j, end=' ')
        print((r - len(str(i * m + 1))) * ' ', end='')
        print(i * m + 1)