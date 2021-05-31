# https://www.acmicpc.net/problem/1292
# 02:35-02:44
s, e = map(int, input().split())

arr = []
t = e

i = 1
cnt = 0
while cnt < t:
    cnt += i
    i += 1

for i in range(1, i + 1):
    arr.extend([i] * i)
print(sum(arr[s-1:e]))