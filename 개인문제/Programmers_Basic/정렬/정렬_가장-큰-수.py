# 17:10-17:33
# 문자열로 sorting 후 차례대로 붙이기
# 9, 8, 7, ...
# 예외처리 : 첫 자리가 동일하지만 0이 더 붙은 경우
# - 9, 5, 34, 30, 3 (정렬된 형태 그대로 붙인 경우)
# - 9, 5, 34, 3, 30 (실제로 더 큰 수)
# - 9, 5, 34, 3, 30 (실제로 더 큰 수)

# My Solution 1(Failed) : Time limit exceeded
from itertools import permutations
def solution(numbers):
    numbers_str = list(map(str, numbers))
    result = permutations(numbers_str, len(numbers_str))
    return str(sorted(list(map(int, list(map(lambda x : ''.join(list(x)), result)))))[-1])

def solution(numbers):
    len_arr = len(numbers)
    numbers = list(map(str, numbers))
    for i in range(len_arr-1):
        for j in range(len_arr-1-i):
            if numbers[j] + numbers[j + 1] <= numbers[j + 1] + numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return ''.join(map(str, map(int, numbers)))

# My Solution 2(Retry) : using sort key by lambda function
# 예외처리 : 첫 자리가 동일하지만 0이 더 붙은 경우
# - 9, 5, 34, 30, 3 (정렬된 형태 그대로 붙인 경우)
# - 9, 5, 34, 3, 30 (실제로 더 큰 수)
# 내림차순 정렬시 동일한 문자가 등장하지 않을때까지 비교하며, 문자가 더 붙은 경우가 값이 더 큰 경우로 처리됨
# 앞자리가 큰 순으로 정렬되어야하므로 30과 3을 역순으로 정렬시 3이 앞에오게 하기 위해선
# 두 번째 자리 이후의 수도 3이 더 크도록 비교해야 -> 333 vs 3030

def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key = lambda x: x*3, reverse=True))))

# Solution 1: compare key를 이용한 정렬
# https://pslog-eraser.tistory.com/19
import functools

def comparator(a,b):
    '''
    -1 : 앞의 인자가 더 작다
     0 : 두 인자가 같다
     1 : 앞의 인자가 더 크다
    '''
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# Solution 2: Quick Sort 이용한 방법
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


# Programmers 제출 답안
def solution(numbers):
    def compare(n1, n2):
        return n1 + n2 > n2 + n1

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
        return low

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

    l = 0
    r = len(numbers) - 1
    numbers = list(map(str, numbers))
    quick_sort(numbers, l, r)
    
    return str(int("".join(numbers)))