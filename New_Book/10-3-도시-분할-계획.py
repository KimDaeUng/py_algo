# https://www.acmicpc.net/problem/1647
# 19:20-20:34 못 품
# My Solution
'''
그래프를 두 개의 MST로 분할할 때, 전체 간선 비용을 최소로하는 경우를 찾아 그 값을 반환하라..
MST를 구한 뒤 부모 노드가 2이상인 그래프에대해서 모든 간선이 연결되는지와 그 비용을 확인한다.

1. 전체 그래프에 대해 Kruskal
간선을 확인하는 과정에서 tmp list에 간선 정보를 모아둔다
현재 간선 정보에서 루트노드가 기존과 동일하게 나올 경우 현재 간선을 tmp list에 추가하고
해당 list를 하나의 마을로 한다?

'''

string = '''7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(n+1))

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    edges.append((c, b, a))

edges.sort()
# Union-Find 수행
for edge in edges:
    c, a, b = edge
    union_parent(parent, a, b)

tmp = { i : [] for i in range(1, n + 1)}
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) == find_parent(parent, b):
        tmp[find_parent(parent, a)].append(edge)
tmp[0]
# from collections import Counter
# count = Counter(parent[1:])

print(tmp)
print(parent)
# tmp = []
# for edge in edges:
#     a, b, cost = edge
#     if find_parent(parent, a) == find_parent(parent, b):
#         tmp.append(edge)