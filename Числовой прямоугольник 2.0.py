n = int(input())
m = int(input())

r = len(str(n * m))
for i in range(n):
    for j in range(m - 1):
        print((r - len(str(j * n + i + 1))) * ' ', end='')
        print(j * n + i + 1, end=' ')
    print((r - len(str((m - 1) * n + i + 1))) * ' ', end='')
    print((m - 1) * n + i + 1)