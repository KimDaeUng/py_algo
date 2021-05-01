# https://leetcode.com/problems/ugly-number-ii/
# 20:00-21:30 : X
# Reference : https://www.youtube.com/watch?v=78Yx7oLA43s

# My Solution (retry)
n = int(input())

# Pointer
i2 = 0
i3 = 0
i5 = 0

# Next Multiple Values
next_m2 = 2
next_m3 = 3
next_m5 = 5

# DP Table
dp = [0] * n
dp[0] = 1


for i in range(1, n):
    dp[i] = min(next_m2, next_m3, next_m5)
    # print(f'i : {i}, dp[i] : {dp[i]}, next m235 : {next_m2, next_m3, next_m5}')
    if dp[i] == next_m2:
        i2 += 1
        next_m2 = dp[i2] * 2
    if dp[i] == next_m3:
        i3 += 1
        next_m3 = dp[i3] * 3
    if dp[i] == next_m5:
        i5 += 1
        next_m5 = dp[i5] * 5

# print(dp)
print(dp[-1])


#################################
# Solution1 : DP
n = int(input())
ugly = [0] * n
ugly[0] = 1

# 2, 3, 5배를 위한 인덱스
i2 = i3 = i5 = 0

# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지 못생긴 수 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])


#################################
# Solution2 : Brute Force : Time Limit Exceeded (O(N^2))
n = int(input())

# Base Case
if n == 1:
    print(1)
    exit()

# def to judge x as ugly number or not
def is_ugly(x):
    uglz = (2, 3, 5)
    while x > 1:
        prev_x = x
        for u in uglz:
            q, r = divmod(x, u)
            if r == 0:
                x = q
        if prev_x == x:
            break
    if x == 1:
        return True
    else:
        return False

# Find ugly number
count = 1
i = 2
answer = 0

while count < n:
    if is_ugly(i):
        count += 1
        answer = i
    i += 1

print(answer)

# My Solution : Failed
# n = int(input())
# ug = [2, 3, 5]

# '''
# 2, 3, 5의 배수 또한 못생긴 수
# 각 수에 2이상의 수를 계속 곱하면서 n번째 못생긴 수가 나올 때까지 구한다.
# '''

# result = {1, 2, 3, 5}

# i = 2
# # O(N * M * P)
# while True:
#     for u in ug:
#         next_ug = u * i
#         if next_ug not in result:
#             result.add(u * i)
#     if i * 2 >= n:
#         break
#     i += 1
# result = list(result)
# # O(NlogN)
# result.sort()
# print(result)
# # O(N)
# print(result[n-1])