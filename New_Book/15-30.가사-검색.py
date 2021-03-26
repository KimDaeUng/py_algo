# https://programmers.co.kr/learn/courses/30/lessons/60060
# 18:47-19:41 해결 못 함
# 약 6시간 넘게 시도
'''
# 최초 실패한 시도:
1. words와 queries의 각 단어를 길이 오름차순, 알파벳순으로 정렬한다. (2*O(NlogN))
2. 전체 쿼리를 순회하며 각 query 마다 ?의 시작과 끝 위치를 찾고 (N*O(logN))
   전체 words를 순회하며 길이가 일치하는 경우, (*N)
    시작과 끝 위치의 값을 슬라이싱해 일치할 때마다 카운트
-->(O(NlogN + N^2*logN)) 약 O(N^2) ?
'''

# Retry
'''
- words를 길이(length)별로 별도의 리스트에 저장한 뒤 각각을 sort 해두고 이를 array[length]라 하자.
  (이전 시도에서는 상관없는 길이를 전체 다돌아서 비효율적이었음)
  또한 words를 뒤집은 값을 동일하게 처리하여 저장한 배열을 reversed_array[length]라 하자.
- 정답을 저장할 빈 리스트 answer 를 만든다.
- queries 리스트의 각 쿼리 q를 모두 순회하면서
  q의 길이와 동일한 words의 후보리스트를 불러온다. (array[len(q)])
- 그 다음 쿼리의 와일드카드의 위치에 따라 분기한다.
- 1. 접미사에 와일드카드가 있는 경우
     와일드카드처리된 부분에서 나올 수 있는
     가장 빠른 단어(와일드카드를 'a'로 대체한 단어)와
     가장 느린 단어(와일드카드를 'z'로 대체한 단어)를 시작값과 끝값으로 하여
     words의 후보리스트에서 그 개수를 구한다.
     (각각 중복된 값을 포함하는 이분탐색에서 lower_bound와 upper_bound를 
     구하는 이분탐색을 수행하여 구한 뒤, 두 값의 차를 계산)
     ex) fr??? -> start_value : fraaa / end_value : frzzz
- 2. 접두사에 와일드카드가 있는 경우
    와일드카드부터 시작할 경우, 위와 같은 방식대로 하면 다음 예시처럼 시작과 끝 값이
    words 후보리스트의 양끝값이 되어 제대로 계산되지 않는다.
    ex) ????o -> aaaao zzzzo
    따라서 각 단어를 뒤집어 처리한다(reversed_array[len(q)] 사용)
- 각 분기마다 계산한 값을 answer에 append 시키고,
  모든 queries의 원소에 대해 처리가 끝나면 answer를 반환한다.

'''
from collections import defaultdict

def find_lower(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if target <= arr[mid]:
            end = mid
        else:
            start = mid + 1
    return start

def find_upper(arr, target):
    # return the first index followed by target
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if target >= arr[mid]:
            start = mid + 1
        else:
            end = mid
    return start

def count_by_range(arr, start_value, end_value):
    upper_bound = find_upper(arr, end_value)
    lower_bound = find_lower(arr, start_value)
    return upper_bound - lower_bound

def solution(words, queries):
    
    array = defaultdict(list)
    reversed_array = defaultdict(list)

    answer = []
    min_len, max_len = 100000, 2

    for word in words:
        word_length = len(word)
        min_len = min(min_len, word_length)
        max_len = max(max_len, word_length)
        array[word_length].append(word)
        reversed_array[word_length].append(word[::-1])

    for i in range(min_len, max_len + 1):
        try:
            array[i].sort()
            reversed_array[i].sort()
        except:
            continue
    
    for q in queries:
        # 접미사에 와일드카드
        if q[0] != '?':
            c = count_by_range(array[len(q)],
             q.replace('?', 'a'),
              q.replace('?', 'z'))
        # 접두사에 와일드카드
        else:
            r_q = q[::-1][:]
            c = count_by_range(reversed_array[len(q)],
             r_q.replace('?', 'a'),
              r_q.replace('?', 'z'))
        answer.append(c)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# result : [3, 2, 4, 1, 0]
print(solution(words, queries))

# Solution(Dongbin Book)
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어를 깊이마다 나누어서 저장하기 위한 리스트
array = [ [] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [ [] for _ in range(10001)]

def solution(words, queries):
    answer = []
    # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
    for word in words:
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
    
    # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    # 쿼리를 하나씩 확인하며 처리
    for q in queries:
        # 접미사에 와일드카드가 붙은 경우
        if q[0] != "?":
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        # 접두사에 와일드카드가 붙은 경우
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer