# 18:07-18:33
# heap.heapify()를 처음에 사용하지 않아 계속 에러
import heapq
def solution(scoville, K):
    
    def check(sco):
        for i in sco:
            if i < K:
                return False
        return True
    
    answer = 0
    
    if check(scoville):
        return answer
    
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        new_sco = a + (b * 2)
        heapq.heappush(scoville, new_sco)
        answer += 1
        
        if check(scoville):
            return answer
        
    return -1

# Solution
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
