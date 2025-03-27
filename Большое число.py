N = int(input())
sum_ = 0
for _ in range(N):
    max_ = max([int(x) for x in str(int(input()))])
    sum_ = 10 * sum_ + max_
print(sum_)