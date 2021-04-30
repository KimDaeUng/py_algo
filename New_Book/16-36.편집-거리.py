# # 13:15-16:17
# https://leetcode.com/problems/edit-distance/
# My Solution 2 (Leetcode)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_a = len(word1)
        len_b = len(word2)
        
        table = [[0] * (len_b + 1) for _ in range(len_a + 1)]
        
        for i in range(len_a + 1):
            table[i][0] = i
        for j in range(len_b + 1):
            table[0][j] = j
        
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(table[i][j-1], table[i-1][j-1], table[i-1][j]) + 1
        
        return table[len_a][len_b]

# My Solution 1 (해설 참고)
a = input()
b = input()

len_a = len(a)
len_b = len(b)

dp = [ [0] * (len_b + 1) for _ in range(len_a + 1) ] 

# 초기값
# 1. 공백 문자 -> b
for i in range(len_a):
    dp[i][0] = i
# 2. 공백 문자 -> a
for j in range(len_b):
    dp[0][j] = j

# 나머지 값
for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        # 두 문자가 같다면 dp table에서 왼쪽 위의 값을 가져옴
        # ex) A : 'su'  / B : 'satu' -> edit dist : 2
        # ->  A : 's' / B ; 'sat' -> edit dist : 2
        # -> 두 문자가 같을 땐 편집 X
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i-1][j-1]
        
        # 두 문자가 다를 떈 아래 경우 중 최솟값 + 1
        # 1. 삽입(왼쪽)
        # 2. 교체(왼쪽 위)
        # 3. 삭제(위쪽)
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
        
print(dp[len_a][len_b])


# Solution
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # DP를 위한 2차원 DP Table 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP Table 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용 찾아 대입
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    
    return dp[n][m]

# 두 문자열 입력 받기
str1 = input()
str2 = input()

# 최소 편집 거리 출력
print(edit_dist(str1, str2))