## 입력
# 10:50-11:20 (30분)
n, m = map(int, input().split())
data = list(map(int, input().split()))

# results = []
answer = 0
# 모든 가능한 경우를 순회
for i in range(0, n-1):
    for j in range(i+1, n):
        # 무게가 같은 경우 스킵
        if data[i] == data[j]:
            continue
        # 무게가 다른 경우
        else:
            # 목록에 있지 않은 경우에 results에 append
            # if (i, j) not in results:
                # results.append((i,j))
            answer += 1
# print(len(results))
print(answer)

