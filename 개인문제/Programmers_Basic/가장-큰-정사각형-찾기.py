# https://programmers.co.kr/learn/courses/30/lessons/12905
# 12:00-13:00 

# My Solution2: Retry: DP
# ref: https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp
def solution(board):
    n = len(board)
    m = len(board[0])
    
    dp = [ [0] * m for _ in range(n) ] 
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]
    
    # Base case
    if n == 1 or m == 1:
        return 1
    
    answer = 0
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                answer = max(answer, board[i][j])
    
    return answer ** 2

# My Solution: Fail
def solution(board):
    n = len(board)
    def get_colwise_max_range(board, n):
        global_max_s = 0
        global_min_e = 0
        for i in range(n):
            max_cnt = 0
            cnt = 0
            s = 0
            e = 0
            max_s = 0
            min_e = n + 1
            for j in range(n):
                if board[i][j]:
                    cnt += 1
                    if cnt == 0:
                        s = j

                else:
                    if max_cnt < cnt:
                        max_cnt = cnt
                        e = i - 1
                        max_s = max(max_s, s)
                        min_e = min(min_e, e)
                    cnt = 0

            global_max_s = max(max_s, global_max_s)
            global_min_e = min(min_e, global_min_e)
        return global_max_s, global_min_e
    
    row_range = get_colwise_max_range(board, n)
    col_range = get_colwise_max_range([ i for i in zip(*board)], n)
    return (abs((max(row_range[0], col_range[0]) - min(row_range[1], col_range[1]))) + 1) ** 2

'''
행, 열의 마진합을 배열로 구한 뒤
두 배열의 모든 원소의 최대값에서 부터 1씩 감소하면서
세로가로
  2 3 4 3
2 0 1 1 0
4 1 1 1 1
4 1 1 1 1 
2 0 0 1 1

가장 긴 연속된 시작인덱스와 끝 인덱스 구하기

# 세로가로 (1, 2) (0, 2), (0, 4), (1, 4) -> (1, 2) #(최대값, 최소값)
(1, 2)     
(0, 4)
(0, 4)
(2, 4)

# *최대값, 최소값)
(1, 2)

행, 열 각각에 대해서 구한 것들을 다시 (둘 중 최대, 둘 중 최소값) 구한 뒤 두 인덱스의 거리의 제곱
'''
