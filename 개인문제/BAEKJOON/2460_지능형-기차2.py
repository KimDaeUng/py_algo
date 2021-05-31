# https://www.acmicpc.net/problem/2460
# 01:09-01:12

crowd = 0
max_crowd = 0
for i in range(1, 11):
    out_, in_ = map(int, input().split())
    crowd -= out_
    crowd += in_
    max_crowd = max(crowd, max_crowd)
print(max_crowd)