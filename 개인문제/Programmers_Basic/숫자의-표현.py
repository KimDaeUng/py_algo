# https://programmers.co.kr/learn/courses/30/lessons/12924
# 1h?
# My Solution 2: Two pointer
def solution(n):
    answer = 0
    s = 0
    e = 1
    n_list = list(range(1, n + 1))
    sum_ = n_list[0]
    while s < e:
        # print(s, e, sum_)
        if sum_ < n:
            sum_ += n_list[e]
            e += 1
        elif sum_ > n:
            sum_ -= n_list[s]
            s += 1
        else:
            answer += 1
            sum_ -= n_list[s]
            s += 1
    return answer

# My Solution1: Greedy, Timeout
def solution(n):
    answer = 0
    cal_sum = lambda n_, a, l: (n_ * (a + l)) // 2
    
    for e in range(1, n + 1):
        for s in range(1, e + 1):
            if cal_sum(e - s + 1, s, e) == n:
                answer += 1

    return answer

# Solution
# 1, ..., i, ..., n 에서 i마다 i부터 n보다 크거나 같은 최초의 누적합을 구함
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1
    return answer