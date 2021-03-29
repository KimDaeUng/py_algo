# Initialize the DP table
d = [0] * 100

# f(1) = f(2) = 1
d[1], d[2] = 1, 1
n = 99

# Fibonacci Function (Iterative)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])