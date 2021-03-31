# https://www.acmicpc.net/problem/1932
# 13:20-13:38
'''
삼각형의 각 줄 양 옆을 패딩한 nested list를 a라 할 때,
다음 점화식으로 계산한다
a[r][c] = a[r][c] + max(a[r-1][c-1], a[r-1][c])
'''

# My Solution
n = int(input())
data = []
for i in range(n):
    data.append([0] + list(map(int, input().split())) + [0])

for r in range(1, n):
    for c in range(1, len(data[r])-1):
        data[r][c] = data[r][c] + max(data[r-1][c-1], data[r-1][c])
print(max(data[r]))


# Solution
n = int(input())
dp = [] # dp table initialization

for _ in range(n):
    dp.append(list(map(int, input().split())))

# DP로 두 번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))