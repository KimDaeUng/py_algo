# https://programmers.co.kr/learn/courses/30/lessons/12904

# 투 포인터를 이용
def solution(s):
    # 길이가 1 또는 전체가 펠린드롬인 경우
    if len(s) < 2 or s == s[::-1]:
        return len(s)

    answer = 0
    def expand(L, R):
        while L >= 0 and R <= len(s) and s[L] == s[R-1]:
            L -= 1
            R += 1
        return len(s[L+1:R-1])
    
    for i in range(0, len(s) - 1):
        answer = max(answer,
                    expand(i, i+1),
                    expand(i, i+2)
                    )

    return answer