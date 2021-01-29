# 15:44-16:08
# 입력
n = map(int, input())
data = list(map(int, input().split()))

# 작은 것부터 가능한 모든 경우를 탐색한 다음
# 이전의 총합과 1 초과된 순간 멈추고 값을 리턴

data.sort()

pre = 0
for i in data:
    if (i - pre) > 1:
        break
    else:
        pre += i

print(pre+1)

