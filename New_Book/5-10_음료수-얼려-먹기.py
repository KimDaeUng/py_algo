# 00:52-
'''
'0'인 값이 상, 하, 좌, 우로 연결되어 있는 노드를 묶으며, 묶음의 개수를 찾아주는 프로그램 작성하기

1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
3. 1 ~ 2 번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 개수를 센다.
   ('0'인 덩어리의 최초 방문 노드만 카운트하게 됨)
'''

N, M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우, 즉시 종료
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if board[x][y] == 0:
        # 방문처리
        board[x][y] = 1
        # 상, 하, 좌, 우 재귀호출로 방문
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    # 방문했다면
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)