# 18:26-19:16
'''
- 각 칸을 순회하면서 모든 경우를 다 시도해본다.
- board를 만들어 기록? -> 실패

# Solution
- 왼쪽부터 차례대로 채운다고 할때, i번째 열에서의 가능한 경우의 수를 dp[i]에 저장
- 현재 i번째 열을 채운다고 할 때, 가능한 경우는 2가지
  1) 왼쪽부터 i-1번째까지 덮개로 이미 채워져 있는 경우, 2 x 1 덮개를 채우는 하나의 경우만 존재
  2) 왼쪽부터 i-2번째까지 덮개로 이미 채워져 있는 경우, 1 x 2 덮개 2개를 넣는 경우, 혹은 2 x 2 덮개 하나 넣는 경우로 2가지 경우 존재
-> 각 경우까지 도달하기 위한 경우의 수를 dp[i]에 저장하고 매번 더해서 갱신해나간다.
'''

# Retry
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i-1] + 2 * dp[i - 2] % 796796

print(d[n])

# Solution
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행(Bottom-Up)
d[1] = 1 # (2 x 1) + (2 x 1)의 한 가지 방법
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])

# My Solution(failed)
# n = int(input())
# board = [ [0] * n for _ in range(2) ]
# dp = [ [0] * n for _ in range(2) ]

# # 덮개의 좌표
# # index : 0, 1, 또는 0 + 1 + 2
# dr = [1, 0, 1]
# dc = [0, 1, 1]

# count = 0
# def simul(dp, r, c, square=False):
#     global count
#     dp[r][c] = 1

#     if square == True:
#         dp[r - 1][c] = 1
#         dp[r][c - 1] = 1
    
#     if 2 * n == sum([ j for i in dp for j in i]):
#         count += 1
#         return None
    
#     # 1. 1 x 2
#     simul(dp, r + 1, c)

#     # 2. 2 x 1
#     simul(dp, r, c + 1)

#     # 3. 2 x 2
#     simul(dp, r + 1, c + 1)

    


# for r in range(n):
#     for c in range(2):
#         board[]


# while True:

#     r, c = q.popleft()
    
#     for i in range(3):
#         nr = r + dr[i]
        # nc = r + dc[i]