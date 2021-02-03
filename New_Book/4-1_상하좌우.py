# My Solution
n = int(input())
data = list(input().split())

direction = {"L" : (0, -1),
             "R" : (0, 1),
             "U" : (-1, 0),
             "D" : (1, 0)}

cur_y, cur_x = 1, 1
move = [0, 0]
for i, d in enumerate(data):
    print("trial : {} : {}, {}".format(i, cur_y, cur_x))
    y, x = direction[d]
    
    move_y, move_x = cur_y + y, cur_x + x
    # 지도 밖을 벗어나면 무시
    if (move_x < 1) or (move_y < 1) \
        or (move_x > n) or (move_y > n):
        continue
    else:
        cur_y, cur_x = move_y, move_x

print(cur_y, cur_x)

# Solution
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)