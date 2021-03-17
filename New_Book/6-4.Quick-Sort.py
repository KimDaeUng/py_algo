data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(data, start, end):
    # 원소 개수 1일 때 종료
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while left <= end and data[left] <= data[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and data[right] >= data[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗 교체
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            data[left], data[right] = data[right], data[left]
    
    # 분할 후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)

quick_sort(data, 0, len(data) - 1)
print(data)

