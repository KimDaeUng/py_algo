# https://www.acmicpc.net/problem/6497
# Online Judge 코드 작동 방식이 기존과 조금 다름(아래 코드 참고)
# 13:45-14:20
# My Solution
'''
간선의 비용 합이 최소가 되도록하는 MST를 구하는 문제
-> Kruskal
'''
string = '''7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
0 0'''

# string = '''2 1
# 1 2'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import sys
input = sys.stdin.readline

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    parent = list(range(m + 1))

    edges = []
    total_cost = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        total_cost += c

    edges.sort()

    min_cost = 0
    for edge in edges:
        cost, a, b = edge
        if find_p(parent, a) != find_p(parent, b):
            union_p(parent, a, b)
            min_cost += cost
    print(total_cost - min_cost)

# Solution (동빈북 문제 기준)
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

m, n = map(int, input().split())
parent = [0] * (n + 1)

# 모든 간선을 담을 리스트와 최종 비용 담을 변수
edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()
total = 0 # 전체 가로등 비용

for edge in edges:
    cost, a, b = edge
    total += cost
    # 사이클이 발생하지 않는 경우만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(total - result)