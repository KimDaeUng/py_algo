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

import copy

def solution(key, lock):
    M, N = len(key), len(lock)
    key = [key]

    # M x M 배열 생성
    # 회전한 숫자를 결과에 저장할 때, 저장할 곳을 생성하는 것

    def init(M):
        res = []
        for m in range(M):
            temp = []
            for n in range(M):
                temp.append(0)
            res.append(temp)
        return res

    def check(key, padded_locK):
        T = len(padded_lock)
        M = len(key)
        # gap은 어떻게 겹칠지를 의미함
        # padded_lock의 (0,0)에서 key를 얼마나 shift 시킬지에 대한 값 
        for gap1 in range(T - M + 1):
            for gap2 in range(T - M + 1):
                res = True
                cnd_padded_lock = copy.deepcopy(padded_lock)
                for p in range(M):
                    for q in range(M):
                        cnd_padded_lock[p + gap1][q + gap2] += key[p][q]
                check_area = []
                for p in range(M-1, T - M + 1):
                    temp = []
                    for q in range(M - 1, T - M + 1):
                        temp.append(cnd_padded_lock[p][q])
                check_area.append(temp)
            
            for p in range(len(check_area)):
                for q in range(len(check_area)):
                    if check_area[p][q] != 1:
                        res = False
                        break
                if res == False:
                    break
            
            if res == True:
                return res

        return False
        

    # Key 후보 다 뽑기(90도 회전 후보)
    '''
    90도 회전시
    (0, 0), (0, 1), (0, 2), ..., (0, M-1)
    =>
    (0, M-1), (1, M-1), (2, M-1), ..., (M-1, M-1) 
    # matrix의 두 번째 줄의 회전
    (1, 1), (1, 2), ..., (1, M-2)
    => 90도
    (1, M-2), (2, M-2), ..., (M-2, M-2)
    => 90도
    (M-2, M-2), (M-2, M-3), ..., (M-2, 1)
    (p, q) -> (q, M-1-p)

    '''

    for i in range(3):
        new_key = init(M)
        for p in range(M):
            for q in range(M):
                # 직전 key에서 90도를 돌리는 것이기 때문에 -1 인덱스
                new_key[q][M - 1 - p] = key[-1][p][q]
        key.append(new_key)
    
    # N x N 타일을 M x M 타일 위에 window sliding 하기 위해
    def padding(lock, N, M):
        T = N * 2 * (M - 1)
        padded_lock = init(T)

        # padded_lock 내의 원래 lock의 값을 복사
        for i in range(N):
            for j in range(N):
                padded_lock[i + M - 1][j + M - 1] = lock[i][j]
        
        return padded_lock
        
    padded_lock = padding(lock, N, M)
    
    # 모두 1로 채워지는지 check
    answer = False
    for i in range(4):
        candidate_key = key[i]
        if check(candidate_key, padded_lock) == True:
            return True


    return answer

key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
