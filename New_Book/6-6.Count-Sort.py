# 모든 원소의 값이 0보다 크거나 같다고 가정
data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 9, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값 0으로 초기화)
count = [0] * (max(data) + 1)

# 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(data)):
    count[data[i]] += 1 

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')