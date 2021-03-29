# 16:52- 17:30 못 품
# x = int(input())

# ops = {'a' : lambda x : divmod(x, 5),
#        'b' : lambda x : divmod(x, 3),
#        'c' : lambda x : divmod(x, 2),
#        'd' : lambda x : (x - 1, 0)}

# from collections import deque
# import sys
# # (value, ops)
# q = deque([(x, [])])

# def solution(x):
#     min_depth = sys.maxsize
#     min_ops = []
#     while q:
#         cur_value, cum_ops = q.popleft()
#         if cur_value == 1:
#             cur_depth = len(cum_ops)
#             if min_depth > cur_depth:
#                 min_depth = cur_depth
#                 min_ops = cum_ops
            
#         for name_ops, func in ops.items():
#             res, remain = func(cur_value)
#             if res < 1:
#                 continue
#             if remain == 0:
#                 q.append((res, cum_ops + [name_ops]))
#     return min_depth

# print(solution(x))

# Solution
# 정수 X 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# (i 지점까지의 계산 횟수가 저장된 DP 테이블)
d = [0] * 30001

# 다이나믹 프로그래밍 진행(Bottom-Up)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])