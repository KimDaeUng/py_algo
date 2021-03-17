# https://programmers.co.kr/learn/courses/30/lessons/42889
# 10:33-11:42

'''
[입력]
N : 전체 스테이지 개수
stages : 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열, N + 1은 모두 클리어 한 사용자

실패율 : (스테이지 도달했지만 클리어 못한 플에이어 수) / (스테이지 도달한 플에이어 수 = 성공 + 도전중)

[출력]-실패율 내림차순으로 스테이지 번호가 담긴 배열

1 <= M <= 500
1 <= len(stages) <= 200,000
실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 온다
스테이지에 도달한 유저가 없을 시 해당 스테이지 실패율은 0
'''

'''
1. 계수 정렬을 이용해 각 스테이지에 도전중인 사용자를 구한다.
-> 이걸 challenge_list라 하자
2. 스테이지에 도달한 플에이어의 수는 뒤에서부터 cumulated sum 되어야한다.
challenge_list의 뒤에서부터 분모를 누적해서 더해가며
실패율의 리스트(fail_rate_list)를 구하자.
각 원소는 (stage_number, fail_rate)이다.
3. fail_rate_list를 fail_rate에 따라 내림차순 정렬한다.
'''
from collections import defaultdict
def solution(N, stages):
    # 총 N + 1개의 칸이 필요한데,
    # 인덱스 번호를 1부터 시작하기 위해 (N + 1) + 1개 칸
    c_list = [0] * ((N + 1) + 1)

    # 1. 각 스테이지 도전중인 사용자 카운트
    for i in stages:
        c_list[i] += 1
    # print(c_list)
    
    # 2. 각 스테이지에 도달한 플에이어 수를 cumsum
    fail_list = [0] * (N + 1)
    cumsum_list = c_list[:]
    # print(cumsum_list)
    for i in range(N, 0, -1):
        # 예외 처리 :
        # ex) N = 2, stages = [1, 1, 1, 1]
        # -> 0 = 2에 도전 중인 사람 + 2를 끝낸 사람
        # 따라서 stage 2에 대한 fail rate 계산시 0으로 나누게 되어 에러 발생
        # 따라서 해당 스테이지가 0이 아닐때만 값을 처리하고 0일땐 fail rate = 0
        if c_list[i] != 0:
            fail_list[i] = (i, c_list[i] / (cumsum_list[i] + cumsum_list[i+1]))
        else:
            fail_list[i] = (i, 0)
        # 분모 누적합
        cumsum_list[i] = cumsum_list[i] + cumsum_list[i+1]
    # 더미 인덱스 값 지움
    del fail_list[0]

    # 3. 정렬
    # print(c_list)
    # print(fail_list)
    fail_list = sorted(fail_list, key=lambda x : (-x[1], x[0]))
    return [i[0] for i in fail_list]

N = 2
stages = [1, 1, 1, 1]
print(solution(N, stages))

# Solution

def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호 1 -> N
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
    
    # 실패율을 기준으로 각 스테이지 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer