# https://www.acmicpc.net/problem/1865
# 13:20-14:50
# 14:50-15:25 : 해설 보고 다시 풀이
# My Solution
'''
도로 : 양방향 경로
웜홀 : 방향이 있는 경로, 음의 가중치
한 지점에서 출발하여 시간여행을 하여 출발위치로 돌아왔을때, 시간이 되돌아가 있는 경우가 있는지?
-> 전체 그래프에서 음의 사이클이 존재하는지

벨만 포드로 풀이

# 조건
- 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다
-> 어차피 벨만포드 수행 과정에서 걸러짐

# 단순 벨만포드로 풀리지 않음
양의 간선 정보와 음의 간선 정보를 따로 준 이유가 있나?
!!! -> 양방향 그래프 간선 정보 입력을 잘못함(한 쪽만 입력)

'''
string = '''2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import sys
input = sys.stdin.readline
INF = int(1e9)

def bmf(n, m, w, edges):
    dist = [INF] * (n + 1)
    dist[1] = 0 # 임의의 시작지점, 음의 사이클 여부만 판단하면 되므로
    for i in range(n):
        for j in range(2 * m + w):
            cur, next_node, cost = edges[j]
            if dist != INF and dist[cur] + cost < dist[next_node]:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:
                    return "YES"
    return "NO"

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    print(bmf(n, m, w, edges))