# https://www.acmicpc.net/problem/2941
# 16:35-18:37

# My Solution 2
# https://one-hour.tistory.com/25 를 참고하여 수정
# 가장 오른쪽의 인덱스 기준으로 탐색 문자열을 매번 만들어 체크
# 최초 시도와 의도는 같으나 깔끔한 코드
string = input()
len_s = len(string)
answer = len_s
cro = set(['c=','c-','dz=','d-','lj','nj','s=','z='])

# Case 1, 2
if len_s < 2:
    print(answer)
    exit()
elif len_s == 2:
    if string in cro:
        answer = 1
    print(answer)
    exit()

# Case 3
for i in range(2, len_s + 1):
    if i > 2 and (string[i - 3] + string[i - 2] + string[i - 1]) in cro:
        answer -= 2
    elif (string[i - 2] + string[i - 1]) in cro:
        answer -= 1
print(answer)

# My Solution 1 : Fail
# 크로아티아 알파벳 표에 해당하는 경우만 변경하여 카운트
# tocroa = {'c=': 'č',
# 'c-': 'ć',
# 'dz=': 'dž',
# 'd-': 'đ',
# 'lj': 'lj',
# 'nj': 'nj',
# 's=': 'š',
# 'z=': 'ž'}

# string = input()
# cnt = 0
# tmp = ""
# i = 2
# while i < len(string) + 1:
#     chk = string[i-2:i]
#     croa = tocroa.get(chk)
#     # 연속된 두 문자가 크로아티아 알파벳이면
#     if croa is not None:
#         cnt += 1
#         i += 2
#         print(i, chk, croa, cnt)

#     # 아니라면 연속된 세 문자가 크로아티아 알파벳인지 확인 ('dz=')
#     elif i + 1 < len(string):
#         croa = tocroa.get(string[i-2:i+1])
#         # 'dz='에 해당하면
#         if croa is not None:
#             cnt += 1
#             i += 3
#             print(i, string[i-2:i+1], croa, cnt)

#         # 아니라면 현재까지 문자 개수를 그대로 더함
#         else:
#             cnt += 2
#             i += 2
#             print(i, string[i-2:i+1], croa, cnt)
#     # 두 경우 모두 아니면 한 칸만 앞으로 이동, 현재 알파벳 카운트
#     else:
#         if len(string) - i >= 2:
#             cnt += 2
#             i += 2
#         elif len(string) - i == 1:
#             cnt += 1
#             i += 1
#         else:
#             cnt += 2
#             i += 1
#         print(i, chk, croa, cnt)
# print(cnt)

# Solution
# replace 메서드를 이용해 대응되는 문자열을 모두 길이 1인 임의의 문자열로 교체한 뒤
# 교체한 문자열의 길이를 출력
string = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    string = string.replace(i, '*')
print(len(string))