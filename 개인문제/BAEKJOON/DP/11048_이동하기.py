# https://www.acmicpc.net/problem/11048
# 4h?
string = '''3 4
1 2 3 4
0 0 0 5
9 8 7 6'''

# string = '''3 3
# 1 0 0
# 0 1 0
# 0 0 1'''

# string = '''4 3
# 1 2 3
# 6 5 4
# 7 8 9
# 12 11 10'''

# string = '''2 1
# 1
# 3'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 4: Retry(Solution)
# https://dev-gorany.tistory.com/6
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

maps = [[0] * (m + 1)]
for i in range(n):
    maps.append([0] + list(map(int, input().split())))

dp = maps[:]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = maps[i][j] + \
                  max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])

# My Solution2: Timeout
# import heapq as hq
# import sys
# # input = sys.stdin.readline
# n, m = map(int, input().split())

# dr = [1, 0, 1]
# dc = [0, 1, 1]

# maps = []
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# q = []
# q.append((maps[0][0], 0, 0)) # value, r, c
# result = 0
# while q:
#     val, r, c = hq.heappop(q)
#     if r == n - 1 and c == m - 1:
#         result = max(result, val)
#     for i in range(3):
#         nr = dr[i] + r
#         nc = dc[i] + c

#         if nr < 0 or nr >= n \
#             or nc < 0 or nc >= m:
#             continue
#         q.append((maps[nr][nc] + val, nr, nc))

# print(result)

# My Solution 3: Simple DP
# import heapq as hq
# import sys
# # input = sys.stdin.readline
# n, m = map(int, input().split())

# dr = [1, 0, 1]
# dc = [0, 1, 1]

# maps = []
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# for c in range(m):
#     for r in range(n):
#         # 1) LU
  
#         lu_br = r - 1
#         if lu_br < 0:
#             lu_val = 0
#         else:
#             lu_val = maps[lu_br][c - 1]
        
#         # 2) L
#         l_val = maps[r][c - 1]

#         # 3) U
#         u_bc = c - 1
#         if u_bc < 0:
#             u_val = 0
#         else:
#             u_val = maps[r][c - 1]

#         maps[r][c] =  max(maps[r][c],
#                           maps[r][c] + max(lu_val, l_val, u_val))

# print(maps[n-1][m-1])


# My Solution 1: Timeout
# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())

# dr = [1, 0, 1]
# dc = [0, 1, 1]

# maps = []
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# dp = [[0] * m for _ in range(n)]
# dp[0][0] = 1

# q = deque([])
# q.append((0, 0))
# while q:
#     r, c = q.popleft()
#     cur_val = dp[r][c]
    
#     for i in range(3):
#         nr = dr[i] + r
#         nc = dc[i] + c

#         if nr < 0 or nr >= n \
#             or nc < 0 or nc >= m:
#             continue
#         q.append((nr, nc))
#         dp[nr][nc] = max(dp[nr][nc], maps[nr][nc] + cur_val)

# print(dp[n-1][m-1])

# My Solution2: Timeout
# import heapq as hq
# import sys
# # input = sys.stdin.readline
# n, m = map(int, input().split())

# dr = [1, 0, 1]
# dc = [0, 1, 1]

# maps = []
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# q = []
# q.append((maps[0][0], 0, 0)) # value, r, c
# result = 0
# while q:
#     val, r, c = hq.heappop(q)
#     if r == n - 1 and c == m - 1:
#         result = max(result, val)
#     for i in range(3):
#         nr = dr[i] + r
#         nc = dc[i] + c

#         if nr < 0 or nr >= n \
#             or nc < 0 or nc >= m:
#             continue
#         q.append((maps[nr][nc] + val, nr, nc))

# print(result)


# import heapq as hq
# import sys
# # input = sys.stdin.readline
# n, m = map(int, input().split())

# dr = [1, 0, 1]
# dc = [0, 1, 1]

# maps = []
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# for i in range(2):
#     maps[i][1] += maps[0][0]
# print(maps)
# for c in range(2, m):
#     for r in range(n):
#         # 1) LU
  
#         lu_br = r - 1
#         if lu_br < 0:
#             lu_val = 0
#         else:
#             lu_val = maps[lu_br][c - 1]
        
#         # 2) L
#         l_val = maps[r][c - 1]

#         # 3) LD
#         ld_br = r + 1
#         if ld_br >= n:
#             ld_val = 0
#         else:
#             ld_val = maps[ld_br][c - 1]

#         maps[r][c] =  max(maps[r][c],
#                           maps[r][c] + max(lu_val, l_val, ld_val))
# print(maps[n-1][m-1])