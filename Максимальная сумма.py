N = int(input())

max_n = 0
max_i = ''
for i in range(N):
    name = input()
    number = sum([int(x) for x in str(int(input()))])
    if number >= max_n:
        max_n = number
        max_i = name
print(max_i)