# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

'''
자물쇠 - 홈
열쇠 - 홈과 돌기
열쇠는 회전과 이동이 가능
열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 열리는 구조

자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만

자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며

열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.

또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,

열쇠로 자물쇠를 열수 있으면 true, 없으면 false를 return

'''

# Retry

def rotate(a):
    n = len(a)
    m = len(a[0])

    result = [ [0] * m for i in range(n) ]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = a[i][j]
    return result

def check(n, lock_pad):
    '''자물쇠에 모든 값이 채워져 있는지 확인'''
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if lock_pad[i][j] != 1:
                return False
    return True

def solution(key, lock):

    m = len(key)
    n = len(lock)

    # 패딩된 lock
    n_pad = 3*n
    lock_pad = [ [0] * n_pad for _ in range(n_pad) ]
    # 기존값 복사
    for i in range(n):
        for j in range(n):
            lock_pad[i + n][j + n] = lock[i][j]
    
    # 완전 탐색
    for i in range(4):
        key = rotate(key)
        for i in range(2 * n):
            for j in range(2 * n):
                # 현재 위치에서 Key를 끼워넣어보기
                for i_key in range(m):
                    for j_key in range(m):
                        lock_pad[i + i_key][j + j_key] += key[i_key][j_key]
                # 검사
                if check(n, lock_pad):
                    return True
                # 초기화
                for i_key in range(m):
                    for j_key in range(m):
                        lock_pad[i + i_key][j + j_key] -= key[i_key][j_key]
    
    return False
    
            
key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))


# Solution
# 18:54-19:37 : solution 이해 후 복기까지

'''
- 패딩된 배열의 크기를 줄인다고 리스트 인덱스를 복잡하게 만드는 것 보다
  조금 더 메모리를 쓰더라도 알아보기 쉬운 코드 짜는 것이 더 낫다.

'''
def rotate_a_mtx_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)] # 결과 리스트
    # Transpose 후에 각 열의 원소를 뒤집는 것
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return False

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존에 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠 중앙 부분에 기존 자물쇠 값 복사
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_mtx_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 체크
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

########


# My Soltuion(Failed)
# import copy

# def solution(key, lock):
#     M, N = len(key), len(lock)
#     key = [key]

#     # M x M 배열 생성
#     # 회전한 숫자를 결과에 저장할 때, 저장할 곳을 생성하는 것

#     def init(M):
#         res = []
#         for m in range(M):
#             temp = []
#             for n in range(M):
#                 temp.append(0)
#             res.append(temp)
#         return res

#     def check(key, padded_locK):
#         T = len(padded_lock)
#         M = len(key)
#         # gap은 어떻게 겹칠지를 의미함
#         # padded_lock의 (0,0)에서 key를 얼마나 shift 시킬지에 대한 값 
#         for gap1 in range(T - M + 1):
#             for gap2 in range(T - M + 1):
#                 res = True
#                 cnd_padded_lock = copy.deepcopy(padded_lock)
#                 for p in range(M):
#                     for q in range(M):
#                         cnd_padded_lock[p + gap1][q + gap2] += key[p][q]
#                 check_area = []
#                 for p in range(M-1, T - M + 1):
#                     temp = []
#                     for q in range(M - 1, T - M + 1):
#                         temp.append(cnd_padded_lock[p][q])
#                 check_area.append(temp)
            
#             for p in range(len(check_area)):
#                 for q in range(len(check_area)):
#                     if check_area[p][q] != 1:
#                         res = False
#                         break
#                 if res == False:
#                     break
            
#             if res == True:
#                 return res

#         return False
        

#     # Key 후보 다 뽑기(90도 회전 후보)
#     '''
#     90도 회전시
#     (0, 0), (0, 1), (0, 2), ..., (0, M-1)
#     =>
#     (0, M-1), (1, M-1), (2, M-1), ..., (M-1, M-1) 
#     # matrix의 두 번째 줄의 회전
#     (1, 1), (1, 2), ..., (1, M-2)
#     => 90도
#     (1, M-2), (2, M-2), ..., (M-2, M-2)
#     => 90도
#     (M-2, M-2), (M-2, M-3), ..., (M-2, 1)
#     (p, q) -> (q, M-1-p)

