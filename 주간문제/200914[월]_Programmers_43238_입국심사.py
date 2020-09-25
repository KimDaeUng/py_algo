# https://programmers.co.kr/learn/courses/30/lessons/43238
# 이분탐색
# 이분탐색 할 값 : 한 명의 심사관에게 얼마나 시간을 줄 것인지
# 이분탐색 기준 : 주어진 시간동안 각 심사관이 심사를 했을 때, 심사를 마친 사람의 수가 n명 이상인지 미만인지?

# https://life-with-coding.tistory.com/346 
# https://post.naver.com/viewer/postView.nhn?volumeNo=27248090&memberNo=33264526
# https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%85%EA%B5%AD-%EC%8B%AC%EC%82%AC-Level-3

def solution(n, times):
    ## 최악의 경우 : 가장 비효율 심사관에게 다 받는 경우의 시간
    L, R = 1, max(times) * n 
    answer = 0
    print(L, R)

    while L <= R:
        # 한 심사관에게 주어진 시간
        mid = (L + R)//2
        people = 0
        # print("-"*50)
        # print(mid, L, R, people)
        # print()
        for i in times:
            # 각 심사관마다, 주어진 시간 동안 몇 명의 사람을 심사할 수 있나?
            people += mid // i 
            # print(i, people)

            # 모든 사람을 심사할 수 있으면
            # 한 심사관에게 주어진 시간을 줄이고 
            # 반복문을 벗어난다.
            if people >= n:
                answer = mid
                R = mid - 1
                # print("Lower the time ", answer, R)
                break
        # 모든 사람을 심사할 수 없는 경우
        # 한 심사관에게 주어진 시간을 늘려본다.
        if people < n:
            # print("More time ", )
            L = mid + 1
    return answer

n = 6
times = [7, 10]

print(solution(n, times))