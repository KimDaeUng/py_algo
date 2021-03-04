# https://www.acmicpc.net/problem/14888
# 21:10-21:20 / 16:41-17:13 # total : 45m
# 모든 가능한 연산자 조합을 구한 다음,
# 각 결과값을 계산해가며 최대, 최소값을 갱신해 출력
# 이게 왜 DFS/BFS ?
# from itertools import permutations
# import sys

# n = int(input())
# operands = list(map(int, input().split()))
# operators = list(map(int, input().split()))


# opreators_chr = ''
# for idx, e in enumerate(operators):
#     if idx == 0:
#         opreators_chr += '+'*e
#     if idx == 1:
#         opreators_chr += '-'*e
#     if idx == 2:
#         opreators_chr += '*'*e
#     if idx == 3:
#         opreators_chr += '/'*e

# opreators_chr = list(opreators_chr)

# min_result = sys.maxsize
# max_result = -sys.maxsize

# for data in permutations(opreators_chr, n-1):
#     result = operands[0]
#     for i in range(n-1):
#         if data[i] == '+':
#             result += operands[i+1]
#         if data[i] == '-':
#             result -= operands[i+1]
#         if data[i] == '*':
#             result *= operands[i+1]
#         if data[i] == '/':
#             # result //= operands[i+1]
#             if result < 0 and operands[i+1] > 0:
#                 result *= -1
#                 result //= operands[i+1]
#                 result *= -1
#             else:
#                 result //= operands[i+1]
#     min_result = min(min_result, result)
#     max_result = max(max_result, result)

# print(max_result)
# print(min_result)

# Solution
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값 & 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이우선탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)