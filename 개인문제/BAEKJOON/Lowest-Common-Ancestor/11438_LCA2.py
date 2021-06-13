# https://www.acmicpc.net/problem/11438
'''
DFS를 이용한 기본적인 LCA 알고리즘의 시간복잡도 : O(NM)
이 문제는 N (2<= N <= 100,000)개의 정점으로 이루어진 트리가 주어지며
M (1<= M <= 100,000)개의 간선이 주어지므로 위의 시간 복잡도로는 시간 초과

각 노드가 거슬러 올라가는 속도를 BIT를 이용해 개선한다.
'''
# 11:35-16:07
string = '''15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n = int(input())
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
log_max = 17
# 노드의 개수 n = 100,000
# log_2(1e5) = 16.61... -> 17
parent_bit = [ [0] * log_max for _ in range(n + 1) ]
check = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now, d):
    check[now] = True
    depth[now] = d
    for adj_node in graph[now]:
        if check[adj_node]:
            continue
        parent_bit[adj_node][0] = now
        dfs(adj_node, d + 1)
dfs(1, 0)

# A와 B의 LCA 찾는 함수
def lca(a, b):
    # a, b의 깊이가 동일해지도록 깊이가 깊은 쪽에서 거슬러 올라옴
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(log_max - 1, -1, -1):
        if (depth[b] - depth[a]) >= (2 ** i):
            b = parent_bit[b][i]

    if a == b:
        return a
    
    for i in range(log_max - 1, -1, -1):
        # 왜 else때 break하지 않는지?
        if parent_bit[a][i] != parent_bit[b][i]:
            a = parent_bit[a][i]
            b = parent_bit[b][i]

    return parent_bit[a][0]

# 2의 제곱꼴 건너뛸때 부모값 기록
for i in range(1, log_max):
    for cur_node in range(1, n + 1):
        parent_bit[cur_node][i] = \
        parent_bit[parent_bit[cur_node][i-1]][i-1]
# import pprint
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

# pprint.pprint(parent_bit)

'''
 [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  2 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  3 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  4 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  5 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  6 [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  7 [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  8 [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  9 [4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 10 [4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 11 [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 12 [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 13 [7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 14 [7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 15 [11, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# def dfs(root):
#     stack = [(root, 0)]
#     while stack:
#         now, d = stack.pop()
#         check[now] = True
#         depth[now] = d
#         for adj_node in graph[now]:
#             if check[adj_node]:continue
#             parent_bit[adj_node][0] = now
#             stack.append((adj_node, d + 1))

    # i = 0
    # while depth[a] != depth[b]:
    #     if (depth[b] & -depth[b]) > 2:
    #         b = parent_bit[b][i]
    #         i += 1
    #     else:
    #         b = parent_bit[b][0]
    
    # # 노드가 같아지도록
    # i = 0
    # while a != b:
    #     if (depth[b] & -depth[b]) > 2:
    #         a = parent_bit[a][i]
    #         b = parent_bit[b][i]
    #         i += 1
    #     else:
    #         a = parent_bit[a][0]
    #         b = parent_bit[b][0]
    # return a

# def dfs(now, d):
#     check[now] = True
#     depth[now] = d
#     for adj_node in graph[now]:
#         if check[adj_node]:continue
#         parent_bit[adj_node][0] = now
#         dfs(adj_node, d + 1)

# def update_parents():
#     for cur_node in range(1, n + 1):
#         # 깊이변수 만들어 2씩 나누어 가면서 parent 노드를 각각에 기록하면?
#         # 이렇게 하면 O(NM)이 됨....
#         d = depth[cur_node]
#         i = 1
#         node = cur_node
#         while d > 0:
#             node = parent_bit[node][0]
#             # 2의 제곱수일 때마다 parent_bit에 기록
#             if d % 2 * i == 0:
#                 parent_bit[cur_node][i] = node
#                 i += 1
#             d -= 1
        # d = 1
        # i = 1
        # node = cur_node
        # while d <= depth[cur_node]:
        #     node = parent_bit[node][0]
        #     # 2의 제곱수일 때마다 parent_bit에 기록
        #     if d % 2 * i == 0:
        #         parent_bit[cur_node][i] = node
        #         i += 1
        #     d += 1
'''