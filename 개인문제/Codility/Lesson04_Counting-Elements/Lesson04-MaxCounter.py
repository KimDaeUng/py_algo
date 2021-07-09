# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/start/

# My Solution
# https://app.codility.com/demo/results/trainingVD836C-ZUS/

def solution(N, A):
    counter = [0] * N
    if A.count(N + 1) == len(A):
        return counter
    max_cnt = 0
    for i in A:
        if  i == (N + 1) and (i - 1) != (N + 1):
            counter = [max_cnt] * N
        else:
            counter[i - 1] += 1
            max_cnt = max(max_cnt, counter[i - 1])
    return counter

# Solution
# ref: https://choichumji.tistory.com/89
# 와 진짜 신기하게 풀었네
# 컨셉 요약은 다음 맥스카운터 만나기 전까지 카운터값을 계속 새로 갱신하며 카운팅하는 것
# 매 번 li 딕셔너리에 값을 카운팅 및 최대 카운팅값을 갱신(max_num) 하다가
# max_counter N + 1를 만나면 li 딕셔너리를 비우면서
# max_num을 최종 최대값을 의미하는 max_sum에 누적합하고, max_num을 초기화
# 최종적으로 max_sum으로 전체 카운터를 채우고, 나머지 카운팅 만큼을 카운터에 반영

def solution(N, A):
    li = {i:0 for i in range(1, N + 1)}
    max_sum = 0
    max_num = 0
    for key in A:
        if key == N + 1:
            max_sum += max_num
            li.clear()
            max_num = 0
        else:
            if li.get(key) is None:
                li[key] = 1
            else:
                li[key] += 1
            
            max_num = max(max_num, li[key])

    answer = [max_sum] * N

    for key, val in li.items():
        answer[key - 1] += val
    
    return answer