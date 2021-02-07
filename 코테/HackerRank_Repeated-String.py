# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# 04:15-04:40

#!/bin/python3

import math
import os
import random
import re
import sys

# 무식하게 풀기
def repeatedString(s, n):

    def _gen():
        i = 0
        len_s = len(s)
        while True:
            yield s[i]
            i += 1
            i %= len_s
    count = 0
    gen = _gen()
    for i in range(n):
        tmp = next(gen)
        if tmp == 'a':
            count += 1
    
    return count

# 규칙 찾아 풀기
def repeatedString(s, n):
    len_s = len(s)
    div, remain = divmod(n, len_s)
    
    # N of 'a' in the piece
    n_a_inpiece = 0
    for i in s:
        if i == 'a':
            n_a_inpiece += 1
    
    s_remain = s[:remain]
    
    # N of 'a' in remains of the piece
    n_a_remain = 0
    for i in s_remain:
        if i == 'a':
            n_a_remain += 1
    
    return div * n_a_inpiece + n_a_remain
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = 'a'

    n = 100000000

    # s = input()

    # n = int(input())

    result = repeatedString(s, n)
    
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
