# 16:17-18:56
# https://programmers.co.kr/learn/courses/30/lessons/42883
# My Solution(Retry)
'''
- Stack 사용이 어색함, 집중 연습 필요
- 결과로 출력할 수를 쌓는 stack을 만들고,
  다음에 입력되는 수와 stack에 입력된 수를 비교해
  stack에 입력된 수가 현재 수보다 커질 때까지 끝 수를 삭제,
  삭제 횟수는 k번으로 제한됨
- k번을 모두 사용하면 그 이후부터는 append만함
- 특수한 케이스 : 길이가 k이상의 내림차순 숫자 -> 5432, k = 2 인경우,
  그대로 계속 append 후 끝 수 2개만 제거 
'''
def solution(number, k):
    st = []
    for n in number:
        while st and st[-1] < n and k > 0:
            st.pop()
            k -= 1
        st.append(n)
        if k < 0:
            break
    if k > 0:
        st = st[:-k]
    return ''.join(st)


# Solution 1
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)

# Solution 2 (위와 표현만 다른 동일한 방식)
def solution(number, k):
    st = []
    n = len(number)
    for i in range(n):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:n-k])

# Solution 3 : 상세 설명
'''
https://velog.io/@dailyhyun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0
1. stack 생성
2. number 문자열 끝까지 순회
3. stack의 마지막 값이 넣으려고 하는 값보다 작으면 큰 값이 나올 때까지 stack의 값을 pop해준 뒤 넣으려는 값을 stack에 넣는다.
  3-1. stack의 마지막 값이 넣으려고 하는 값보다 크다면 그냥 넣기
4. 삭제할 수 있는 값이 아직 있으면 stack에서 pop하고 삭제할 수 있는 값 하나 감소
5. 삭제할 수 있는 값이 더 이상 없으면 while 문 종료
6. number 문자열 끝까지 다 순회했는데 아직 삭제해야 할 갯수가 더 남아있으면
   삭제해야 할 갯수만큼 stack의 마지막 부분에서 pop
7. stack의 요소들 문자열로 합쳐서 반환
'''
def solution(number, k):
    # 1.
    stack = []
    # 2.
    for i in number:
        # 3.
        while stack and i > stack[-1]:
            # 4.
            if k > 0:
                stack.pop()
                k -= 1
            # 5.
            else:
                break
        # 3-1.
        stack.append(i)
    # 6
    if k > 0:
        for i in range(k):
            stack.pop()
    return ''.join(stack)

# import logging

# def __get_logger():
#     __logger = logging.getLogger('logger')
#     # 로그 포맷 정의
#     formatter = logging.Formatter(
#             'LOG##LOGSAMPLE##%(levelname)s##%(asctime)s##line::%(lineno)s>> %(message)s')
#     # 스트림 핸들러 정의
#     stream_handler = logging.StreamHandler()
#     # 각 핸들러 포맷 지정
#     stream_handler.setFormatter(formatter)
#     # 로거 인스턴스에 핸들러 삽입
#     __logger.addHandler(stream_handler)
#     # 로그 레벨 정의
#     __logger.setLevel(logging.DEBUG)

#     return __logger

# # 로거 정의
# logger = __get_logger()

# def solution(number, k):
#     # 1.
#     stack = []
#     logger.info(f'stack : {stack}')

#     # 2.
#     for i in number:
#         logger.info(f'i : {i} ----------------')

#         # 3
#         while stack and i > stack[-1]:
#             logger.info(f'  stack and i : {i} > stack[-1] : {stack[-1]}')

#             # 4.
#             if k > 0:
#                 logger.info(f'      k : {k} > 0 -> stack.pop() -> k : {k-1}')
#                 stack.pop()
#                 k -= 1
#             # 5.
#             else:
#                 logger.info(f'      k : {k} <= 0 -> stack.pop() -> break')
#                 break
#         # 3-1
#         stack.append(i)
#         logger.info(f'stack.append({i}) stack : {stack}')

#     # 6.
#     if k > 0:
#         logger.info(f'k : {k} > 0 -> for i in range(k):stack.pop() -> stack : {stack}')
#         for i in range(k):
#             stack.pop()
#     # 7.
#     answer = ''.join(stack)
#     return answer

print(solution('1924', 2))
# print(solution('1231234', 2))
# print(solution('5432', 2)) # stack에서 숫자를 빼는 경우 없이 계속 쌓이는 경우
# print(solution('4177252841', 2))
# print(solution('1234444', 2))
