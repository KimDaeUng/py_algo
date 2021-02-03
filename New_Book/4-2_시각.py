n = int(input())

# 전체 개수가 24 * 60 * 60 = 86,400
# 10만개 이하이므로 완탐으로도 가능한 시간
# 3중 for문으로 계산

hours = list(map(str, range(0, n+1)))
m_s = list(map(str, range(0, 60)))
count = 0
for h in hours:
    for m in m_s:
        for s in m_s:
            if "3" in h+m+s:
                count +=1

print(count)

# Solution
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)