# https://programmers.co.kr/learn/courses/30/lessons/42885
# 19:40-20:54 : 해결 못함
# My Solution
'''
구명보트를 최대한 적게 사용해 모든 사람을 구출
매번 최대의 인원수를 실어나를 수 있는 경우를 선택해 필요한 구명보트 개수를 출력
-> 반례 : [10, 10, 20, 20, 30, 30], limit = 40이면
[30]
[30]
[20]
[10, 10, 20]

-> 4
[10, 30]
[10, 30]
[20, 20]
-> 3

큰 값부터 먼저 담되, 그 다음부터는 모든 원소에서 나머지 빈 공간을 채울 때까지 탐색
[30]      | [10, 10, 20, 20, 30]
[30, 10]  | [10, 20, 20, 30] -> count += 1
[30]      | [10, 20, 20]
[30, 10]  | [20, 20] -> count += 1
[20]      | [20]
[20, 20]  | [] -> count += 1 -> return answer
'''

# My Solution : Retry2
'''
이전 풀이와 비슷하나 가장 무거운 사람 + 가장 가벼운 사람 조합으로 탐색
가장 가벼운 사람을 더했는데도 무게가 나간다 -> 뒤에 더 탐색할 필요 없음
가장 무거운 사람 쪽에서 가벼운 사람 쪽으로 탐색하는 것은 탐색 초반에 무거운 무게부터 탐색하므로
탐색 시간이 오래걸림
? : deque로 하지 않으면 시간초과로 통과 불가
'''
from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while len(people) >= 2:
        total = people.pop()
        if total + people[0] <= limit:
            people.popleft()
        answer += 1
    if len(people) == 1:
        answer += 1
    return answer

# My Solution : Retry : 보트 최대 인원 2 조건 : 시간초과
def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        people_sum = people.pop()
        next_i = len(people) - 1
        while 0 <= next_i and people_sum + people[next_i] > limit:
            next_i -= 1
        if 0 <= next_i:
            # people_sum += people[next_i]
            del people[next_i]
            
        answer += 1
    return answer


people = [10, 10, 20, 20, 30, 30]
limit = 40
print(solution(people, limit))


# Solution
# https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python
from collections import deque

def solution(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)
    w = 0
    cnt = 0
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1
    return boat

# Solution 2 
# deque 이용하지 않고, 인덱싱만으로 품
def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    # 짝 지었을때만 2명씩 boat를 타므로, 전체 인원에서 짝지은 수를 빼면 보트의 수
    return len(people) - answer