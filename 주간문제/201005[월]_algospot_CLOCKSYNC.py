# https://www.algospot.com/judge/problem/read/CLOCKSYNC

import sys


switch_clock = [
    [0, 1, 2],
    [3, 7, 9, 11],
	[4, 10, 14, 15],
	[0, 4, 5, 6, 7],
	[6, 7, 8, 10, 12],
	[0, 2, 14, 15],
	[3, 14, 15],
	[4, 5, 7, 14, 15],
	[1, 2, 3, 4, 5],
	[3, 4, 5, 9, 13]
    ]


# 종만북 Solution - Python 시간초과

# 스위치 누르는 순서 무관
# 스위치의 클릭 수 [0, 3]

# 작업 : 한 스위치를 누를 횟수 정하기

def push(clocks, n_switch):
    for n_linked_clock in switch_clock[n_switch]:
        clocks[n_linked_clock] = (clocks[n_linked_clock] + 3) % 12

# clocks : 시계의 상태
# n_switch : 누를 스위치의 번호
# 각 스위치를 눌러 clocks를 12시로 맞출 최소 횟수 반환
# 불가능할 경우 큰 수 반환

def solution(clocks, n_switch):
    # Base Case
    # 1. 모두 12시를 가리키는 경우
    if any(clocks) == False:
        return 0
    
    # 2. 불가능한 경우(10개 스위치 모두 눌러도 )
    if n_switch == 10:
        return float('inf')
    
    ret = float('inf')
    
    # 스위치를 0~3번 모두 누른다.
    for i in range(4):
        ret = min(ret, i + solution(clocks, n_switch+1))
        push(clocks, n_switch)

    return ret

C = int(sys.stdin.readline())


for i in range(C):
    clocks = list(map(int, sys.stdin.readline().split()))             
    
    answer = solution(clocks, 0) 
    
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
