# https://www.acmicpc.net/problem/2252
# 15:42-16:26


string = '''3 2
1 3
2 3'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution
'''
줄 세우기 -> 순위 -> 위상정렬
답이 여러 가지인 경우 아무거나 출력 -> 순위가 하나로 결정되지 않아도됨
사이클이 생기는 경우는 주어지지 않는가?
'''
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
# 순위가 높은 학생 -> 낮은 학생의 방향그래프
# result 리스트에 순위가 낮은 학생부터 높은 학생 순으로 쌓임

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque([])
result = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result.append(now)

    for next_node in graph[now]:
        if indegree[next_node]:
            indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

for i in result:
    print(i, end=' ')