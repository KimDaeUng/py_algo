# 18:40-19:14
# My Solution(failed)
n = int(input())
data = list(map(int, input().split()))

# 여기서 실수, dp[1]의 값을
# 첫번째 원소를 선택했을 때 vs 두 번째 원소를 선택했을 때
# 중 큰 값으로 확실히 지정했어야함
dp = data[:]


for i in range(2, n):
    # 여기서 실수, dp[i]를 더할 것이 아니라 원래 배열에서 값을 가져왔어야함
    dp[i] = max(dp[i-1], dp[i] + dp[i-2])
print(dp)
# 여기서 실수, 최댓값 X, 가장 마지막 값
print(max(dp))

# Solution
# 정수 N 입력
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP Table 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(Bottom-Up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산결과 출력
print(d[n - 1])