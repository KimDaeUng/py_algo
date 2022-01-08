# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

'''
시뮬레이션이 아닌 수학문제
P1, P2 각각이 이길 조건을 따져서 조건문에 따라 답을 리턴
1. 1개의 타워(n == 1)인 경우
 - 하나의 타워 높이가 1인 경우(m == 1) : P1은 손쓸 수 없음 P2 승리
 - 하나의 타워 높이가 2이상인 경우(m >= 2) : P1이 1로 만들면 P2는 손쓸 수 없음 P1 승리
2. 2개 이상의 타워(n >= 2)인 경우
 - 타워 개수가 짝수 : P2가 P1대로 따라하면 P1이 못 움직이므로 P2 승리
 - 타워 개수가 홀수 : P1이 첫타워를 1로 만듦 -> 타워개수가 짝수인데 P2와 P1의 순서가 뒤바뀐 상황 -> P1 승리
'''

def towerBreakers(n, m):
    # Write your code here
    if m == 1 or n % 2 == 0:
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
