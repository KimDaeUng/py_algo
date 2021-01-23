# https://programmers.co.kr/learn/courses/30/lessons/42842

# 40m

def solution(brown, yellow):
    # answer = []
    # 1. yellow 기준으로 가능한 사각형 모두 찾기
    # 2. 세로 길이 <= 가로 길이인 경우에 한하여 
    # 3. yellow의 가로 길이 * 2 + (yellow의 세로 길이 + 2) * 2 == brown 인 것을 찾고
    # 4.  [yellow의 세로 길이 + 2, yellow의 가로 길이 + 2] 를 반환

    maximum = int(yellow ** 0.5) + 1
    cases = []
    for i in range(1, maximum):
        width_yellow, remain = divmod(yellow, i)
        if remain == 0:
            height_yellow = yellow//width_yellow
            print(height_yellow, width_yellow)
            if height_yellow <= width_yellow:
                # [Yellow를 기준으로 계산한 Brown의 개수]
                expected = (2 * width_yellow) + 2 * (height_yellow + 2)
                if brown == expected:
                    return [width_yellow+2, height_yellow + 2]
    