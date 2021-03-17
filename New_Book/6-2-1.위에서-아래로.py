# 21:16-21:18
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort(reverse=True)

for i in range(N):
    print(data[i], end=' ')