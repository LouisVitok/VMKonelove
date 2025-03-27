def primery(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


s = 0
N = int(input())
for _ in range(N):
    number = int(input())
    if primery(number):
        s += 1
print(s)