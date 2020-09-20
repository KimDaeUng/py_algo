# 8강 연결 리스트 ADT

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        # 먼저 pos가 올바른 값의 범위에 있는지 체크
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        # (1) 삽입 위치가 리스트 맨 앞
        # : preve가 없고, head가 새로운 노드를 가리키도록 함
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        
        # (2) 리스트의 처음이 아니라면
        else:
            # (3) 삽입 위치가 리스트 맨 끝이면
            # : 처음부터 탐색할 필요없이 바로 tail로 찾음
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode
        
        # (3) 삽입 위치가 리스트 맨 끝
        # : tail이 새로운 노드를 가리키도록 조정
        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
