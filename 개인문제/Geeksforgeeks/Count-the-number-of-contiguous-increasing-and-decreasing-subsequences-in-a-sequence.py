arr = [80, 50, 60, 70, 40]
n = len(arr)
dpi = [1] * (n + 1)
dpd = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if dpi[j] < dpi[i]:
            dpi[i] = dpi[j] + 1
        if dpd[j] > dpd[i]:
            dpd[i] = dpd[j] + 1
print(dpi)
print(dpd)
print(max(dpi), max(dpd))

# Solution
def n_of_seq(arr, n):
    i, inc_count, dec_count = 0, 0, 0
    max_, min_ = [0] * n, [0] * n
    # k2, k1 are used to store the
    # count of max and min arry
    k1, k2 = 0, 0

    # Comparison to store the index of
    # first element of array
    if (arr[0] < arr[1]):
        min_[k1] = 0
        k1 += 1
    else:
        max_[k2] = 0
        k2 += 1
    
    # Comparison to store the index
    # from second to second last
    # index of array
    for i in range(1, n - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            min_[k1] = i
            k1 += 1

        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            max_[k2] = i
            k2 += 1

    # Comparison to store the index
    # of last element of array
    if (arr[n - 1] < arr[n - 2]):
        min_[k1] = n - 1
        k1 += 1
    else:
        max_[k2] = n - 1
        k2 += 1
    
    # Count of number of maximul contiguous
    # increasing and decreasing subsequences
    if (min[0] == 0):
        inc_count = k2
        dec_count = k1 - 1
    else:
        inc_count = k2 - 1
        dec_count = k1

    
    