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

# 사용자가 정의한 대소 관계를 이용해 정렬(내림차순)
# https://eda-ai-lab.tistory.com/467
def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1) # 내림차순
    # return str(n1) + str(n2) < str(n2) + str(n1) # 오름차순

def partition(nums, l, r):
    # print(nums, l, r)
    # low는 compare 비교 방식에 따라 현재까지 확인된
    # 가장 낮은 우선 순위의 값을 가리키는 포인터
    # 왼쪽에서 부터 차례대로 오른쪽 제일 끝 원소 nums[r]과 비교하여
    # compare를 만족하면 low와 위치 swap, 즉 현재까지 추적된
    # 우선순위가 가장 낮은 원소(compare를 만족하지 않는 원소)와 swap.
    # 최종적으로 low가 가리키는 위치의 왼쪽은 nums[r]보다 큰 값, 오른쪽은 작은값이 위치
    # 모든 원소를 정렬한 것은 아니지만 적어도 하나의 원소의 순위 확정해 위 아래로만 정렬하면 됌

    low = l
    while l < r:
        # l + r > r + l 이면
        if compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    
    # 가장 낮은 순위 low를 가장 오른쪽 r과 변경
    # 여기서 r은 분할정복으로 들어와서 들어온 값 중 가장 마지막값
    nums[low], nums[r] = nums[r], nums[low]
    print(nums)
    return low

# 위의 partition 함수는 기능적으로 아래 함수와 동일함
'''
def partition(nums, l, r):
    pivot = r
    end = r - 1
    start = l 
    
    while l < r:
        # compare를 만족하지 않는 데이터를 찾을 때까지 반복
        while l <= end and compare(nums[l], nums[pivot]):
            l += 1
        # compare를 만족하는 데이터를 찾을 때까지 반복
        while r > start and not compare(nums[r], nums[pivot]):
            r -= 1
        # 엇갈렸다면 compare == False인 데이터(오른쪽)와 pivot 교체
        if l > r:
            nums[l], nums[pivot] = nums[pivot], nums[l]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            nums[l], nums[r] = nums[r], nums[l]

    return l
'''

def quick_sort(nums, l, r):
    if l >= r:
        return
    
    # partion 함수를 실행하면 r을 pivot으로 하여 
    # compare 함수의 대소 비교 기준으로 내림차순 정렬하며
    # 이때 pivot r의 내림차순 정렬시 정확한 Index가 반환된다.
    # nums는 nums[pos]를 기준으로 왼쪽과 오른쪽의 상대적 대소만 정렬된 상태
    # 재귀호출을 통해 각 분할을 정렬한다

    pos = partition(nums, l, r)
    quick_sort(nums, l, pos - 1)
    quick_sort(nums, pos + 1, r)
    

# Test
nums = [34, 30, 2, 5, 9, 3]
l = 0
r = len(nums) - 1

print(nums)
print(partition(nums, l, r))
print(nums)