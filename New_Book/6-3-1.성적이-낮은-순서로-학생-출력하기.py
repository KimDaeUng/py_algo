# 21:21-21:23
N = int(input())
data = []
for _ in range(N):
    data.append(input().split())

data.sort(key=lambda x : (int(x[-1])))

for i in range(N):
    print(data[i][0], end=' ')