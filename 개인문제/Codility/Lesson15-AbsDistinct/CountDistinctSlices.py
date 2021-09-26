# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/start/

# My Solution: Fail 
import math
def solution(M, A):
    
    cur_set = set()
    answer = 0
    # prev_a = -1
    for a in A:
        # print(a)
        # if prev_a == a:
        #     cur_set = set()
        #     cur_set.add(a)
        #     continue

        if a not in cur_set:
            cur_set.add(a)
            # prev_a = a
            # print('\ta not in cur_set', cur_set)
        else:
            len_set = len(cur_set)
            # print('\tlen_set ', len_set)
            if len_set >= 2:
                answer += math.factorial(len_set) // (math.factorial(2)* math.factorial(len_set - 2)) + len_set
                # print('\tfactorial ', math.factorial(len_set) // (math.factorial(2)* math.factorial(len_set - 2)), len_set, answer)
                cur_set = set()
                cur_set.add(a)
            else:
                cur_set = set()
                cur_set.add(a)
                continue
            # print('\ta in cur_set', cur_set)
    else:
        len_set = len(cur_set)
        # print('\tlen_set ', len_set)
        if len_set >= 2:
            answer += math.factorial(len_set) // (math.factorial(2)* math.factorial(len_set - 2)) + len_set
            # print('\tfactorial ', math.factorial(len_set) // (math.factorial(2)* math.factorial(len_set - 2)), len_set, answer)
        else:
            answer += 1
            # print('\tfactorial ', answer)
    return answer


# Solution
https://app.codility.com/demo/results/trainingA4DHZU-Z5D/
def solution(M, A):
    n = len(A)
    app_set = set()
    front = 0
    total_cnt = 0
    for back in range(n):
        while (front < n and (A[front] not in app_set)):
            app_set.add(A[front])
            total_cnt += front - back + 1
            front += 1
        
        app_set.remove(A[back])

        if total_cnt > 1000000000:
            return 1000000000

    return total_cnt