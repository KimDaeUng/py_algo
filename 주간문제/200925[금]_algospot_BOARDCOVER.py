# https://www.algospot.com/judge/problem/read/BOARDCOVER#

# 최초 시도
# 실패요인
# 탐색 알고리즘을 무엇을 쓸지 불명확
# 탐색을 위한 재귀코드 작성시 구체적인 종료조건이나 예외처리 고려 미흡

import sys

C = int(sys.stdin.readline())

def move(h, w, grid):
    p2 = [(h+1, w-1), (h, w-1), (h-1, w), (h, w+1)]
    p3 = [(h+1, w), (h+1, w-1), (h-1, w+1), (h+1, w+1)]
    for p_2, p_3 in zip(p2, p3):
        center = grid[h][w]
        point1 = grid[p_2[0]][p_2[1]]
        point1 = grid[p_3[0]][p_3[1]]
        try:
            if center == False \
                & point1 == False \
                & point2 == False:
            grid[h][w], grid[p_2[0]][p_2[1]], grid[p_3[0]][p_3[1]] = True, True, True

        except:
            
# Solution
# https://hellominchan.tistory.com/263
import sys

def DFS():
    global ans
    i, j = -1, -1
    isFinish = True
    
    # Find the coordinate where pointer have not visited
    for x in range(H):
        for y in range(W):
            if not visit[x][y]:
                isFinish = False
                i, j = x, y
                break
        if not isFinish:
            break
    
    # if finished, return ans
    if isFinish:
        ans += 1
        return
    
    # if not finished, 
    if not visit[i][j]:
        # Search the all rotations
        for rotate in range(4):
            isPossible = True
            possibleDirection = []
            
            for way in range(3):
                ii = i + dx[rotate][way]
                jj = j + dy[rotate][way]

                # Check whether the index will be out of range or not.
                if ii < 0 or ii > H - 1 or jj < 0 or jj > W - 1:
                    isPossible = False
                    break
                
                # Check whether the index pass the black block
                if visit[ii][jj]:
                    isPossible = False
                    break
                
                possibleDirection.append((ii, jj))
            
            if isPossible:
                for pDX, pDY in possibleDirection:
                    visit[pDX][pDY] = True

                DFS()
                
                # For the next iteration, initialize the grid
                for pDX, pDY in possibleDirection:
                    visit[pDX][pDY] = False


C = int(sys.stdin.readline())
dx = [(0, 1, 1), (0, 1, 0), (0, 1, 1), (0, 0, 1)]
dy = [(0, 0, -1), (0, 0, 1), (0, 0, 1), (0, 1, 1)]

for _ in range(C):
    ans = 0
    H, W = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(H)]

    visit = [[False] * W for _ in range(H)]
    whiteSection = 0

    for i in range(H):
        for j in range(W):
            if board[i][j] == "#":
                visit[i][j] = True
            else:
                whiteSection += 1

    # If we can't fill the white section by this condition,
    # return 0 and skip to next case
    if whiteSection % 3:
        print(0)
        continue

    DFS()

    print(ans)