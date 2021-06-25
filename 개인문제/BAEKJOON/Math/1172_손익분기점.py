# https://www.acmicpc.net/problem/1712
# 14:17-14:31

# My Solution
'''
a : 고정비용
b : 1대 생산에 드는 비용
c : 가격
n : 노트북 판매 수

# if b == c, then a < 0 -> 손익분기점 계산 불가
a + b * n < c * n 이 되는 최초의 n을 구하라
= a + (b - c) * n < 0
= a / (c - b) <  n
-> a / (c - b) 보다 큰 최초의 자연수
'''

a, b, c = map(int, input().split())

if b == c:
    print(-1)
    exit()

answer = (a // (c - b) ) + 1
if answer < 1:
    print(-1)
else:
    print(answer)

# Solution
# https://deokkk9.tistory.com/3
# - 생산량을 n이라 하면 A + B * n = C * N 일 때
#  수입과 비용이 같아지기 때문에 B ≥ C일 경우에 손익
#  분기점이 나타나지 않게 되므로 먼저 검사해서 걸러냄
# - 생상량이 늘어날 때마다 C와 B의 차이만큼 수입과 비용의
#   차이가 줄어들게 되고 따라서 A(C-B) 대 생산했을 때
#   수입과 비용이 같아지기 떄문에 +1 부터 수입이 많아짐

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A / (C - B) + 1))