# https://www.acmicpc.net/problem/2504
# 14:12 - 15:27
string = '''(()[[]])([])'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

# My Solution : Retry
# 괄호가 여러개 중첩되었을 때의 괄호 내부값의 계산 아이디어를 coef로 해결
arr = input()
st_s = 0
st_b = 0
coef = 1
is_paired = True
ans = 0

for i in range(len(arr)):
    if arr[i] == '(':
        st_s += 1
        coef *= 2
    elif arr[i] == '[':
        st_b += 1
        coef *= 3
    elif arr[i] == ')':
        if st_s:
            st_s -= 1
            if arr[i - 1] == '(':
                ans += coef
            coef //= 2
        else:
            is_paired = False
            break
    elif arr[i] == ']':
        if st_b:
            st_b -= 1
            if arr[i - 1] == '[':
                ans += coef
            coef //= 3
        else:
            is_paired = False

if is_paired and not st_s and not st_b:
    print(ans)
else:
    print(0)

# My Solution : Fail
# 재귀 탐색
# 직전에 오는 여는 괄호에 대해 닫는 괄호가 나오면 재귀를 종료, 값을 출력
# 괄호 내부값의 합 * 괄호에 의해 곱해지는 값
# data = input()

# def cal(i, arr, now):

#     if i == len(arr):
#         return now, i
#     if i > 0 and arr[i - 1] == '(' and arr[i] == ')':
#         return 2, i + 1
#     if i > 0 and arr[i - 1] == '[' and arr[i] == ']':
#         return 3, i + 1

#     next_i = None
#     result = now
#     if arr[i] == '(':
#         mid_result, next_i =  cal(i + 1, arr, 0)
#         result += mid_result
#     elif arr[i] == '[':
#         mid_result, next_i =  cal(i + 1, arr, 0)
#         result += mid_result
    
#     if next_i is not None:
#         if arr[next_i] == ')':
#             return cal(next_i + 1, arr, result * 2)
#         elif arr[next_i] == ']':
#             return cal(next_i + 1, arr, result * 3)
#         else:
#             return cal(next_i + 1, arr, result)
#     else:
#         if arr[i + 1] == ')':
#             return cal(i + 2, arr, result * 2)
#         elif arr[i + 1] == ']':
#             return cal(i + 2, arr, result * 3)
#         else:
#             return cal(i + 2, arr, result)
# result = cal(0, data, 0)
# print(result)

# Solution : Stack
s = input().strip()

st_s = []
st_b = []
coeff = 1
is_paired = True
ans = 0

for i in range(len(s)):
    # 여는 괄호를 스택에 추가
    # coeff를 곱하는 이유 : 소괄호, 대괄호 중첩처리
    if s[i] == '(':
        st_s.append(i)
        coeff *= 2
    elif s[i] == '[':
        st_b.append(i)
        coeff *= 3

    # 닫는 괄호가 나왔을 떄 여는 괄호 하나를 스택에서 빼고, 현재 괄호에 대한 coeff 효과를 초기화
    # 현재 인덱스 직전이 여는 괄호면 현재 coeff를 정답에 추가한다.
    # 비어있다면, 짝이 맞지 않는 것이므로 is_pared = False 처리후 for문을 종료
    elif s[i] == ')':
        if st_s:
            if s[i - 1] == '(':
                ans += coeff
            st_s.pop()
            coeff //= 2
        else:
            is_paired = False
            break
    elif s[i] == ']':
        if st_b:
            if s[i - 1] == '[':
                ans += coeff
            st_b.pop()
            coeff //= 3
        else:
            is_paired = False
            break

if not st_b and not st_s and is_paired:
    print(ans)
else:
    print(0)