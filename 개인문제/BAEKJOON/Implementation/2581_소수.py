# https://www.acmicpc.net/problem/2581
# 02:46-03:08
m = int(input())
n = int(input())

max_v = max(m, n)
dp = [0] + [1] * (max_v)

i = 2
while i < max_v + 1:
    if dp[i] == 1:
        j = 2
        while i * j < max_v + 1:
            dp[i * j] = 0
            j += 1
    i += 1

sum_r = 0
min_r = 10001
for d, v in enumerate(dp[m:n + 1], start=m):
    if v and d != 1:
        sum_r += d
        min_r = min(min_r, d)

if min_r == 10001:
    print(-1)
else:
    print(sum_r)
    print(min_r)