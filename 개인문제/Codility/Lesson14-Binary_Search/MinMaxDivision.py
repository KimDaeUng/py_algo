

# My Solution
'''
부분합의 최대값을 최소화하자
K개 블록으로 분할, 각 블록의 총합의 최댓값이 가장 작은 것을 구하는 문제
각각은 최대 M개 원소까지만 담을 수 있다.
parametric search
비슷한 합을 가지도록 분할 후 둘 중 하나가 더 커지도록 분할?

block 개수 K에 따라 각 블록 총합의 최댓값이 가장 작은 경우는
1. K == 1 인 경우 : 모든 원소 합
2. K == len(A) 인 경우 : 각 블록의 총합 == 각 원소의 값이므로, 블록 총합 최대값 == max(A)
3. K > len(A) 인 경우 : 2와 동일하나 빈 블록 추가됨
4. 1 < K < len(A)인 경우 : 
각 블록 sum에 대하여 이분탐색 


'''

# Solution
# https://programming-review.com/python/algorithms#minmaxdivision
# https://www.martinkysel.com/codility-minmaxdivision-solution/


# https://app.codility.com/demo/results/trainingCNANAF-RH9/
'''

'''
def chk(A, max_block_cnt, max_block_sum):
    # 제약 조건(블록 개수
    tmp_sum = 0 
    tmp_cnt = 0 # 블록 개수
    
    for e in A:
        # block의 최대값을 넘어가면 블록 나누기
        if tmp_sum + e > max_block_sum:
            tmp_sum = e
            tmp_cnt += 1
        # block의 최대값을 넘어가지 않으면 블록 안의 원소 값 sum
        else:
            tmp_sum += e
        if tmp_cnt >= max_block_cnt:
            return False
    return True
 
def solution(K, M, A):
    N = len(A)
    lower_sum = max(A) # 각 블록 sum의 최소값
    upper_sum = sum(A) # 모든 블록 sum 값
    
    # Case 1
    if K == 1:
        return upper_sum

    # Case 2, 3
    if K >= N:
        return lower_sum

    # Case 4 
    while lower_sum <= upper_sum:
        mid_sum = (lower_sum + upper_sum) // 2
        # K개 블록으로 분할되면 블록합의 크기를 줄여가면서 더 작은 블록합 탐색
        if chk(A, K, mid_sum):
            upper_sum = mid_sum - 1
        # K개 블록으로 분할 안되면 분할 안되는 블록합보다 작은 블록합은 탐색하지 않음
        else:
            lower_sum = mid_sum + 1

    return lower_sum