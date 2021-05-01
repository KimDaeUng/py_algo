# https://www.acmicpc.net/problem/11722
# 19:10-19:45 
'''
dp[i] : 마지막 원소를 array[i]로 갖는 감소하는 부분 수열의 최대 길이

dp[i] = max(dp[j] + 1, dp[i]) if array[j] > array[i]

- 현재 인덱스와 그 이전 인덱스를 비교했을 때 현재 값보다 더 큰 값이 있는가?
- 만약 더 큰 값이 있다면 그 인덱스까지 최대 길이에 1을 더하면 현재 인덱스보다 커지는가?

# Reference
https://velog.io/@pyh8618/BaekJoon-11722-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
'''

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n
max_size = 1

for i in range(n):
    for j in range(i):
        # 이전 수 중에서 현재 수 array[i] 보다 큰 값을 가질 경우
        # dp[i]를 j번째까지의 최대 길이 + 1과 현재까지 구해진 i번째까지의 최대 길이 중 큰 값으로 갱신
        if array[j] > array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            max_size = max(max_size, dp[i])
print(max_size)