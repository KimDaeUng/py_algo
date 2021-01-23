# https://programmers.co.kr/learn/courses/30/lessons/42839

# 14:09-14:50

# My solution 틀린 풀이
from itertools import permutations

def solution(numbers):
    len_numbers = len(numbers)
    answer_list = list(numbers)
    answer_list = [i for i in answer_list if i != "0"]
    
    for num in range(2, len_numbers):
        cases = list(map("".join, permutations(numbers, num)))
        cases = [i for i in cases ]
        for i in cases:
            if i[0] != "0":
                for j in answer_list:
                    if int(i) % int(j) != 0:
                        answer_list.append(i)
    
    return len(answer_list)


# 18:20-19:17
# ref : https://liveyourit.tistory.com/211

from itertools import permutations

# 모든 경우를 담은 리스트를 입력받아 소수의 개수를 출력하는 함수
def cnt_prime(case_list):
    prime_list = []
    for n in case_list:
        is_prime = True
        # 2부터 n-1까지 나누었을 떄 나머지가 0인 것은 소수가 아님
        for i in range(2, n):
            # 소수가 아닐 경우 이후 case를 나누지 않고 내부 for문 종료
            if n % i == 0:
                is_prime = False
                break
        # 나누어 떨어지지 않고 0, 1이 아닌 경우 prime_list에 append
        if n > 1 and is_prime:
            prime_list.append(n)
    return len(prime_list)

def solution(numbers):
    # 모든 경우를 다 찾기
    cases = []
    len_numbers = len(numbers)
    for num in range(1, len_numbers+1):
        tmp = permutations(numbers, num)
        for n in tmp:
            tmp_str = "".join(n)
            cases.append(int(tmp_str))
    
    cases = list(set(cases))
    # print(cases)
    return cnt_prime(cases)

# Best Solution
from itertools import permutations
def solution(n):
    n_list = list(n)
    a = set()
    # 1. 가능한 모든 경우의 수 구함
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(n_list, i+1))))
    # 2. 0, 1을 제외
    a -= set(range(0, 2))
    # 3. 에라토스테네스의 체
    # 어떤 수 N의 최대 약수는 sqrt(N)이므로,
    # 전체 경우의 수 중 최대 값의 최대 약수 까지만 탐색
    maximum = int(max(a) ** 0.5) + 1
    for i in range(2, maximum):
        # i = 2, 3, ... 최대값의 가능한 최대 약수까지 순회하면서
        # i 자기 자신을 재외한 배수를 지움
        a -= set(range(i * 2, max(a)+1, i))
    
    return len(a)

# 또 다른 풀이
# https://yurimkoo.github.io/algorithm/2019/09/26/find_prime_number.html

    