# 19:16-19:55
'''
# 최초시도: 재귀함수이용, 엄밀히는 DP가 아닌 완전탐색
# 솔루션 : 전혀 감이 오지 않는다... 어떻게 이렇게 생각하지?
- 곱한다는 것도 결국 덧셈의 반복으로 봄
- DP table의 인덱스 자체가 금액이 될 거라 생각 못함, 계수정렬 같은 느낌?
- 각 화폐 단위 k 마다 모든 금액 i에 대해
  (i번째까지의 최소 화폐 수) = min[ (i번째까지의 최소 화폐 수), (i - k 번째까지의 최소 화폐 수) + 1]

'''
# Retry
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

# DP Table
dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(data[i], m + 1):
        if dp[j - data[i]] != 10001:
            dp[j] = min(dp[j], dp[j - data[i]] + 1)

if data[m] == 10001:
    print(-1)
else:
    print(data[m])

# My Solution (failed...?)
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

# 최소한의 화폐 개수
data.sort(reverse=True)

min_n_coin = 10000


def recursive(value, n_coin):
    global min_n_coin

    if value < 0:
        return None
    # 종료조건, 코인을 다 구성하면
    if value == 0:
        min_n_coin = min(n_coin, min_n_coin)
        return None
    # 모든 화폐 종류들에 대해서 나눗셈 및 뺄셈 전부 수행
    for money in data:
        # 1. 나눗셈
        quotient, remaineder = divmod(value, money)
        if quotient >= 1:
            # 나눠떨어질 경우, 몫(동전 개수)를 n_coin에 더함,
            # min_n_coin 새로 갱신
            if remaineder == 0:
                min_n_coin = min(quotient + n_coin, min_n_coin)
            # 나눠떨어지지 않을 경우, 남은 금액(remainder)와 동전 수 + 몫의 동전 개수로 재귀
            else:
                recursive(remaineder, quotient + n_coin)
        
        # 2. 뺄셈
        # 0보다 크거나 같을 경우에만 재귀, n_coin + 1
        if value - money >= 0:
            recursive(value - money, n_coin + 1)
    
    # 실패해서 변화가 없는 경우 -1 출력
    if min_n_coin == 10000:
        min_n_coin = -1
    return None

recursive(m, 0)
print(min_n_coin)

# Solution
'''
각 dp 테이블은 인덱스 i를 금액으로 하고,
각 인덱스마다 그 금액을 만들기 위해 필요한 최소 화폐의 개수를 저장한다.
화폐의 단위를 k라고 할 때 (k = {2, 3, 5, ...}) 
금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i,
a_{i-k}를 (i에 k를 더하기 전의 금액인) i-k 원을 만들 수 있는 최소한의 화폐 개수라 할 때
1. a_{i-k}를 만드는 방법이 존재하는 경우, a_i = min(a_i, a_{i - k} + 1) [기존 개수와 비교해 더 작은 것으로 갱신]
2. a_{i-k}를 만드는 방법이 존재하지 않는 경우, a_i = 10001

위 점화식을 모든 화폐 단위에 대해서 차례대로 적용한다.
먼저 가장 큰 화폐단위 K 크기 만큼의 리스트를 할당한후,
각 인덱스를 '금액'으로하여 메모이제이션을 실행

'''
# 정수 N, M을 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# Dynamic Programming (Bottom-Up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # (i - k) 원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])