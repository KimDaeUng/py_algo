data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(data)):
    min_idx = i
    for j in range(i + 1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
    # Swap
    data[i], data[min_idx] = data[min_idx], data[i]

print(data)