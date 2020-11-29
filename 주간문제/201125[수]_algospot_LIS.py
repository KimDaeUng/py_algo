# https://algospot.com/judge/problem/read/LIS

import sys, math

# 최적화 문제 동적 계획법 레시피
# 1. 모든 답을 만들어 보고 그중 최적해의 점수를 반환하는 완전 탐색 알고리즘을 설계
# 2. 전체 답의 점수를 반환하는 것이 아닌, 앞으로 남은 선택들에 해당하는 점수만을 반환하도록 부분 문제 정의를 바꾸기
# 3. 재귀 호출의 입력에 이전의 선택에 관련된 정보가 있다면 꼭 필요한 것만 남기고 줄이기, 문제에 최적 부분 구조가 성립할 경우에는
# 이전 선택에 관련된 정보를 완전히 제거 가능, 여기서 목표는 가능한 한 중복되는 부분 문제를 많이 만드는 것. 입력의 종류가 줄어들면 더 많은
# 부분 문제가 중복되고, 따라서 메모이제이션을 최대로 활용 가능
# 4. 입력이 배열이거나 문자열인 경우 가능하다면 적절한 변환을 통해 메모이제이션 하도록 함
# 5. 메모이제이션 활용

# 부분문제 : idx에서 시작하는 최대 증가부분 수열 중 최대 길이 반환

cache = [-1 for _ in range(501)]

def lis(idx):
    ret = cache[idx]
    if (ret != -1):
        return ret
    
    ret = 1
    for i in range(idx+1, N):
        if (idx == -1) | (array[idx] < array[i]):
            ret = max(ret, lis(i)+1)
    return ret

C = int(sys.stdin.readline())
for i in range(C):
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    print(lis(-1)-1)