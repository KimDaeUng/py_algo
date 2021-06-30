# https://app.codility.com/c/run/trainingSDCHYR-7VQ/

def solution(N):
    # write your code in Python 3.6
    bin_n = bin(N)[2:]

    count = 0
    max_count = 0

    for i in bin_n:
        if i == '1':
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1
    return max_count