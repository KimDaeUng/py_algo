# 중복원소가 있는 이분탐색에서
# 각각 왼쪽과 오른쪽에 있는 값을 찾는 알고리즘을 정리

# Ref:
# - https://lemidia.github.io/algorithm/binary-search/
# - https://velog.io/@kgh732/Python%EC%9C%BC%EB%A1%9C-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89Binary-Search
data = [1, 2, 4, 4, 4, 5, 6, 7]

# Introduction) 기본형
# - 탐색 결과가 mid에 저장되게 하는 방법(L = mid = R)
# - target의 존재성 파악은 가능, 그러나 중복원소의 시작과 끝은 파악 불가
def binary_search(array, target):
    L = 0
    R = len(array) - 1

    while L <= R:
        mid = (L + R) // 2
        if array[mid] > target: # Move to left
            right = mid - 1
        elif array[mid] < target: # Move to right
            left = mid + 1
        else: # Correct
            return mid
    # Incorrect
    return - 1

# 4를 맨 처음으로 발견한 위치를 출력함
print(binary_search(data, 4))

# lower bound와 uppper bound 찾는 방법
# 1. lower_bound 찾기
# target보다 같거나 큰 값 중 가장 앞에 있는 원소의 위치
def binary_search_lower(array, target):
    L = 0
    R = len(array)
    # 모든 데이터가 target보다 작을 경우 데이터 범위 밖의 값을 리턴해야 하기 때문에
    # 일반적인 이분탐색과 달리 right가 len(array)가 된다.
    # 또한, target을 찾았을 때 끝내는 것이 아닌(return mid가 아닌)
    # left/right를 조절해서 범위를 찾는다.
    # -> target == array[mid] 일때
    #     -> 오른쪽을 날리면 lower bound
    #     -> 왼쪽을 날리면 upper bound(이때 target을 초과하는 첫번째 수의 인덱스가 left에 할당)
    while L < R:
        mid = (L + R) // 2
        if target <= array[mid]:
            R = mid
        else:
            L = mid + 1
    return L

# 2. upper_bound 찾기
# target과 같거나 큰 값 중 가장 앞에 있는 원소의 위치
def binary_search_upper(array, target):
    L = 0
    R = len(array)
    while L < R:
        mid = (L + R) // 2
        if target >= array[mid]:
            L = mid + 1
        else:
            R = mid
    return L - 1

print(binary_search_lower(data, 4))
print(binary_search_upper(data, 4))