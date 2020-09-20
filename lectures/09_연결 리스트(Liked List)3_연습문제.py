# https://programmers.co.kr/learn/courses/57/lessons/13781
# (09) dummy head 를 가지는 연결 리스트 노드 삭제
# 인덱스 범위나, 작동방식을 insert의 경우와 비슷할 거라 생각한게 잘못
# 유일 노드 여부를 Tail 관점에서 생각해야함

class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        # prev 다음 노드가
        # 1. 삭제할 노드가 없는 경우
        if prev.next == None:
            return None
        
        # 2. Tail Node인 경우
        if curr.next == None:
            # 유일한 노드일 떄
            if self.nodeCount == 1:
                self.tail = None
            # 유일한 노드가 아닐 때
            else:
                self.tail = prev

        # 링크 조정
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        # pos 범위 조건 확인
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos-1)
        
        return self.popAfter(prev)

def solution(x):
    return 0