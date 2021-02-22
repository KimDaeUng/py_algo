# https://programmers.co.kr/learn/courses/30/lessons/60061
# 02:20-
'''
# 각 셀 안에 보와 기둥에 해당하는 값으로 채우기

1. 작업 수행시 조건 충족 확인
- 기둥:
  1) 바닥위인지
  2) 보의 한쪽 끝 부분 위인지
  3) 기둥 위인지
- 보:
  1) 한쪽 끝이 기둥 위에 있는지
  2) 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는지

# 처음에 틀렸던 이유
- 제거의 경우 작업 수행 전에 조건을 확인하는 것이 무의미함. 제거한 작업을 수행 후 타당한지 확인하고
  아닌 경우 다시 뒤로 돌리는 것이 필요
- 기둥과 보가 한 좌표 상에 겹칠 수 있는 경우를 생각 못함 (보의 왼쪽 끝 위에 기둥이 있는 경우)
- 제거시 해당 구조가 타당한지를 설치시 타당성 검사 했던 그대로 적용하려함 : 있어야할 곳에 있는지를 체크해야
- 제거작업을 수행한 주변만 체크 -> 일부 케이스 실패
'''
# Eunseon Solution : 구조물을 배열에 기록하는 방식
def solution(n, build_frame):
    # wall
    wall = [[ 0 for _ in range(n+1)] for _ in range(n+1)]

    # 기둥 = 1, 보 = 2
    def has_col(r, c):
        return (wall[r][c] == 1) or (wall[r][c] == 3)
    def has_bo(r, c):
        return (wall[r][c] == 2) or (wall[r][c] == 3)
    
    # 기둥 설치 조건 체크
    def ck_col_install(r, c):
        # 1) 바닥 위
        if r == n: return True
        # 2) 보의 한쪽 끝 부분 위
        if c > 0 and has_bo(r, c - 1): return True
        if has_bo(r, c): return True
        # 3) 다른 기둥 위
        if r < n and has_col(r + 1, c): return True
        return False

    # 보 설치 조건 체크
    def ck_bo_install(r, c):
        # 1) 한쪽 끝이 기둥 위
        if r < n and has_col(r + 1, c): return True
        if r < n and has_col(r + 1, c + 1): return True
        # 2) 양쪽 끝 부분이 다른 보와 동시에 연결
        if c > 0 and c < n and\
            has_bo(r, c - 1) and has_bo(r, c + 1):
            return True
        return False

    def ck_valid():
        for r in range(n + 1):
            for c in range(n + 1):
                # 설치 불가능한 곳에 각 구조물이 있는 경우
                if has_bo(r, c) and not ck_bo_install(r, c):
                    return False
                if has_col(r, c) and not ck_col_install(r, c):
                    return False
        return True

    # 탐색범위 줄여보려했으나 일부 테스트 케이스에서 실패, 전체 탐색 필요 
    # def ck_valid2(r, c):
    #     # 설치 불가능한 곳에 각 구조물이 있는 경우
    #     dx = [0, -1, 1, 0, 0, 1, 1, -1, -1]
    #     dy = [0,  0, 0,-1, 1, 1, -1, 1, -1]
    #     for i in range(5):
    #         nc = c + dx[i]
    #         nr = r + dy[i]
    #         # 공간 벗어난 경우 무시
    #         if nc < 0 or nr < 0 or nc > n or nr > n:
    #             continue
    #         if has_bo(nr, nc) and not ck_bo_install(nr, nc):
    #             return False
    #         if has_col(nr, nc) and not ck_col_install(nr, nc):
    #             return False
    #     return True

    # 시뮬레이션
    for work in build_frame:
        x, y, stuff, process = work
        r, c = n - y, x

        # 보
        if stuff == 1:
            # 설치
            if process == 1:
                if ck_bo_install(r, c):
                    wall[r][c] += 2 
            # 삭제
            else:
                wall[r][c] -= 2
                # 전체를 다 확인? or 현재 지점만 확인?
                if not ck_valid():
                    wall[r][c] += 2
        # 기둥
        else:
            # 설치
            if process == 1:
                if ck_col_install(r, c):
                    wall[r][c] += 1
            else:
                wall[r][c] -= 1
                if not ck_valid():
                    wall[r][c] += 1
    
    # 출력
    ret = []
    for c in range(n + 1):
        x = c
        for r in range(n, -1, -1):
            y = n - r
            if has_col(r, c):
                ret.append([x, y, 0])
            if has_bo(r, c):
                ret.append([x, y, 1])

    return ret


