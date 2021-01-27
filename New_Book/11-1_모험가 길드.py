# 입력
# n = map(int, input())
# data = list(map(int, input().split()))
import numpy as np

N = 300
data = list(np.random.randint(1, N, size=(1, N))[0])

# 가장 공포도가 큰 사람부터 꺼낼 수 있도록 정렬
data.sort()
print(data)

count = 0
while data:
    # 매 회차마다 하나의 그룹을 생성,
    # 1. 가장 공포도가 큰 사람을 먼저 뽑고
    try: 
        person = data.pop()
    # 2. 나머지 인원 만큼을 더 뽑음, 공포도가 큰 사람끼리
    #    먼저 묶음
        for i in range(person-1):
            data.pop()
    except:
        break
    # 3. 그룹수 추가
    count +=1

print(count)