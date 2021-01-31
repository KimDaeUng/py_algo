# 20:30-21:20 
# My Solution -> 26, 5 케이스에서 잘못된 답
n, k = map(int, input().split())

def solution(n, k):
    count = 0
    while n > 1:
        div, remain = divmod(n, k)
        # 나누어 떨어질 경우
        if (remain == 0)&(div >= 1):
            # 나누기 연산 카운트
            count += 1
        # 나누어 떨어지지 않는 경우
        else:
            # 몫이 1인 경우
            if div == 1:
                # 나누기 연산 카운트
                count += 1
                # 나머지는 모두 빼기 연산
                # 이 부분 때문에 몫이 0인 경우가 발생하지 않음
                count += remain
                return count
            # 몫이 1초과인 경우 다음 턴으로 넘기면서 나머지 모두 추가
            elif div > 1:
                count += remain
        n = div
    return count
    
print(solution(n, k))

# Solution : 단순한 풀이,
# N의 범위가 10만 이하인 경우 가능, 그 이상은 시간초과
n, k = map(int, input().split())

def solution(n, k):
    while n > 1:
        # 나누어 떨어질 경우 나눔
        if n % k == 0:
            n //= k
        # 나누어 떨어지지 않는 경우, 1을 뺌
        else:
            n -= 1
        cnt += 1
    return cnt
            
# Solution 2 : 효율적인 풀이
# 문제 해결을 위한 아이디어 : 최대한 많이 나누기
# 따라서 다음의 과정을 반복할 수 없을 때까지 반복하면 정답 구할 수 있다.
# 1. N이 K의 배수가 될 때까지 1씩 빼기
# 2. N을 K로 나누기

# 이 때 N이 K의 배수가 되도록 효율적으로 짜기 위해 1을 일일이 빼지 않고 한 번에 뺀다.
n, k = map(int, input().split())

def solution(n, k):
    count = 0

    while True:
        # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기(한꺼번에)
        target = (n // k) * k  # k의 배수 표현
        count += (n - target) # result : 나머지를 1씩 뺴는 연산


        # K의 배수로 업데이트함
        n = target

        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break

        # K의 배수를 k로 나누면 딱 나누어 떨어짐
        count += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 뺴기
    # ex. [27, 5], 
    count += (n-1)
    # n-1인 이유 : n = 1이 될 때,
    # 라인 60에서 count에 1이 더해지고, 라인 64에서 n이 0이 됨  
    # 잘못 더해진 만큼 뺴기
    return count

print(solution(n, k))