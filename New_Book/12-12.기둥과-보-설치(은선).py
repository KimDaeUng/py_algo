# Eunseon Solution
def solution(n, build_frame):
    board = [[0] * (n + 1) for _ in range(n+1)]
    # 기둥 = 1, 보 = 2
    def has_col(r, c):
        return (board[r][c] == 1) #or (board[r][c] == 3)
    def has_bo(r, c):
        return (board[r][c] == 2) #or (board[r][c] == 3)
    
    # 기둥 설치 조건 체크
    def check_col_install(r, c):
        # 1) 바닥위
        if r == n: return True
        # 3) 다른 기둥 위
        # (r < n == n-y < n == 0 < y )
        if r < n and has_col(r + 1, c): return True
        # 2) 보의 한쪽 끝 부분 위(왼쪽, 오른쪽)
        if c > 0 and has_bo(r, c - 1): return True
        if has_bo(r, c): return True
        return False
    
    # 보 설치 조건 체크
    def check_bo_install(r, c):
        # 1) 한쪽 끝이 기둥 위(왼, 오)
        if r < n and has_col(r + 1, c): return True
        if r < n and has_col(r + 1, c + 1): return True
        # 2) 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는지
        if c > 0 and c < n and\
            has_bo(r, c - 1) and has_bo(r, c + 1):
            return True
        return False

    # 구조물 타당성 체크
    def check_valid():
        for r in range(n + 1):
            for c in range(n + 1):
                # 설치할 수 없는 곳에 각 구조물이 있는 경우
                if has_bo(r, c) and not check_bo_install(r, c):
                    return False
                if has_col(r, c) and not check_col_install(r, c):
                    return False
        return True
    
# 시뮬레이션
    for work in build_frame:
        x, y, stuff, process = work
        r, c = n-y, x

        # 보
        if stuff == 1:
            # 설치
            if process == 1:
                # 설치 가능한지 체크
                if check_bo_install(r, c):
                    board[r][c] += 2
            # 삭제
            else:
                board[r][c] -= 2
                # 지운 구조물의 타당성 평가
                if not check_valid():
                    board[r][c] += 2
        # 기둥
        else:
            # 설치
            if process == 1:
                # 설치 가능한지 체크
                if check_col_install(r, c):
                    board[r][c] += 1
            # 삭제
            else:
                board[r][c] -= 1
                # 지운 구조물의 타당성 평가
                if not check_valid():
                    board[r][c] += 1
    
    # 출력
    ret = []
    for c in range(n + 1):
        x = c
        for r in reversed(range(n + 1)):
            y = n - r
            if has_col(r, c):
                ret.append([x, y , 0])
            if has_bo(r, c):
                ret.append([x, y, 1])
    return ret

n = 5
build_frames = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(n, build_frames))
