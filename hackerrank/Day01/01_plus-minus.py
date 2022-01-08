# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n_minus = 0.
    n_zero = 0.
    n_plus = 0.
    

    for i in arr:
        if i < 0:
            n_minus += 1.
        elif i == 0:
            n_zero += 1.
        else:
            n_plus += 1.
    
    answer = [n_plus, n_minus, n_zero]
    n_total = sum(answer)
    
    for cnt in answer:
        print("{:.6f}".format(cnt/n_total))
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
