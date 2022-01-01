# https://app.codility.com/demo/results/trainingGZQCY4-34K/

def solution(A):
    N = len(A)
    if N <= 2:
        return sum(A)

    i = 0
    score = A[0]
    while i < N - 1:
        
        # 매번 가능한 후보들 중에서 최대가 되는 인덱스를 선택
        max_score = -int(1e9)
        max_idx = 0
        for dice_idx in range(1, 7):
            if i + dice_idx < N and max_score <= A[i + dice_idx]:

                max_idx = dice_idx
                max_score = A[i + dice_idx] + A[-1] if i + dice_idx != N - 1 else A[i + dice_idx]

        i += max_idx
        score += A[i]

    return score


# https://app.codility.com/demo/results/trainingSN3H22-YVY/
For example, for the input [0, -4, -5, -2, -7, -9, -3, -10] the solution returned a wrong answer (got -13 expected -12).

def solution(A):
    N = len(A)
    if N <= 2:
        return sum(A)

    i = 0
    score = A[0]
    while i < N - 1:
        # 매번 가능한 후보들 중에서 최대가 되는 인덱스를 선택
        max_score = -int(1e9)
        max_idx = 0
        for dice_idx in range(1, 7):
            if i + dice_idx > N - 1:
                break

            if  max_score <= A[i + dice_idx]:
                max_idx = dice_idx
                if i + dice_idx >= N - 1 - 6:
                    max_score = A[i + dice_idx] + A[-1] \
                        if i + dice_idx != N - 1 else A[i + dice_idx]
                else:
                    max_score = A[i + dice_idx]
                # print(i, score, i + max_idx, max_score)

        i += max_idx
        score += A[i]

    return score

# My Solution : Fail
# For example, for the input [1, -2, 4, 3, -1, -3, -7, 4, -9] the solution returned a wrong answer (got -6 expected 3).


# https://app.codility.com/demo/results/trainingQWBFUR-XTJ/
def solution(A):
    N = len(A)
    if N <= 2:
        return sum(A)

    i = 0
    score = A[0]
    while i < N - 1:
        # 매번 가능한 후보들 중에서 최대가 되는 인덱스를 선택
        max_score = -int(1e9)
        max_idx = 0
        for dice_idx in range(1, 7):
            if i + dice_idx > N - 1:
                break
            if i + dice_idx >= N - 1 - 6:
                cur_score = A[i + dice_idx] + A[-1] if i + dice_idx < N - 1 else A[-1]
            else:
                cur_score = A[i + dice_idx]
                
            if  max_score <= cur_score:
                max_idx = dice_idx
                max_score = cur_score
                print(i, score, i + max_idx, max_score)

        i += max_idx
        score += A[i]

    return score



def solution(A):
    N = len(A)
    if N <= 2:
        return sum(A)

    i = 0
    score = A[0]
    while i < N - 1:
        # 매번 가능한 후보들 중에서 최대가 되는 인덱스를 선택
        max_score = -int(1e9)
        max_idx = 0
        for dice_idx in range(1, 7):
            next_idx = i + dice_idx

            # 범위를 넘어가는 경우
            if next_idx > N - 1:
                break
            
            # 마지막 인덱스 포함 5개 남았을 때
            if i + 6 > N - 2:
                cur_score = A[next_idx] + A[-1] if next_idx != N - 1 else A[-1]
            else:
                cur_score = A[next_idx]
                
            if  max_score < cur_score:
                max_idx = dice_idx
                max_score = cur_score



        i += max_idx
        score += A[i]
        print(i, score)


    return score

# https://app.codility.com/c/run/trainingEWJD7Z-SDE/
# 인덱스로 풀려다가 오름차순으로 진행하면 부분최적해가 전역최적해임이 보장되지 않음을 확인
# 뒤에서부터 인덱스 해야하는 듯
def solution(A):
    N = len(A)
    if N <= 2:
        return sum(A)

    i = min(6, N)
    score = A[0]
    total_score = 0
    while i < N - 1:
        print(i)
        # 1 ~ 6까지 모든 경우 가운데 최대값의 index 계산
        cur_score = 0
        max_idx = 0
        max_score = -int(1e9)
        for dice_idx in range(1, 7):
            next_idx = i - dice_idx

            # 범위를 넘어가는 경우
            if next_idx < 0:
                break
            
            # 넘어가지 않는 경우 현재값 계산 후 기존 max_score와 비교
            # 가장 큰 값으로 대체
            cur_score = score + A[next_idx]
            if  max_score < cur_score:
                max_idx = dice_idx
                max_score = cur_score
        
        # print(i, max_idx, max_score)

        i += max_idx
        score += A[i]
        total_score = max(score, total_score)

    return total_score