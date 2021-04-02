# https://www.acmicpc.net/problem/14501
# 11:19-11:42, 12:03-13:25 : 해결 못함
# 13:25-17:00 : 솔루션 보면서 학습
'''
n + 1 일째에 퇴사
상담 기간 t와 보수 p가 주어질 때 얻을 수 있는 최대 수익
1 <= N <= 15
1 <= T_i <= 5
1 <= P_i <= 1,000

뒤에서 부터 거꾸로 계산
max_value = 뒤에서 부터 계산할 때 현재까지 구할 수 있는 최대 이익
dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
      = max(p[i] + dp[t[i] + i], max_value)
여기서 p[i] + dp[t[i] + i]는
p[i] + dp[t[i] + i] = 현재 상담 일자 이윤 + 현재 상담을 마친 일자부터 최대 이윤
'''
# Retry 2
n = int(input())
t = []
p = []
max_value = 0
for _ in range(n):
    t_, p_ = map(int, input().split())
    t.append(t_)
    p.append(p_)

# DP Table
d = [0] * n

for i in range(n - 1, -1, -1):
    time_councle = i + t[i]
    if time_councle <= n:
        # t[n-1] = 1인 경우, dp table 범위를 넘어가기 떄문에
        # d[time_councle]을 더하지 않음
        # mav_value와의 최댓값 비교는 계속 해주어야하는데,
        # 예를 들어 i = 3, t = n-4 인 경우,
        # dp[i]가 i번째 날 부터 마지막까지 낼 수 있는 최대이익이 되어야하는데
        # 단순 d[i] = p[i]로 설정할 경우 이것이 반영되지 않음
        if time_councle == n:
            d[i] = max(p[i], max_value)
        else:
            d[i] = max(p[i] + d[time_councle], max_value)
        max_value = d[i]
    else:
        d[i] = max_value
print(max_value)

# Solution
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp table initialization
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)

# # Retry(Failed)
# n = int(input())
# t_list = []
# p_list = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     t_list.append(t)
#     p_list.append(p)
# # print(t_list)
# # print(p_list)

# max_value = 0
# dp = [0] * n

# for i in range(n-1, -1, -1):
#     time = t_list[i] + i
#     if time > n:
#         continue
#     if t_list[i] + i < n:
#         dp[i] = max(p_list[i] + dp[t_list[i] + i], max_value)
#     else:
#         dp[i] = max(p_list[i], max_value)
#     max_value = max(dp[i],  max_value)
# print(max_value)

# My Solution(Failed)
# n = int(input())
# t_list = []
# p_list = []
# for _ in range(n):
#     t, p = map(int, input().split())
#     t_list.append(t)
#     p_list.append(p)
# print(t_list)
# print(p_list)

# max_value = 0
# dp = [0] * n
# for i in range(n):
#     dura = t_list[i]
#     j = i + dura
#     if j >= n:
#         continue
#     else:
#         dp[j] = p_list[i]
#     while j < n:
#         dura = t_list[j]
#         tmp_pay = p_list[j]
#         if dura == 1:
#             j += 1
#         else:
#             j += dura
#         if 0 > j or j >= n:
#             break
#         else:
#             print(j, n)
#             dp[j] += tmp_pay

#     print(i, max_value)
#     print(dp)
#     max_value = max(max_value, sum(dp))
# print(max_value)