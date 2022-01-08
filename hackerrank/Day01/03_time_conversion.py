# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?h_l=interview&h_r=next-challenge&h_v=zen&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time, ampm = s[:-2], s[-2:]
    time = time.split(":")
    if ampm == 'AM':
        if int(time[0]) == 12:
            time[0] = "00"
    else:
        if int(time[0]) == 12:
            time[0] = "00"
        time[0] = str(int(time[0]) + 12)
    time = ":".join(time)
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
