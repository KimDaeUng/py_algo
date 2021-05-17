# https://programmers.co.kr/learn/courses/30/lessons/77484
# 02:00-02:50
# My Solution
def solution(lottos, win_nums):
    count2rank = { k: v for k, v in zip(range(6, 0, -1), range(1, 7))}
    count2rank[0] = 6
    check_nums = []
    n_zero = 0
    
    for i in lottos:
        if i == 0:
            n_zero += 1
            continue
        # 확인 가능한 번호 중 당첨된 숫자 탐색
        j = 0
        while j < len(win_nums) and win_nums[j] != i:
            j += 1
        if j != len(win_nums):
            check_nums.append(win_nums.pop(j))
    

    count = len(check_nums)
    lower_count = len(check_nums)
    # 모든 번호를 모르는 경우
    if n_zero == 6:
        return [1, 6]
    # 모든 번호를 아는 경우
    if n_zero == 0:
        return [count2rank[count], count2rank[count]]
    
    # 나머지 당첨 번호의 개수 >= 모르는 번호의 개수이면
    # 모르는 번호를 모두 맞았다고 가정할 수 있으므로
    remain_win_nums_count = 6 - len(check_nums)
    if remain_win_nums_count >= n_zero:
        count += n_zero
    # 나머지 당첨 번호의 개수 < 모르는 번호의 개수이면
    # 최대 나머지 당첨번호 개수만큼만 더 맞을 수 있으므로
    else:
        count += remain_win_nums_count

    return [count2rank[count], count2rank[lower_count]]

# Solution
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]