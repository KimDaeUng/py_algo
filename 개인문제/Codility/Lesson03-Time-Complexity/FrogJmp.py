# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    q, r = divmod(X - Y, D)
    if r == 0:
        return q
    else:
        return q + 1