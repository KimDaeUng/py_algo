# https://algospot.com/judge/problem/read/JLIS

import sys, math

# 최적화 문제 동적 계획법 레시피
# 1. 모든 답을 만들어 보고 그중 최적해의 점수를 반환하는 완전 탐색 알고리즘을 설계
# 2. 전체 답의 점수를 반환하는 것이 아닌, 앞으로 남은 선택들에 해당하는 점수만을 반환하도록 부분 문제 정의를 바꾸기
# 3. 재귀 호출의 입력에 이전의 선택에 관련된 정보가 있다면 꼭 필요한 것만 남기고 줄이기, 문제에 최적 부분 구조가 성립할 경우에는
# 이전 선택에 관련된 정보를 완전히 제거 가능, 여기서 목표는 가능한 한 중복되는 부분 문제를 많이 만드는 것. 입력의 종류가 줄어들면 더 많은
# 부분 문제가 중복되고, 따라서 메모이제이션을 최대로 활용 가능
# 4. 입력이 배열이거나 문자열인 경우 가능하다면 적절한 변환을 통해 메모이제이션 하도록 함
# 5. 메모이제이션 활용

# 부분 문제 : 
# A[idxA], B[idxB]에서 시작하는 합친 증가 부분 수열의 최대길이


NEGINF = -math.inf
cache = [[-1]*101 for _ in range(101)]

def jlis(idxA, idxB):
    
    # 메모이제이션
    ret = cache[idxA+1][idxB+1]
    if (ret!=-1):
        return ret
    
    ret = 2
    cache[idxA+1][idxB+1] = 2
    if idxA == -1:
        a = NEGINF
    else:
        a = A[idxA]
    if idxB == -1:
        b = NEGINF
    else:
        b = B[idxB]
    max_elem = max(a, b)
    for nextA in range(idxA+1, N):
        if max_elem < A[nextA]:
            ret = max(ret, jlis(nextA, idxB)+1)
            cache[idxA+1][idxB+1] = ret
    for nextB in range(idxB+1, M):
        if max_elem < B[nextB]:
            ret = max(ret, jlis(idxA, nextB)+1)
            cache[idxA+1][idxB+1] = ret
    return ret 


C = int(sys.stdin.readline())
for i in range(C):
    # pi_str = list(map(int, sys.stdin.readline().strip()))
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    print(jlis(-1, -1))