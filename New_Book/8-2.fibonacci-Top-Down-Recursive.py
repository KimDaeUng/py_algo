# Initialize the Memoization List
d = [0] * 100

# Fibonacci Function (Recursive, Top-Down DP)
def fibo(x):
    # END Condition(Return 1 when x == 1 or 2)
    if x == 1 or x == 2:
        return 1
    # If it has been calculated, return that value
    if d[x] != 0:
        return d[x]
    # Not calculated, return value by calculating
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))