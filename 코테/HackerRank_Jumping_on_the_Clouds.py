# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# 01:50-03:52

# 이전에 풀었던 유사한 문제 : 나누기 또는 빼기

# 플레이어는 현재 위치에서 한번에 1~2칸 오른쪽으로 이동 가능
# 번개 구름은 피해야함(배열에서 1로 표시)
# 마지막 구름까지 도달할 수 있는 최소한의 스텝 수를 구하라

# 항상 2칸씩 이동하되, 번개구름을 만날 경우 또는 인덱스 범위를 벗어난 경우 1칸만 이동
# 항상 성공한다 했으므로, 1이 두 번 연속하는 경우는 없음
#!/bin/python3

import math
import os
import random
import re
import sys

# My Solution
def jumpingOnClouds(c):

    len_c = len(c)
    count = 0
    idx = 0

    # Go forward by 2 spaces,
    # then go back by 1 when it meets 1

    while (idx < len_c):

        if c[idx] == 1:
            idx -= 1
            count -= 1
        else:
            idx += 2
        
        # prevent list idx out of range
        # 제일 마지막 스텝은 카운트 하지 않음
        # 다음 스텝에 대한 count를 미리하는 코드이므로, 다음 스텝의 idx가
        # 종료되는 상황(마지막 인덱스에 도달)이거나
        # 리스트 인덱스를 벗어난 상황일 경우 count += 1을 하지 않아야함
        if idx < (len_c-1):
            count += 1

    if idx >= len_c:
        count += 1
            
    return count

# Other Solution
def jumpingOnClouds(c):
    goal_idx = len(c) - 1
    idx = 0
    count = 0

    while(idx < goal_idx):
        # 먼저 2칸 앞으로 갔을 때, 번개구름인지(1) 아닌지 체크하고
        # 갈 수 있으면 idx += 2
        # (이 때 2칸 앞으로 가는 경우가 list를 벗어나는지 확인)
        if idx + 2 <= goal_idx and c[idx + 2] == 0:
            idx += 2
        # 갈수 없으면 += 1
        elif c[idx + 1] == 0:
            idx += 1
        # 한 번 움직였으므로 count += 1
        count += 1
    return count



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = 6

    c = [0, 0, 0, 1, 0, 0]
    # c = [0, 0, 1, 0, 0, 1, 0]

    # n = int(input())

    # c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
