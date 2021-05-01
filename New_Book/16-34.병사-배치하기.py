# https://www.acmicpc.net/problem/18353
# 15:25-16:53 : 해결 못 함

# My Solution
n = int(input())
score = list(map(int, input().split()))

# DP Table
dp = [1] * n
max_drop = 1
# 가장 긴 감소하는 부분 수열(LDS) 알고리즘 수행
for i in range(n):
    for j in range(i):
        if score[j] > score[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            max_drop = max(max_drop, dp[i])
# 열외 시켜야 하는 병사의 최소 수를 출력
print(n - max_drop)


# Solution
n = int(input())
array = list(map(int, input().split()))
# 순서 뒤집어 '가장 긴 증가하는 부분 수열'문제로 변환
array.reverse()

# DP Table
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외 시켜야 하는 병사의 최소 수를 출력
print(dp)
print(n - max(dp))


# My Solution1 : Failed
'''
각 경우를 직접 시뮬레이션하여 조건을 만족하는 array를 구하려함
'''
# n = int(input())
# score = list(map(int, input().split()))

# if n == 1:
#     print(0)
#     exit()

# if n == 2:
#     if score[0] > score[1]:
#         print(0)
#     else:
#         print(1)
#     exit()

# max_s = score[0]
# prev_s = score[0]
# result = [score[0]]

# for i, s in enumerate(score):
#     if s > max_s or i == 0:
#         continue
#     if prev_s > s:
#         if s != max_s:
#             result.append(s)
#         prev_s = s
#     elif prev_s < s:
#         # Remove the last element
#         if s != max_s:
#             result.pop()
#             result.append(s)
#         prev_s = s
#     else: # s == prev_s 인 경우
#         continue

# # print(result)
# print(n - len(result))