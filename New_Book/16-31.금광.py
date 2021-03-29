# 19:35-20:34
# My Solution
# - 처리하기 쉽게 시계방향 90도로 돌리고 시작함
# - DP array를 만들고, 각 위치에 가능한 경우 중 최대값을 계속 기록
# - DP[r][c] = max(DP[r-1][c + dc] + A[r][c])
# where dc = [-1, 0, 1], 단, 0 <= dc + c <= n
# - 마지막 행의 최대값을 출력

def rotate_a_mtx_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)] # 결과 리스트
    # Transpose 후에 각 열의 원소를 뒤집는 것
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# column의 이동
diff = [-1, 0, 1]

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())
    case = list(map(int, input().split()))
    data = [ [0] * m for _ in range(n) ]
    
    for i, e in enumerate(case):
        row = i // m
        col = i % m
        data[row][col] = e

    rotate_90 = rotate_a_mtx_by_90_degree(data)
    dp = [ [0] * n for _ in range(m)]
    dp[0] = rotate_90[0]

    for r in range(1, m):
        cur_row = rotate_90[r]
        for c, cur_rc_value in enumerate(cur_row):
            max_value = 0
            max_idx = 0
            # 직전 행에서 가능한 계산 범위에 대해 모두 계산하며 최대값을 갱신
            for d in diff:
                prev_c = c + d
                # 범위가 벗어나는 경우는 제외
                if 0 <= prev_c and prev_c < n:
                    cur_sum = dp[r-1][prev_c] + cur_rc_value
                    dp[r][c] = max(dp[r][c], cur_sum)

    print(max(dp[m-1]))


# Solution
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)