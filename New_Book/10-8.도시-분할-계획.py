# https://www.acmicpc.net/problem/1647
# 19:20-20:34 못 품
# 19:00-21:50
# 00:30-01:57
# My Solution
'''
전제 MST를 구한 뒤, 비용이 가장 큰 노드를 잘라내어 두 개의 MST로 분할
시간초과 이슈 해결방안
- weighted union으로 depth 줄이기
- 간선정보 입력시 왕복으로 받지 않아도 문제가 요구하는 해에 영향 없음
  (양방향 X, 단방향으로만 입력)
- input = sys.stdin.readline
- ref : https://ziegler.tistory.com/101
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

# Kruskal
import sys
# input = sys.stdin.readline
def f_parent(parent, x):
    if parent[x] != x:
        parent[x] = f_parent(parent, parent[x])
    return parent[x]

def weighted_union_p(parent, size_list, a, b):
    x = f_parent(parent, a)
    y = f_parent(parent, b)
    # 자식노드수(size)가 더 작은 노드(트리)가 더 큰 노드(트리)의 아래로 가면
    # 트리가 세로로 길어지는 것을 방지할 수 있다.
    if size_list[x] > size_list[y]:
        parent[y] = x
        size_list[x] += size_list[y]
    else:
        parent[x] = y
        size_list[y] += size_list[x]

# def u_parent(parent, a, b):
#     a = f_parent(parent, a)
#     b = f_parent(parent, b)
#     if a < b:
#         parent[a] = b
#     else:
#         parent[b] = a

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
size_list = [1] * (n+1)
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    # edges.append((cost, b, a))

edges.sort()

total_cost = 0
max_edge_cost = 0
for edge in edges:
    c, a, b = edge
    if f_parent(parent, a) != f_parent(parent, b):
        weighted_union_p(parent, size_list, a, b)
        total_cost += c
        max_edge_cost = c # 가장 마지막에 할당된 cost가 최대 cost
print(total_cost - max_edge_cost)


# Solution
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
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
# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i 

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 ㅇ낳는 경우에만 집합에 퐇마
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)