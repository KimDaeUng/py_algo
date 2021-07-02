# https://brownbears.tistory.com/454

'''
# GCD(Greatest Common Divisor)
주어진 두 수 x, y에서 x의 약수이면서 y의 약수인 수 중 최대값을 의미합니다.ㅇ
최대 공약수를 구하는 간단한 방법은 1에서 x와 y중 작은 값의 범위에서 공약수(둘 모두 나머지가 0)를 모두 구한 다음
이 수들 중 최대값을 구하는 방법입니다. 1부터 x또는 y중 작은 값까지 반복하여 값을 구할 수 있지만 유클리드 호제법을
이용하면 간단하게 계산됩니다.

유클리드 호제법의 공식은 다음과 같습니다.

  1. 최대 공약수를 구하는 함수를 gcd(x, y)라고 가정
  2. x % y == 0 이라면 gcd(x, y) = y가 성립
  3. x % y != 0 이라면 gcd(x, y) = gcd(x, x % y)가 성립
  4. 2번이 될 때까지 2-3번을 반복
'''

# GCD Implementation
def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x

def gcd_rec(x, y):
    if y == 0:
        return x
    return gcd_rec(y, x % y)

print(gcd(1071, 1029))

# Built-In Function
from math import gcd
print(gcd(1071, 1029))

'''
# 최소 공배수(Least Common Multiple)
 x, y의 공통 배수 가운데 최소값을 의미한다. 더 쉽게 말해서 최소 공배수는 
 주어진 수인 x,y의 곱에서 x,y의 최대공약수를 나누어 준 것과 같다.
 즉, 유클리드 호제법을 사용해 최대공약수를 구한 다음, x, y를 곱한 값을 나눠주면
 최소공배수를 구할 수 있다.
'''

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(1071, 1029))

# N개의 최소 공배수
'''
먼저 2개의 수에 대해 최소공배수를 구한 다음, 그 값과 계산하지 않은 값들 중 1개를 선택해
다시 최소공배수를 구한다.이렇게 모든 수에 대해 최소공배수를 구하면 N개의 최소공배수를 구할 수 있다.
'''
from math import gcd
def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

print(solution([2, 6, 8, 14]))

# No Built-In
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def solution(num):
    temp = 1
    for i in range(len(num)):
        # lcm = (a*b) / gcd
        # gcd = (a*b) / lcm
        temp = (num[i] * temp) / (gcd(num[i], temp))
    return temp