# Main Solution : 각 작업 마다 타당한지를 확인하여 타당한 작업만 남겨 출력하는 방식
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or\
                [x - 1, y, 1] in answer or\
                [x, y, 1] in answer or\
                [x, y - 1, 0] in answer:
                continue
            return False # 아닐 경우 거짓 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or\
                [x + 1, y - 1, 0] in answer or\
                ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아닐 경우 거짓 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치 후에
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)

n = 5
build_frames = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n, build_frames))


# My Solution (Failed)
'''
    def _is_valid():
        # 전체를 돌면서 기둥과 보의 타당성 체크
        for y in range(N+1):
            for x in range(N+1):
                # 0 : 빈칸 / 2 : 기둥 / 1 : 보
                # 현재 위치에 기둥이 있을 경우(기둥만 있거나 기둥과 보가 함께 있거나)
                if (wall[y][x] == 2) or (wall[y][x] == 3):
                    # !!! : 기둥과 보가 같은 칸에 겹칠 수 있음 이에따라 코드 수정 필요
                    # 1) 바닥위
                    if y == n: continue
                    # 2) 보의 한쪽 끝 부분 위
                    if wall[y][x] == 3: continue # 기둥의 오른쪽(같은 좌표에 기둥과 보가 겹치는 경우)
                    if (x > 0) and ((wall[y][x - 1] == 1) or (wall[y][x - 1] == 3)): continue # 기둥의 왼쪽
                    # 3) 다른 기둥 위
                    if (y > 0) and ((wall[y-1][x] == 1) or (wall[y-1][x] == 3)): continue
                    # 위의 정상 조건에 해당되지 않는 경우
                    return False
                # 현재 위치에 보가 있을 경우
                if wall[y][x] == 1 or (wall[y][x] == 3):
                    # 1) 한쪽 끝이 기둥 위
                    if (y > 0) and ((wall[y-1][x] == 2) or (wall[y-1][x] == 3)): continue # 보의 왼쪽 끝
                    if (y > 0) and ((wall[y-1][x+1] == 2) or (wall[y-1][x+1] == 3)): continue # 보의 오른쪽 끝
                    # 2) 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는지
                    if (x > 0) and (x < N) and\
                        ((wall[y][x-1] == 1) or (wall[y][x-1] == 3)) and\
                        ((wall[y][x+1] == 1) or (wall[y][x+1] == 3)):
                        continue
                    return False
        return True


    def _pr(wall, x, y, how, what):
        # 설치
        if how == 1:
            wall[y][x] = what
        # 제거
        else:
            # 제거 후에 구조물이 타당한가를 확인하고
            # 아니라면 제거를 취소해야함
            # 1. 일단 제거
            # 기둥 제거
            if what == 0:
                wall[y][x] -= 2
            # 보 제거
            elif what == 1:
                wall[y][x] -= 1

            # 2. 타당성 확인
            if not _is_valid():
                # 복구
                if what == 0:
                    wall[y][x] += 2
                elif what == 1:
                    wall[y][x] += 1

    # building process
    for process in build_frame:
        x, y, what, how = process
        if what == 0:
            # 조건 체크
            if y == 0 or \
            ((x - 1 > 0) and (wall[y][x-1] == 1)) or\
            (wall[y][x] == 1) or\
            ((y - 1 > 0) and (wall[y-1][x] == 0)):
                # 설치 또는 제거
                _pr(wall, x, y, how, what)
        # 보 설치
        else:
            # 설치 조건 체크
            if ((y - 1 > 0) and (wall[y-1][x] == 0)) or\
            ((y - 1 > 0) and (x + 1 < n) and (wall[y-1][x+1] == 0)) or\
            (((x - 1 > 0) and wall[y][x-1] == 1) and ((x + 1 < n) and wall[y][x+1] == 1)):
                # 설치 또는 제거
                _pr(wall, x, y, how, what)
    
    pprint.pprint(wall)

    # return값 생성
    answer = []
    for x in range(n):
        for y in range(n):
            # 빈 칸이 아닌 경우에
            if wall[y][x] != -1:
                answer.append([x+1, y+1, wall[y][x]])

    return sorted(answer, key=lambda x : (x[0], x[1], x[2]))
'''
