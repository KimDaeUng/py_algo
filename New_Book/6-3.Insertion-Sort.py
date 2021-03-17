data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(data)):
    # 인덱스 i부터 1까지 감소하여 반복
    for j in range(i, 0, -1): 
        # 왼쪽에 있는 값보다 작으면 왼쪽으로 한 칸씩 이동
        if data[j] < data[j - 1]:
            data[j - 1], data[j] = data[j], data[j - 1]
        #  자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break
print(data)