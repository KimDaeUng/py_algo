# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# 20m

# My Solution
# https://app.codility.com/demo/results/trainingJU26SW-JDM/
def solution(A):
    east_cnt = 0
    answer = 0 
    for car in A:
        if car == 0:
            east_cnt += 1
        else:
            answer += east_cnt

    if answer > 1000000000:
        return -1
    else:
        return answer