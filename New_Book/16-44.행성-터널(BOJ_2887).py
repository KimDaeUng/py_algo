# https://www.acmicpc.net/problem/2887
# 16:50-18:30, 20:30-21:40 : 해결 못함

'''
터널을 N - 1개 연결해서 모든 행성이 연결되도록 한다 -> Tree의 특징
모든 행성을 연결하는데 필요한 '최소 비용' -> MST
-> Kruskal

노드의 좌표만 주어짐, 각 노드 간 거리를 구하는 방법 고민

'''

string = '''5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution 2 : Retry
import sys
input = sys.stdin.readline
def fp(p, x):
    if p[x] != x:
        p[x] = fp(p, p[x])
    return p[x]

def up(p, a, b):
    a = fp(p, a)
    b = fp(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n = int(input())

nodes = []
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z, i))

edges = []
for i in range(3):
    nodes.sort(key=lambda x : x[i])
    for j in range(n - 1):
        edges.append((nodes[j + 1][i] - nodes[j][i],
                      nodes[j + 1][3], nodes[j][3]))

parent = list(range(n))

result = 0
edges.sort()
for edge in edges:
    c, a, b = edge
    if fp(parent, a) != fp(parent, b):
        up(parent, a, b)
        result += c
print(result)

# My Solutioni 1
def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]

def union_p(p, a, b):
    a = find_p(p, a)
    b = find_p(p, b)
    if a > b:
        p[a] = b
    else:
        p[b] = a

n = int(input())
nodes = []
for i in range(n):
    xyz = tuple(map(int, input().split()))
    nodes.append((xyz, i))

edges = []
for k in range(3):
    nodes.sort(key=lambda x: x[0][k])
    for i, j in zip(nodes[:-1], nodes[1:]):
        print(i, j)
        idx_i, idx_j = i[1], j[1]
        print(idx_i, idx_j)
        i, j = i[0], j[0]
        c = tuple(map(lambda x, y : abs(x - y), i, j))[k]
        edges.append((c, idx_i, idx_j))

parents = list(range(n))
edges.sort()
total_cost = 0
for edge in edges:
    cost, a, b = edge
    print(edge)
    if find_p(parents, a) != find_p(parents, b):
        union_p(parents, a, b)
        total_cost += cost
print(total_cost)

##################
# Solution
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

x, y, z = [], [], []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append(x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1])
    edges.append(y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1])
    edges.append(z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1])

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)