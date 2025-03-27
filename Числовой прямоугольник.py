n = int(input())
m = int(input())

r = len(str(n * m))
for i in range(n):
    for j in range(m - 1):
        print((r - len(str(i * m + j + 1))) * ' ', end='')
        print(i * m + j + 1, end=' ')
    print((r - len(str(i * m + m))) * ' ', end='')
    print(i * m + m)