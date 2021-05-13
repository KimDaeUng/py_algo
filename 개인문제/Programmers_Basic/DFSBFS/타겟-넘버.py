# https://programmers.co.kr/learn/courses/30/lessons/43165
# 유사문제 : 동빈북 - 13-19.연산자-끼워넣기
# 20:47-21:06
# 재귀함수를 이용한 완전탐색
# My Solution
def solution(numbers, target):
    n = len(numbers) - 1
    def rec(i, now):
        if i == n:
            if target == now:
                return 1
            else:
                return 0
        else:
            # 각 연산자에 대해 재귀 수행
            return rec(i+1, now + numbers[i+1]) + rec(i+1, now - numbers[i+1])
    
    return rec(-1, 0)


# Solution : 위와 동일하지만 간결한 코드
def solution(numbers, target):
    # numbers가 비어있고, target이 0이면 카운트
    if not numbers and target == 0:
        return 1
    # numbers가 비어있기만하면 카운트 X
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# Solution : DFS
answer = 0
def dfs(idx, numbers, target, value):
    global answer
    n = len(numbers)
    if (idx == n and target == value):
        answer += 1
        return
    if idx == n:
        return
    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

# Solution : Pythonic
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # 2개 이상의 리스트의 모든 조합
    # ex) [1, 1, 1, 1, 1]
    # -> l = [(1, -1) (1, -1) (1, -1) (1, -1) (1, -1)]
    # -> products(*l)은 모든 수의 +- 조합의 튜플을 원소로 하는 리스트
    # print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))