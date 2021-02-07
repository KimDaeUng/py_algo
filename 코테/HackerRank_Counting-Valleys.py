# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# 이전에 풀었던 유사한 문제 - 문자열 뒤집기

# 여기선 D 다음 U가 나타나는 횟수 카운트

# mountains : 해수면 기준으로 U 했다가 D 해서 다시 해수면으로 도달한 횟수
# valleys : 해수면 기준으로 D 했다가 U 해서 다시 해수면으로 도달한 횟수

# 현재 높이를 나타내는 변수를 만들고 이 값이 0 미만 되었다가 다시 0이 되면 카운트
# 00:30-01:10(40m)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # 1. Record Sea-level changes
    sea_level = [0]

    for i, step in enumerate(path):
        if step == "U":
            sea_level.append(sea_level[i]+1)
        else:
            sea_level.append(sea_level[i]-1)
    
    # 2. Only count when meet [negative, 0] case
    len_sea_level = len(sea_level)

    count = 0
    for i in range(1, len_sea_level-1):
        if (sea_level[i+1] == 0 )& (sea_level[i] < 0):
            count += 1
    
    return count
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # steps = int(input().strip())

    # path = input()

    steps = 8

    path = "UDDDUDUU"

    result = countingValleys(steps, path)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
