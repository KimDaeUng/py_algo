# https://programmers.co.kr/learn/courses/30/lessons/12953

# 17:00-

def solution(arr):
    N = max(arr)
    prime_cnt = [True] * (N + 1)
    prime_cnt[0] = False
    prime_cnt[1] = False
    
    for i in range(2, N + 1):
        m = 2
        while i * m < N:
            prime_cnt[i * m] = False
            m += 1
    
    primes = [i for i in range(2, N + 1) if prime_cnt[i]]
    
    i = 0
    cur_arr = arr[:]
    
    answer = 1
    while True:            
        cnt_divided = 0
        next_arr = []
        for a in cur_arr:
            q, r = divmod(a, primes[i])
            if q != 0 and r == 0:
                next_arr.append(q)
                cnt_divided += 1

            else:
                next_arr.append(a)
            if r == 0:
                cnt_divided += 1
                
        # 나눠진 것이 없다면
        # 다음 소인수로 다시 나눠본다
        if cnt_divided < 2:
            i += 1
        # 나눠진 것이 하나라도 있으면
        # 다음 반복으로 넘어감
        elif cnt_divided >= 2:
            cur_arr = next_arr
            answer *= primes[i]
            i = 0
        
        # 소인수 인덱스를 넘어가도록 나누지 못하거나
        # 더이상 나눠지지 않을 때 멈춤
        if i > len(primes) - 1 or cur_arr.count(1) == len(arr):
            break

    return answer

arr = [2,6,8,14]
print(solution(arr))

# Solution
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def nlcm(num):
    # num.sort()
    # max_num = num[-1]
    # print (num, max_num)
    temp = 1
    for i in range(len(num)):
        # lcm = (a*b) / gcd
        # gcd = (a*b) / lcm
        temp = (num[i] * temp) / (gcd(num[i], temp))
        # print (temp)
    return temp