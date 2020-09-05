class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # Front pointer
        self.p2 = 0 # Rear pointer
    
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return self.q[self.p1] if self.q[self.p1] is not None else -1
    
    def Rear(self) -> int:
        return self.q[self.p2-1] if self.q[self.p2-1] is not None else -1
    
    def isEmpty(self) -> bool:
        if self.p1 == self.p2 & self.q[self.p1] is None:
            return True
        else:
            False

    def isFull(self) -> bool:
        if self.p1 == self.p2 & self.q[self.p1] is not None:
            return True
        else:
            return False

            
            





















class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
    
        return answer

