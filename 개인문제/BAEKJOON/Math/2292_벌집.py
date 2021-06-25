# https://www.acmicpc.net/problem/2292
# 6, 12, 18, ... 
# 14:31-17:08
# My Solution : 계차수열이 포함된 수열 이용
'''
6각형으로 둘러싸는 시작수와 끝수로 이뤄진 수열(아래에서 2, 7, 19, 37)의 규칙을 살펴보면
해당 수열이 계차수열을 포함하는 수열임을 알 수 있음

수       2,  7,  19,  37  ...
계차(b_k)   6   12   18    ...
계차항번호    1    2    3    ...

# 원래 수열인 a(n) = 2 + (n - 1)까지 계차 수열 b_k의 합
  a(n) = 2 + Sum_{k = 1}^{n - 1}b_k

# b_k는  초항 6, 공차 6인 등차 수열이므로 1부터 n-1까지의 합은
  Sum_{k = 1}^{n - 1}b_k = (n - 1) * (6 + 6 * (n - 1)) / 2
  이고 따라서 원래 수열 a(n)의 일반항은

  a(n) = a_1 + (n - 1) * (6 + 6 * (n - 1)) / 2
       =   2 + (n - 1) * (6 + 6 * (n - 1)) / 2

# 어떤 수 T까지의 거리는 시작점을 포함한 1과
  T보다 작거나 같은 수열 a(n)의 항 중 최대값의 항 번호 k의 합
  distance(T) = 1, where T == 1
  distance(T) = 1 + argmax_k[a(k)], where a(k) <= T, T >= 2
  ex) target = 13,
      6각형 거리 = 1 + 2 (2번째 항 12) = 3
'''

t = int(input())
answer = 1

if t == 1:
    pass
else:
    for k in range(1, t + 1):
        # target인 t을 넘어서는 최초의 k에서 멈춰도
        # 시작점 1을 더한 것과 같은 효과
        if  t < 2 + (k - 1) * (6 + 6 * (k - 1)) / 2:
            answer = k
            break
print(answer)

# Solution:
'''
주어진 N에 대하여 
N :     1  /  2 ~ 7   /  8 ~ 19 /  20 ~ 37 / ...
갯수 :   1개 /   6개    /   12개   /   18개   / ...
출력 :    1  /    2    /     3   /     4    / ...

1을 제외한 +6개씩 누적되어 늘어나는 규칙
'''

# Solution 1: While
# idea: 시작점을 제외한 나머지 조각들로 6각형을 몇겹 감쌀 수 있는지 센다.
#       구체적인 인덱스번호 X, 덩어리로 보고 지워가며 카운트
# N이 1보다 큰 범위일 동안(시작점 제외) 6, 12, 18씩 빼나가기
N = int(input())
cnt = 1
while N > 1:
    N -= (6 * cnt)
    cnt += 1
print(cnt)

# Solution 2: Recursive
import sys
# 재귀함수 깊이 제한 확장
sys.setrecursionlimit(10**5)
N = int(input())
def bee_house(N, cnt):
    if N <= 1:
        return cnt
    else:
        return bee_house(N - (6 * cnt), cnt + 1)
print(bee_house(N, 1))