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