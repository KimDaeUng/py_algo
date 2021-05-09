# https://programmers.co.kr/learn/courses/30/lessons/42584
# 00:45-

# My Solution : 완전 탐색, 매 원소마다 떨어지지 않는 기간 계산
# 인덱싱 사용해 prices 원소 접근 및 len(prices) 사용시 시간초과
# 효율성 테스트 약 70ms
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    
    prices = deque(prices)
    idx = 0
    while prices:
        cur_p = prices.popleft()
        dura = 0
        for p in prices:
            dura += 1
            if cur_p > p:
                break
        answer[idx] = dura
        idx += 1
    
    return answer

# Solution : Stack을 이용한 풀이
# 효율성 테스트 약 30ms
'''
주식가격이 유지되거나 올랐으면 +, 떨어지면 끝.
아직까지 떨어지지 않은 주식 가격들의 큐를 만들고, price를 만나면서 떨어졌는지 확인
st : 아직 떨어지지 않은 시간들의 모음(인덱스)

# 핵심
price에 해당하는 index를 st에 저장
현실의 시간을 index로 생각에 stack으로 저장한 다음에 
appen, pop 하면서 answer에 기록

# 정리
매 시간 마다 이전의 가장 마지막 가격들과 가격을 비교
1. 이전 가격 > 현재 가격이면 현재 시점에서 가격 하락이 시작된 것이므로
  stack에서 이전 가격을 pop하여 제거,
  이전 가격 기준으로 가격이 떨어지지 않은 기간은
  (현재 시점 - 이전 가격 시점)이므로,
  이를 answer[이전가격시점] = (현재 시점 - 이전 가격 시점)에 저장
  이후 남은 stack의 시점 들에 대해서도 1을 반복, 가격 하락이 아니라면 2로 진행
2. 반대로 이전 가격 <= 현재 가격이면 가격 하락 X이므로 stack에 현재 시각 i 추가
3. st에는 종료시까지 가격이 떨어지지 않은 시점들이 담김
   그 시점부터 종료시까지 남은 시간을 계산해 answer list에 해당 위치에 기록
   answer[i] = n - i - 1
'''

def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    st = [] # 아직 떨어지지 않은 시간 인덱스

    for i in range(n):
        # 현재 가격 보다 제일 마지막 가격이 더 크면, 주식값이 내림을 의미
        # prices[st[-1]] : 마지막으로 주식이 떨어지지 않은 시간이 언제인지를 보고, 그 시각의 주식 가격을 보는 것
        while st and prices[st[-1]] > prices[i]:
            top = st.pop()
            answer[top] = i - top 
        st.append(i)

    while st:
        top = st.pop()
        answer[top] = n - top - 1
            
    return answer

# Example
'''
i = 0
prices [1, 2, 3, 2, 3]
st     []
--------------
i = 1
prices [1, 2, 3, 2, 3]
st     [0]
  prices[st[-1]] = prices[0] = 1
  prices[1] = 2
  -> 1 > 2 => False -> st.append(1)
--------------
i = 2
prices [1, 2, 3, 2, 3]
st     [0, 1]
  prices[st[-1]] = prices[1] = 2
  prices[2] = 3
  -> 2 > 3 => False -> st.append(2)
--------------
i = 3
prices [1, 2, 3, 2, 3]
st     [0, 1, 2]
  prices[st[-1]] = prices[2] = 3
  prices[3] = 2
  -> 3 > 2 => True : 2초일 때 가격 > 3초일 때의 가격 : 가격 하락
  st.pop() : st에서 떨어지기 시작한 가격인 2를 제거(pop)
  -> st = [0, 1] top = 2
  2번째 인덱스가 가격이 떨어지지 않은 기간은
  answer[top] = answer[2] = i - top = 3 - 2 = 1
  -> answer = [0, 0, 1, 0, 0]
! 처음으로 가격 하락 발생한 현 시점 i = 3 기준으로
  i = 2 는 확인 되었으니 i = 1, 0 에 대해서 거슬러 올라가며 가격하락에 해당하는지 확인한다
prices [1, 2, 3, 2, 3]
st     [0, 1]
  prices[st[-1]] = prices[1] = 2
  prices[3] = 2
  -> 2 > 3 => False : 1초일 때 가격 < 3초일 때 가격 : 현재 시점 3초의 가격이 1초일 때 가격보다 하락하지 않았다.
  st.append(3)
--------------
i = 4
prices [1, 2, 3, 2, 3]
st     [0, 1, 3]
  prices[st[-1]] = prices[3] = 2
  prices[4] = 3
  -> 2 > 3 => False
  st.append(4)
--------------
for loop end
prices [1, 2, 3, 2, 3]
st     [0, 1, 3, 4]
answer [0, 0, 2, 0, 0]
st는 끝까지 안내린 시점의 인덱스들
-> 전체 길이 - 인덱스 번호 - 1
'''