# Recursive
def rec(n):
    if n <= 1:
        return n 
    else:
        return rec(n-1) + rec(n-2)
# Iteration
def iter(n):
    if n <= 1:
        return n 
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= n:
            t9, t1 = t1, t0 + t1
            i += 1
        return t1

# Iterative 2
def solution(n):
    if n <= 1:
        return n
    else:
        f_nm1, f_nm2 = 1, 0
        while n > 1:
            f_n = f_nm1 + f_nm2
            # print(f_n, f_nm1, f_nm2)
            f_nm2 = f_nm1
            f_nm1 = f_n
            n -= 1
    return f_n