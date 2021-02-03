# 22:54-23:02

# My Solution
data = input()
import re
front = "".join(sorted(re.findall(r'[a-zA-Z]', data)))
back = str(sum(map(int, (re.findall(r'[0-9]', data)))))
print(front + back)

# Solution

data = input()
result = []
value = 0

# 문자를 하나씩 확인해
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    
    # 숫자는 따로 더함
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))