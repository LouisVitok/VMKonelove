def evclid(n, m):
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
    return n


N = int(input())
a = int(input())
b = 0
for _ in range(N - 1):
    b = int(input())
    a = evclid(a, b)
    if a == 1:
        break
print(a)