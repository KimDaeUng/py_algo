# https://programmers.co.kr/learn/courses/30/lessons/12982
# 16:39-16:40
# My Solution
def solution(d, budget):
    d.sort()
    total = 0
    cnt = 0
    for i in d:
        total += i
        cnt += 1
        if total > budget:
            total -= i
            break
            cnt -= 1
    return cnt

# Solution
# 예산에서 차감하며 체크
def solution(d, budget):
    d.sort()
    cnt = 0
    
    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1
    return cnt