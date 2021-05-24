# https://www.acmicpc.net/problem/10816
# 00:30-01:00
# My Solution
# 중복 원소가 있는 이분탐색
# lower bound, upper bound를 구한뒤
# 두 인덱스간의 거리를 이용해 개수 카운팅

string = '''10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)


n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()

# 1. lower bound
def bs_left(arr, target):
    L = 0
    R = len(arr)
    '''
    모든 데이터가 target 보다 작을 경우, 데이터 범위 밖의 값을 리턴해야 하기 때문에
    일반적인 이분 탐색과 달리 right가 len(array)가 된다.
    또한 target을 찾았을 때 끝내는 것이 아닌 (return mid)가 아닌
    left, right를 조절해 범위를 찾는다.
    -> target == arr[mid] 일 때
       -> 오른쪽을 날리면 lower bound
       -> 왼쪽을 날리면 upper bound(이 때 target을 초과하는 첫 번째 수의 인덱스가 left에 해당)
    '''
    while L < R:
        mid = (L + R) // 2
        # target == arr[mid] 일때 R을 mid로 갱신(오른쪽 날림)
        if target <= arr[mid]:
            R = mid
        else:
            L = mid + 1
    return L

# 2. upper bound
def bs_right(arr, target):
    L = 0
    R = len(arr)
    while L < R:
        mid = (L + R) // 2
        # target == arr[mid] 일때 L을 mid + 1로 갱신
        # (왼쪽 날림, target을 초과하는 첫 번째 수의 인덱스)
        if target >= arr[mid]:
            L = mid + 1
        else:
            R = mid
    return L - 1

def cal_span(arr, target):
    r_idx = bs_right(arr, target)
    l_idx = bs_left(arr, target)
    return r_idx - l_idx + 1
for d in arr_m:
    print(cal_span(arr_n, d), end=' ')