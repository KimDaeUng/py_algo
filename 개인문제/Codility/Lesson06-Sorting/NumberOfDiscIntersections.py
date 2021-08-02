
# My Solution 3
https://app.codility.com/demo/results/trainingK6GE6P-BFK/
def solution(A):
    arr = []

    for i in range(len(A)):
        arr.append((i - A[i], 0))
        arr.append((i + A[i], 1))
    
    arr.sort()
    
    cnt_open = 0
    cnt_intersect = 0

    for _, direction in arr:
        if direction == 0:
            cnt_intersect += cnt_open
            cnt_open += 1
        elif direction == 1:
            cnt_open -= 1
    if cnt_intersect > 10000000:
        return -1
    else:
        return cnt_intersect

# 40m
# My Solution : Fail : O(N^2)
# https://app.codility.com/demo/results/training5AD7PS-C2K/
def solution(A):

    uppers = []
    lowers = []
    cnt = 0
    for i in range(len(A)):
        cur_r = A[i]
        cur_upper = i + cur_r
        cur_lower = i - cur_r

        for j in range(len(uppers)):
            if j == i:
                continue
            if (lowers[j] <= cur_lower and cur_lower <= uppers[j]) or \
                (lowers[j] <= cur_upper and cur_upper <= uppers[j]) or \
                (lowers[j] >= cur_lower and cur_upper >= uppers[j]) or \
                (lowers[j] <= cur_lower and cur_upper <= uppers[j]):
                cnt += 1
                # print(f'cnt : {cnt} | cur : ({cur_lower}, {cur_upper}), compare : ({lowers[j]}, {uppers[j]}))')

        uppers.append(cur_upper)
        lowers.append(cur_lower)
    return cnt

# 26m
# My Solution : Fail : O(N^2), arithmetic error
# https://app.codility.com/demo/results/trainingKVMS43-53Y/
def solution(A):
    
    def get_range(j):
        r = A[j]
        return set(list(range(j - r, j + r + 1)))
    
    sets = []
    for i in range(len(A)):
        sets.append(get_range(i))
        
    cnt = 0
    for i in range(len(sets)):
        cnt += sum([bool(sets[i] & sets[j]) for j in range(len(sets)) if j != i])
    return cnt // 2

# 3rd
def solution(A):
    if len(A) == 1:
        return 0
    cum_cnt = 0
    uppers = 0
    lowers = 0
    cnt = 0
    
    boundarys = []
    for i in range(len(A)):
        cur_upper = i + A[i]
        cur_lower = i - A[i]
        boundarys.append((cur_lower, cur_upper))
    
    boundarys.sort(key=lambda x : (x[0], x[1]))
    print(boundarys)
    min_upper = 2147483647
    max_upper = -2147483647
    for i in boundarys:
        cur_lower = i[0]
        if cur_lower <= min_upper:
            cnt += 1
            cum_cnt += cnt
        else:
            cnt -= 1
            cum_cnt += cnt
        min_upper = min(min_upper, i[1])
        max_upper = max(max_upper, i[1])

        # if (lowers <= cur_lower and cur_lower <= uppers) or \
        #     (lowers <= cur_upper and cur_upper <= uppers) or \
        #     (lowers >= cur_lower and cur_upper >= uppers) or \
        #     (lowers <= cur_lower and cur_upper <= uppers):
            
        #     cum_cnt += cnt
        #     print(f'cnt : {cnt} | cur : ({cur_lower}, {cur_upper}), compare : ({lowers}, {uppers}))')
        # cnt += 1
        # uppers = max(uppers, cur_upper)
        # lowers = min(lowers, cur_lower)
    return cum_cnt


# Solution
def solution(A):
    lowers = []
    uppers = []

    for i in range(len(A)):
        lowers.append(i - A[i])
        uppers.append(i + A[i])
    
    lowers.sort()
    uppers.sort()

    intersection = 0
    j = 0
    for i in range(len(A)):
        while j < len(A) and lowers[j] <= uppers[i]:
            print(i, j, lowers[j], uppers[i], intersection)
            intersection += j
            intersection -= i
            j += 1

    if intersection > 10000000:
        return -1
    
    return intersection


