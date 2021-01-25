# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))


# # 숫자가 어떻게 되든 가장 큰 수와 그 다음으로 큰 수로 번갈아가며 진행
# data.sort()

# first, second = data[n-1], data[n-2]

# answer = []
# count = 1
# offset = k + 1
# while len(answer) != m:
#     if count % offset == 0:
#         answer.append(second)
#     else:
#         answer.append(first)
    
#     count += 1
# print(answer)
# print(sum(answer))

#################################
# 단순한 풀이

# 여기는 동일
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first, second = data[n-1], data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

###################################
# 효율적인 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first, second = data[n-1], data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k 
count += m % (k+1)

result = 0
result += count * first      # 첫 번째로 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)
