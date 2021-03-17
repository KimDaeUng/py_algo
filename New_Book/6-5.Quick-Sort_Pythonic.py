data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(data):
    # 리스트가 하나 이하의 원소만을 담고 있으면 종료
    if len(data) <= 1:
        return data
    
    pivot = data[0] # 피벗은 첫 번째 원소
    tail = data[1:] # 피벗 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분절된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분절된 왼쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(data))