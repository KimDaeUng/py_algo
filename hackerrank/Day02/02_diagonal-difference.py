# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    l2r = 0
    r2l = 0
    
    """
    N = 5
    left to right : (0, 0), (1, 1), (2, 2), ..., (4, 4)
    (i , i)
    right to left : (0, 4), (1, 3), (2, 2), ..., (4, 0)
    (i, N - 1 - i)
    """
    
    N = len(arr)
    
    for row in range(N):
        for col in range(N):
            if row == col:
                l2r += arr[row][col]
            if col == (N - 1 - row):
                r2l += arr[row][col]
    
    return abs(l2r - r2l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
