# https://www.acmicpc.net/problem/11437
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

# My Solution : 기존 Solution 복기 코드
import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기
input = sys.stdin.readline

n = int(input())
parent = [0] * (n + 1)
d = [0] * (n + 1) # 각 노드 까지의 깊이
c = [0] * (n + 1) # 각 노드 까지의 깊이가 계산되었는지 여부
graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 무방향 그래프 처리 하지 않으면 잘못된 결과 -> 왜?

# 각 노드의 깊이 및 부모 노드 저장
def dfs(node, depth):
    c[node] = True
    d[node] = depth

    for adj_node in graph[node]:
        if c[adj_node]:continue
        parent[adj_node] = node
        dfs(adj_node, depth + 1)

# A와 B의 LCA 찾는 함수
def lca(a, b):
    # a, b의 깊이가 동일해지도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a =  parent[a]
        elif d[a] < d[b]:
            b = parent[b]
    
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
