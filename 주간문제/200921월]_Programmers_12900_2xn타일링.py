# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0
    visit = [[False] * n for _ in range(2)]
    
    dx = [(0, 0), (0, 1)]
    dy = [(0, 1), (0, 0)] 
    
    def dfs():
        global answer
        i, j = -1, -1
        isFinish = True
        
        for x in range(2):
            for y in range(n):
                if not visit[x][y]:
                    isFinish = False
                    i, j = x, y
            if not isFinish:
                break
        if isFinish:
            answer += 1
            return
        
        if not visit[i][j]:
            for rotate in range(2):
                isPossible = True
                possibleDirection = []
                
                for way in range(2):
                    ii = i + dx[rotate][way]
                    jj = j + dy[rotate][way]
                    
                    if ii > 1 or  jj > n - 1:
                        isPossible = False
                        break
                    
                    if visit[ii][jj]:
                        isPossible = False
                        break
                    
                    possibleDirection.append((ii, jj))
                    
                if isPossible:
                    for pDX, pDY in possibleDirection:
                        visit[pDX][pDY] = True
                    
                    dfs()
                    
                    for pDX, pDY in possibleDirection:
                        visit[pDX][pDY] = False
    
    print('start')
    dfs()
                
    
    return answer

##########

# Solution : 효율성 테스트 통과 x
# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2-x-n-%ED%83%80%EC%9D%BC%EB%A7%81-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# list로 저장하지 말고, 변수 3개로만 해야 통과함
def solution(n):
    
    m = [ 0 for _ in range(n+1) ]
    
    if n <= 3:
        answer = n
    else:
        m[1] = 1
        m[2] = 2
        
        for i in range(3, n+1):
            m[i] = m[i-1] + m[i-2]
        
        answer = m[i] % 1000000007
    return answer