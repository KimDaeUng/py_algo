# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/start/

# My Solution
def solution(A):
    A = list(set(A))
    counter = [0] * 1000001

    for i in A:
        if i > 0 and counter[i] == 0:
            counter[i] = 1
    
    for i in range(1, 1000001):
        if counter[i] == 0:
            return i