# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/
# 3h

# My Solution : Fail
# https://app.codility.com/demo/results/trainingSUC5ME-84B/
'''
못이 판자 너비 내에 위치하는 최대 연속 개수 파악
각각의 못에 대해 모든 판자 너비를 순회하며 검사

i = 0, k = 0
    C[0] = 4
        k = 0, [1, 4], k += 1
        k = 1, [4, 5], k += 1
        k = 2, [5, 9] 범위내 없으므로  i += 1, k = 2

i = 1, k = 2
    C[1] = 6
        k = 2, [5, 9], k += 1
        k = 3, [8, 10] 범위내 없으므로z i += 1, k = 3

i = 2, k = 3
    C[2] = 10
        k = 3, [8, 10] k += 1
        k = 4, list A, B out of range, break
'''


def solution(A, B, C):
    k = 0
    i = 0
    N_plank = len(A)
    N_nail = len(C)

    if A[0] == B[0] and (B[0] < C[0] or C[0] < A[0]):
        return -1

    while k < N_plank and i < N_nail:
        if A[k] <= C[i] and C[i] <= B[k]:
            k += 1
        else:
            i += 1
    return i + 1

# Solution : Correct 100%
def solution(A,B,C):
    N = len(A)
    m = dict() #[0]*n
    
    for i, nail in enumerate(C):
         for j, (a, b) in enumerate(zip(A,B)):
            if a <= nail <= b:
                m[j] = 1
                if len(m) == N:
                    return i + 1
    return -1

# Solution
'''
판자에 못을 박을 수 있는 못 중 가장 작은 좌표값을 가진 못을 찾고,
판자 위에 있으면서 인덱스가 가장 작은 못을 찾기 위한 선형 탐색 시도
# ref : https://www.martinkysel.com/codility-nailingplanks-solution/
'''
# https://app.codility.com/demo/results/trainingTVATGD-YWF/
PLANK_START = 0
PLANK_END = 1

NAIL_ARR_IDX = 0
NAIL_HIT_LOC = 1

def solution(A,B,C):
    def find_nail_pos(nails, plank, prev_max):
        # 판자에 못을 박을 수 있는 가장 작은 좌표값 이진탐색
        nail_idx = -1
        result = -1

        lower_idx = 0
        upper_idx = len(nails) - 1

        while lower_idx <= upper_idx:
            mid_idx = (lower_idx + upper_idx) // 2
            nail_hit_loc = nails[mid_idx][1]
            if nail_hit_loc < plank[PLANK_START]:
                lower_idx = mid_idx + 1
            elif nail_hit_loc > plank[PLANK_END]:
                upper_idx = mid_idx - 1
            else:
                upper_idx = mid_idx - 1
                result = nails[mid_idx][NAIL_ARR_IDX]
                nail_idx = mid_idx
        
        if result == -1:
            return result
        
        # 판자 위에 있으면서 인덱스가 가장 작은 못을 찾기 위한 선형 탐색
        nail_idx += 1
        while nail_idx < len(nails):
            if nails[nail_idx][NAIL_HIT_LOC] > plank[PLANK_END]:
                break
            result = min(result, nails[nail_idx][NAIL_ARR_IDX])
            if result <= prev_max:
                return result
            nail_idx += 1

        return result

    def get_nails_required(planks, nails):
        result = -1
        for plank in planks:
            result = max(result, find_nail_pos(nails, plank, result))
        if result == -1:
            return result
        else:
            return result + 1
    
    planks = zip(A, B)
    nails = sorted(enumerate(C), key=lambda x: x[1])

    return get_nails_required(planks, nails)