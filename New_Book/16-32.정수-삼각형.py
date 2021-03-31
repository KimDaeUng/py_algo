# https://www.acmicpc.net/problem/1932
# 13:20-13:38
'''
삼각형의 각 줄 양 옆을 패딩한 nested list를 a라 할 때,
다음 점화식으로 계산한다
a[r][c] = a[r][c] + max(a[r-1][c-1], a[r-1][c])
'''

n = int(input())
data = []
for i in range(n):
    data.append([0] + list(map(int, input().split())) + [0])

for r in range(1, n):
    for c in range(1, len(data[r])-1):
        data[r][c] = data[r][c] + max(data[r-1][c-1], data[r-1][c])
print(max(data[r]))