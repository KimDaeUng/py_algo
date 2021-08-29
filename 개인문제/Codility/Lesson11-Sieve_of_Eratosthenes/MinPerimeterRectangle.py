# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
# 20m
# My Solution: 
# https://app.codility.com/demo/results/training8B9WEH-5CJ/
def solution(N):
    n_sqrt = int(N ** 0.5) + 1
    min_peri = int(2e9)
    for i in range(n_sqrt, 0, -1):
        a, r = divmod(N, i)
        if r == 0:
            b = N // a
            peri = 2 * (a + b)
            min_peri = min(min_peri, peri)

    return min_peri