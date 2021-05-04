# https://programmers.co.kr/learn/courses/30/lessons/49191
# 15:32-16:10
'''
문제 예시 입력
각 번호에 해당하는 학생들의 대소 관계가 다음과 같이 주어짐

1 < 5
3 < 4
4 < 2
4 < 6
5 < 2
5 < 4

1 < 5 < 4 < 2
   3    |  6

# 위에서 4번 학생은 순위를 정확히 알 수 있으나 나머지는 알 수 없음
학생 성적을 비교한 결과가 주어질 때 성적 순위를 정확히 알 수 있는 학생은 몇 명인가?

# 입력 조건
- 학생 수 2 <= N <= 500
- 성적 비교 횟수 2 <= M <= 10,000

# 출력
성적 순위를 정확히 알 수 있는 학생의 수

# 접근
- N 수가 적다
- 모든 노드에 대해서 떨어진 거리가 필요
-> Floyd-worshall
# 행렬을 구한 뒤, 행과 열 모두에서 자기 자신을 제외한 모든 선수에 대해
# 적어도 한 번씩은 대전을 치뤘으면 순위 결정 가능

'''
string = '''6 6
1 5
3 4
4 2
4 6
5 2
5 4'''

# string = '''5 5
# 4 3
# 4 2
# 3 2
# 1 2
# 2 5'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

import pprint

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에 대한 거리는 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    # a 학생의 성적이 b 학생보다 낮다
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

graph2 = [[0] * n for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != INF:
            graph2[i-1][j-1] = graph[i][j]
        else:
            graph2[i-1][j-1] = 0

count = 0
for i, col in enumerate(zip(*graph2)):
    is_rankable = True
    for j, (r, c) in enumerate(zip(graph2[i], col)):
        if r == 0 and c == 0 and i != j:
            is_rankable = False
            break
    if is_rankable:
        count += 1

print(count)

# # My Solution(Programmers)
INF = int(1e9)
def solution(n, results):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    # 자기 자신에 대한 거리는 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for i in results:
        a, b = i
        # a 학생의 성적이 b 학생보다 낮다
        graph[a][b] = 1
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    graph2 = [[0] * n for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] != INF:
                graph2[i-1][j-1] = graph[i][j]
            else:
                graph2[i-1][j-1] = 0

    answer = 0
    for i, col in enumerate(zip(*graph2)):
        is_rankable = True
        for j, (r, c) in enumerate(zip(graph2[i], col)):
            if r == 0 and c == 0 and i != j:
                is_rankable = False
                break
        if is_rankable:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

n = 1
results = []
print(solution(n, results))

# defaultdict와 set을 이용한 풀이 : O(N^2)
from collections import defaultdict
def solutiont(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    # 대전 결과 반영
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])
    # 대전 결과에 딸린 상대적 정보 반영
    # (a가 b에 승리, b가 c에 승리 -> a는 c에 승리)
    for i in range(1, n + 1):
        # i한테 이긴 선수는 i가 이긴 다른 선수들에게 모두 이긴다
        for winner in lose[i]:
            win[winner].update[win[i]]
        # i한테 진 선수들은 i가 진 다른 선수들에게 모두 진다
        for loser in win[i]:
            lose[loser].update[lose[i]]

    # 이긴 횟수와 진 횟수를 모두 합한 길이가
    # n - 1(자기 자신을 제외한 선수의 수)이 될 때
    # 순위 결정가능
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer

# Solution
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신 비용은 1로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 1 # 0이어도 결과에 무관함

# 각 간선 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 전화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하여 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(graph)
print(result)