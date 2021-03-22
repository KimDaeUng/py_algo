'''
bisect: 이진탐색 구현을 위한 라이브러리 
'정렬된 배열'에서 특정 원소를 찾아야 할 때 사용됨
# 다음 두 함수가 가장 중요하게 사용되며, 시간 복잡도 O(logN)
- bisect_left(a, x): 정렬된 순서를 유지하면서
  리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x): 정렬된 순서를 유지하면서
  리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
예를 들어 정렬된 리스트 [1, 2, 4, 4, 8]이 있을 떄,
새롭게 데이터 4를 삽입하려 한다 가정하자.
이때 bisect_left(a, 4)와 bisect_right(a, 4)는
각각 인덱스 값으로 2와 4를 반환
'''

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))