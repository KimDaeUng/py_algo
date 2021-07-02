# https://programmers.co.kr/learn/courses/30/lessons/12899


# My Solution: Retry
'''
규칙찾기
3으로 나눈 몫과 나머지를 쭉 나열한 뒤  규칙 찾기
나머지에 따라 어떤 숫자를 쓸지 정함
나머지 1, 2 -> 1, 2
나머지 0 -> 4

3으로 나눠 떨어져서 나머지가 0인 경우
다음번 반복에서 몫을 3으로 나눈 나머지가 자리수가 되는데 숫자가 1씩 뒤로 밀려있음
# ex) n = 3
    n % 3 = 0, -> 자리수 4 붙임
    -> 다음번 반복에서 몫 1을 3으로 나눈 나머지 1이 붙어 14가 됨
    -> 따라서 다음번 반복으로 가기 전에 몫에서 1을 빼줘야함
'''
def solution(n):

    trans = "412"
    answer = ''
    
    q = None
    while q != 0:
        q, r = divmod(n, 3)
        answer += trans[r]
        if r == 0:
            q -= 1
        n = q
    return answer[::-1]

# My Solution:Fail
# 3진법으로 계산 후 3진법으로 올라간 자리만 다르게 처리하려 했으나 실패
def solution(n):
    def get_n(n):
        n_rev = []
        while True:
            n, r = divmod(n, 3)
            n_rev.append(r)
            if len(n_rev) > 0 and n > 0 and r == 0:
                n_rev[-1] = 4
                if n == 1:
                    break
            if n == 0:
                break
        return ''.join(map(str, n_rev[::-1]))
    return get_n(n)

# Solution:
'''
ref: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=h0609zxc&logNo=221480111945


나머지가 0일 때 몫을 1 빼줘야 

'''
def solution(n):
    answer = ''

    n_dict = {1:'1', 2:'2', 0:'4'}
    q, r = None, None
    
    while q != 0:
        q, r = divmod(n, 3)
        if r == 0:
            q -= 1
        n = q

        answer = n_dict[r] + answer
    return answer

# Solution2
# https://eda-ai-lab.tistory.com/452
def solution(n):
    if n <= 3:
        return '124'[n - 1]
    
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]