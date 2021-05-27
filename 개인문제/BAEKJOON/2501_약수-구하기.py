# https://www.acmicpc.net/problem/2501
n, k = map(int, input().split())
divider = []
for i in range(1, n + 1):
    if n % i == 0:
        divider.append(i)

if len(divider) < k:
    print(0)
else:
    print(divider[k - 1])