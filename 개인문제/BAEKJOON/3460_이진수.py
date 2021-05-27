# https://www.acmicpc.net/problem/3460
# 15:30-16:30

# My Solution 1 : 시간 초과
# 내부 while에서 조건문을 세 번, 계산 세 번
# 매번 나머지가 1일 때 인덱스를 출력하면
# 최종적으로 n == 1인 경우 r == 0이되고 해당 케이스를
# 첫번째 if r == 1: 에서 잡아내지 못 한다고 생각하고 if문을 하나 더 작성해 시간초과
# n == 2 -> n == 1이 된 후, 반복문을 한 번 더 돌면 r = n % 2 = 1 이 되어
# if r == 1로도 처리 가능.
t = int(input())
while t > 0:
    n = int(input())
    idx = 0
    while True:
        r = n % 2
        n = n // 2
        if r == 1:print(idx, end=' ') 
        idx += 1
        if n == 1:print(idx, end=' ');break
    t -= 1

# My Solution 2 : 통과 but 정석 X
while t > 0:
    n = int(input())
    idx = 0
    tmp = bin(n)[2:][::-1]
    for i in tmp:
        if i == '1':
            print(idx, end=' ')
        idx += 1
    t -= 1

# My Solution 3 
t = int(input())
while t > 0:
    n = int(input())
    idx = 0
    while n > 0:
        if n % 2 == 1:print(idx, end=' ') 
        n = n // 2
        idx += 1
    t -= 1

# Solution
t = int(input())
for _ in range(t):
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:
            print(i, end=' ')
        n = n//2
        i += 1