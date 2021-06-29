# https://programmers.co.kr/learn/courses/30/lessons/77884
# 18:44- 19:11

# My Solution
def div_n_even(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    
    if cnt % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    total = 0
    for i in range(left, right + 1):
        if div_n_even(i):
            total += i
        else:
            total -= i
    return total


# Solution: 제곱수는 약수의 개수가 홀수임을 이용
# k = 30
# q = 25
# print(int(k ** 0.5), k ** 0.5)
# print(int(q ** 0.5), q ** 0.5)

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer