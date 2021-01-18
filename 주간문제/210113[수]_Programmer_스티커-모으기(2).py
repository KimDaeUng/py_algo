# https://programmers.co.kr/learn/courses/30/lessons/12971

# 21:42 - 
# 최대가 되도록 -> BFS
# 환형큐 -> deque 사용

# sticker 뜯으면 인접한 것 탐색 불가 -> 전에 풀었던 house robber ?
# -> 

# Ref
# https://train-validation-test.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level-4-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%EB%AA%A8%EC%9C%BC%EA%B8%B02-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://inspirit941.tistory.com/158



def solution(sticker):
    len_sticker = len(sticker)
    if len_sticker <= 4:
        return max(sticker)

    # table[i] = i번째 스티커를 떼는 경우 최댓값
    # 맨 앞 스티커를 떼는지 아닌지 -> 맨 뒤 스티커에 영향을 준다.
    
    # 1. 첫 번째 스티커를 떼는 경우
    table = [ 0 for _ in range(len_sticker)]
    table[0] = sticker[0]
    table[1] = table[0]

    cur_max = 0
    maximum_value1 = 0
    table = [ 0 for _ in range(len_sticker)]

    for i in range(2, len_sticker-1):
        cur_max = table[i] = max(table[i-1], table[i-2] + sticker[i])
        if cur_max > maximum_value1:
            maximum_value1 = cur_max 

    # 2. 맨 앞 스티커를 떼지 않는 경우
    table = [ 0 for _ in range(len_sticker)]
    table[0] = 0
    table[1] = sticker[1]

    cur_max = 0
    maximum_value2 = 0

    for i in range(2, len_sticker):
        cur_max = table[i] = max(table[i-1], table[i-2] + sticker[i])
        if cur_max > maximum_value2:
            maximum_value2 = cur_max 

    return max(maximum_value1,maximum_value2) 