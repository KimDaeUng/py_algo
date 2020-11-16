# https://algospot.com/judge/problem/read/PI

import sys
sys.setrecursionlimit(10**8)
# # 동적 계획법 레시피
# 1. 주어진 문제를 완탐으로 해결
# 2. 중복된 부분 문제를 한 번만 계산하도록 메모이제이션 

# 부분 문제가 뭐지?? : 3~5자리씩 끊어진 숫자의 난이도 구하기
# 중복되는 것이 있나? : 이미 구한 숫자의 난이도라면 단순 리턴하기

def difficulty(start, end):
    # 1. 모든 숫자가 같을 때
    len_input = end-start+1
    # print(len_input)
    input_str = pi_str[start:start+len_input]
    # print(pi_str)
    # print("input str : ", input_str)
    # print("len_input ", len_input)
    if input_str == [input_str[0]]*len_input:
        return 1
    # 4. 숫자가 등차수열을 이룰 때
    chk2 = True
    diff = input_str[1] - input_str[0]

    # 2. 숫자가 1씩 단조 증가 | 감소할 때
    #    (공차 1인 등차수열)
    for i in range(0, len_input-1):
        if (input_str[i+1] - input_str[i]) != diff:
            chk2 = False
            break

    if chk2&(abs(diff) == 1):
        return 2
    # 3. 두 숫자가 번갈아가면서 출현할 때
    chk3 = True
    for i in range(len_input):
        if input_str[i] != input_str[i%2]:
            chk3 = False
            break
    if chk3:
        # print("ck3 is true")
        return 4
    # 4. 숫자가 등차 수열을 이룰 때
    #    단조 증가 또는 감소를 만족하는 공차가 1이 아닌 수열
    if chk2: # diff != 1
        return 5
    # 5. 그 외 난이도 10
    return 10

def recur_get_score(start):
    len_pi_str = len(pi_str)
    # 기저 사례 : 숫자 전체를 탐색완료할 경우    
    if start == len(pi_str):
        return 0
    
    # 메모이제이션
    # 이미 계산된 값이 있으면 그 값을 리턴
    ret = cache[start]
    if (ret != -1):
        return ret

    # 각 길이별 최소 난이도 중 가장 최소인 난이도를 출력
    # 현재의 최소 난이도 + 다음부터 끝까지의 최소 난이도(재귀)
    ret = MAXINF
    for length in range(3, 6):
        if (start + length <= len_pi_str):
            # print("-"*50)
            # print("start : {}, lenght : {}, end : {}".format(start, length, start+length-1))
            ret = min(ret, difficulty(start, start + length -1)
                        + recur_get_score(start+length))
            cache[start] = ret

    # memoization : 필요한가???
    return ret
MAXINF = 987654321
C = int(sys.stdin.readline())
for i in range(C):
    cache = [-1] * 10001
    # pi_str = list(map(int, sys.stdin.readline().strip()))
    pi_str =  list(map(int, list(input().strip())))
    print(recur_get_score(0))


##########################

# pi
def score_3(a, b, c):  # 3자리씩 끊어 읽기
    if a == b == c:  # 모든 숫자가 같음
        return 1
    if a-b == b-c == 1 or a-b == b-c == -1:  # 단조증가/감소
        return 2
    if a == c != b:  # 숫자가 번갈아 출현
        return 4
    if a-b == b-c:  # 등차수열
        return 5
    return 10
 
 
def score_4(a, b, c, d):  # 4자리씩 끊어 읽기
    if a == b == c == d:
        return 1
    if a-b == b-c == c-d == 1 or a-b == b-c == c-d == -1:
        return 2
    if a == c and b == d and a != b:
        return 4
    if a-b == b-c == c-d:
        return 5
    return 10
 
 
def score_5(a, b, c, d, e):  # 5자리씩 끊어 읽기
    if a == b == c == d == e:
        return 1
    if a-b == b-c == c-d == d-e == 1 or a-b == b-c == c-d == d-e == -1:
        return 2
    if a == c == e and b == d and a != b:
        return 4
    if a-b == b-c == c-d == d-e:
        return 5
    return 10
 
 
def pi(arr):
    N = len(arr)  # 리스트의 길이
    cache = [None] * (N+1)
    cache[3] = score_3(arr[0], arr[1], arr[2])  # 0~2번까지 3개 읽음
    cache[4] = score_4(arr[0], arr[1], arr[2], arr[3])  # 0~3번까지 4개 읽음
    cache[5] = score_5(arr[0], arr[1], arr[2], arr[3], arr[4])  # 0~4번까지 5개 읽음
    for i in range(6, N+1):
        cand = []
        if cache[i-3] is not None:
            cand.append(cache[i-3] + score_3(arr[i-3], arr[i-2], arr[i-1]))
        if cache[i-4] is not None:
            cand.append(cache[i-4] + score_4(arr[i-4], arr[i-3], arr[i-2], arr[i-1]))
        if cache[i-5] is not None:
            cand.append(cache[i-5] + score_5(arr[i-5], arr[i-4], arr[i-3], arr[i-2], arr[i-1]))
        cache[i] = min(cand)  # 최소값을 cache에 넣는다
    return cache[-1]
 
 
case = int(input())
for k in range(case):
    number = list(map(int, list(input().strip())))  # 입력을 숫자 리스트로 만든다
    print(pi(number))


출처: https://doctcoder.tistory.com/39 [나만의 코딩 일기]