# data = input().strip()
# data = str(int(data))

# length = len(data)

# n_comma = length // 3
# # if n_comma < 1:
# #     print("READY")

# data = data[::-1]
# is_lucky = False
# for i in range(1, n_comma+1): 
#     front = data[(i)*3:]
#     back = data[:(i)*3]
#     print(back, front)
#     # print("---------------")
#     front = sum([int(j) for j in front])
#     back  = sum([int(j) for j in back])
#     print(back, front)

#     if front == back:
#         is_lucky = True
#         break

# if not is_lucky:
#     print("READY")
# else:
#     print("LUCKY")

# My Solution
data = input()

half_length = len(data) // 2


left = sum(map(int, data[:half_length]))
right = sum(map(int, data[half_length:]))

if left == right:
    print("LUCKY")
else:
    print("READY")

# Solution
n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")