N = int(input())
K = int(input())

apples = []
board = [[ 0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1
    apples.append([row, col])

# R, D, L, U (시계방향 움직임)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

L = int(input())
moves = []
for _ in range(L):
    X, C = input().split()
    moves.append([int(X), C])

idx = 0


sh_row, sh_col = 0, 0
board[sh_row][sh_col] = 1
while True:
    d = directions[idx]
    nsh_row, nsh_col = sh_row + d[0], sh_col + d[1]
    board[nsh_row][nsh_col] = 1
    

    