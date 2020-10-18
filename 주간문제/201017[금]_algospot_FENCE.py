# https://algospot.com/judge/problem/read/FENCE#

import sys

'''
가운데 울타리를 포함하는 최대 넓이를 계산
(가운데를 포함하는 모든 가능한 너비에 대한 넓이 계산)

한 번의 재귀함수에서
1. 가운데울타리를 포함하는 최대 넓이
2. 왼쪽 부분의 가운데울타리를 포함하는 최대넓이
3. 오른쪽 부분의 가운데울타리를 포함하는 최대넓이
중 최대값을 반환
2, 3은 재귀로 처리

'''

# 가운데 울타리를 포함하는 최대 넓이
def midMax(Start, end):
    global Fence
    mid = (Start + end)//2
    # Current Height
    cur_h = min(Fence[mid], Fence[mid+1])
    # Current Max value
    cur_max = -1 
    # Current Width
    cur_w = -1
    # 오른쪽 확장 인덱스
    right = mid
    # 왼쪽 확장 인덱스
    left = mid
    
    while True:
        # 탐색이 종료되면 
        if left == Start and right == end:
            break
        # 오른쪽 끝에 도달하면 왼쪽으로 확장
        if right == end:
            left -= 1
            # 현재 높이가 확장한 지점의 높이보다 작으면 값을 그대로 유지하고
            # 현재 높이가 더크면 확장한 값(더 작은 높이)으로 갱신한다.
            cur_h = cur_h if cur_h < Fence[left] else Fence[left]
        # 왼쪽 끝에 도달하면 오른쪽으로 확장
        elif left == end:
            right +=1
            cur_h = cur_h if cur_h < Fence[right] else Fence[right]
        # 중간을 탐색중인 경우 좌우를 비교하고 큰 쪽으로 확장
        else:
            if Fence[left-1] <= Fence[right+1]:
                right += 1
                cur_h = cur_h if cur_h < Fence[right] else Fence[right]
            else:
                left -= 1
                cur_h = cur_h if cur_h < Fence[left] else Fence[left]
        
        cur_w += 1
        # 현재 넓이와 현재까지의 최대 넓이를 비교해
        # 큰 값으로 갱신
        cur_max = cur_max if cur_max > cur_h * cur_w else cur_h * cur_w

    return cur_max


def solution(Start, N):
    global Fence
    # 울타리가 1개인 경우

    if Start == N:
        return Fence[N]

    # 울타리가 2개인 경우
    if n - Start == 1:
        return max(Fence[Start], Fence[N], 2*min(Fence[Start], Fence[end]))
    
    # 절반으로 나누어 분할정복, 현재의 최대값과 비교
    return max(findMax(Start, (N+Start)//2), findMax((N+Start)//2+1, N), midMax(Start, N))

C = int(sys.stdin.readline())

for i in range(C):
    N = int(input())
    Fence = list(map(int, sys.stdin.readline().strip().split()))
    print(solution(0, N-1))    