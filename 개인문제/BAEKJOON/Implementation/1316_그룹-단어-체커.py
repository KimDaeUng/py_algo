# https://www.acmicpc.net/problem/1316
# 18:42-18:49

string = '''3
happy
new
year'''

def testcase(string):
    string = string.split("\n")
    for i in string:
        yield i

G = testcase(string)

def input():
    return next(G)

n = int(input())

def check(string):
    seen = set()
    for i in range(len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        # 같은 문자열의 연속이 아니면서
        # 이미 본 문자열인 경우
        elif i > 0 and \
            string[i - 1] != string[i]:
            return False
    return True

cnt = 0
for _ in range(n):
    string = input()
    if check(string):
        cnt += 1
print(cnt)

# Solution
# ref: https://duwjdtn11.tistory.com/584
# for ~ else문을 사용하면
# for문이 마지막 원소까지 모두 실행되었을 때
# else 문이 실행됨

n = int(input())
cnt = 0

for _ in range(n):
    checker = []
    word = input()
    for char in word:
        if char in checker:
            if checker[-1] != char:
                break
        else:
            checker.append(char)
    else:
        cnt += 1

print(cnt)