#     '''

#     for i in range(3):
#         new_key = init(M)
#         for p in range(M):
#             for q in range(M):
#                 # 직전 key에서 90도를 돌리는 것이기 때문에 -1 인덱스
#                 new_key[q][M - 1 - p] = key[-1][p][q]
#         key.append(new_key)
    
#     # N x N 타일을 M x M 타일 위에 window sliding 하기 위해
#     def padding(lock, N, M):
#         T = N * 2 * (M - 1)
#         padded_lock = init(T)

#         # padded_lock 내의 원래 lock의 값을 복사
#         for i in range(N):
#             for j in range(N):
#                 padded_lock[i + M - 1][j + M - 1] = lock[i][j]
        
#         return padded_lock
        
#     padded_lock = padding(lock, N, M)
    
#     # 모두 1로 채워지는지 check
#     answer = False
#     for i in range(4):
#         candidate_key = key[i]
#         if check(candidate_key, padded_lock) == True:
#             return True


#     return answer


# Retry
# 21:00-
# 17:40-18:54 : 일부 케이스만 통과.
'''
어떻게 풀까?
가능한 모든 경우를 찾아본다.
Lock에 패딩을 주고, 계속해서 회전 & 쉬프팅해가며 모든 칸이 채워지는 경우를 찾는다.

# 구조
자물쇠의 가로 세로길이를 N이라 하고
N_pad = 2 * (N - 1) + N라 하자
1. for : 모든 회전 경우 (0, 90, 180, 270)
    2. for : N_pad x N_pad 상에서 Key를 쉬프팅해가며
    Lock의 범위 내에 있는 값들이 모두 1인지 확인,
    Key와 Lock의 돌기가 겹치면 실패처리
'''
# import copy
# import pprint
# def solution(key, lock):
#     M, N = len(key), len(lock)
#     N_pad = 2 * (M - 1) + N 
    
#     # 패딩된 lock 생성
#     lock_hole = 0
#     lock_pad = [ [ 0 for _ in range(N_pad)] for _ in range(N_pad) ]

#     # 기존 lock 값을 복사
#     for r in range(M - 1 , M - 1 + N):
#         for c in range(M - 1, M - 1 + N):
#             lock_pad[r][c] = lock[r - (M - 1)][c - (M - 1)]
#             # 홀의 개수 카운트
#             if lock[r - (M - 1)][c - (M - 1)] == 0:
#                 lock_hole += 1
    
#     # pprint.pprint(lock_pad)
#     # 90도 회전
#     def rotate(array):
#         return list(zip(*array[::-1]))
    
#     def check(key, lock_pad, r, c):
#         # (r, c)를 좌상단으로 하는 key의 모든 값을 조사
#         count = 0
#         for i in range(r, r + M):
#             for j in range(c, c + M):
#                 # 현재 조사 범위가 자물쇠 안이면, key와 비교해서, 값을 채움
#                 if (0 <= i < N_pad) and (0 <= j < N_pad):
#                     if key[i - r][j - c] == 1 and lock_pad[i][j] == 0:
#                         count += 1
#                         if lock_hole == count:
#                             return True
#                     # key의 돌기가 잘못 lock의 돌기에 닿는 경우
#                     # if key[i - r][j - c] == 1 and lock_pad[i][j] == 1:
#                     #     return False
#                     # # # key의 홀
#                     # if key[i - r][j - c] == 0 and lock_pad[i][j] == 0:
#                     #     return False
                
#         return False
#     # print(lock_hole, "###")
#     for i in range(4):
#         # print(i)
#         key = rotate(key)
#         # pprint.pprint(key)
#         # pprint.pprint(lock_pad)
#         # Key의 좌상단 기준으로 쉬프팅
#         for r in range(0, N + M - 1):
#             for c in range(0, N + M - 1):
#                 if check(key, lock_pad, r, c):
#                     return True
#     return False