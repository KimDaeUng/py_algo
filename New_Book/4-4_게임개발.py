# 21:44-22:52 # 해결 못함

print(m_world)
n, m = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))

world = []
m_world = [[ 0 for i in range(m) ] for j in range(n)]
m_world[n][m] = 1

for i in range(n):
    world.append(list(map(int, input().split())))

# world[y][x]

# 캐릭터는 왼쪽 방향으로 계속 회전함
# 북, 서, 남, 동 , 반시계방향
directions = [ 0, 3, 2, 1]
start_idx = directions.index(d)

directions = directions[start_idx:] + directions[:start_idx]

forward_steps = [(-1, 0), (0, -1), (1,  0), (0, 1)]
backward_steps  = [ (1, 0), (0,  1), (-1, 0), (0,-1)]
while True:
    # 4방향 모두 탐색
    m_directions = [0, 0, 0, 0]
    for idx in range(4):
        # 왼쪽으로 회전
        d = directions[idx]
        step = forward_steps[idx]
        ny, nx = a + forward_steps[0], b + forward_steps[1]
        # 왼쪽 방향이 육지이고, 가보지 않은 칸이라면
        if matrix[ny][nx] == 0:
            if m_world[ny][nx] == 0:
                # 왼쪽으로 한 칸 전진
                a, b = ny, nx
            # 가본 칸이면
            else:
                # 왼쪽 방향으로 회전만 수행하고(이미 처리) 1단계로 back
                # 이 때 4방향 모두 가보았는지 기록
                m_directions[idx] = 1

    # 네 방향 모두 이미 가본 칸 또는 바다인 경우,
    # 한 칸 뒤로 가고 1단계로 돌아감
    ny, nx = a + backward_steps[0], b + backward_steps[1]
    if (matrix[ny][nx] == 1) or sum(m_directions)==4:
        
            

            
    