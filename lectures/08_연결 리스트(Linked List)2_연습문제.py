# https://programmers.co.kr/learn/courses/57/lessons/13780
# 연결 리스트 노드 삭제 popAt 구현

class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


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
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # popAt의 구현
    def popAt(self, pos):
        # pos가 올바른 범위인지 확인
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        data = 0
        # 1) 유일한 원소를 삭제하는 경우
        if self.nodeCount == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.nodeCount -= 1
            return data
        # 2) Head Node를 삭제하는 경우
        if pos == 1:
            data = self.head.data
            self.head = self.head.next

        # 3) Head Node < Node <= Tail Node 범위내 Node 삭제
        else:
            # 직전 Node 추출 & pos Node 값 추출
            prev = self.getAt(pos - 1)
            curr = prev.next
            data = curr.data
            
            # 3-1)Tail Node를 삭제한 경우 : self.Tail 갱신
            if pos == self.nodeCount:
                prev.next = None
                self.tail = prev
            # 3-2)Head < Node < Tail 범위내 Node 삭제한 경우
            else:
                prev.next = curr.next
                # ?? tail 안바꿔도 되지않나?
                self.tail = self.getAt(self.nodeCount-1)
        # nodeCount 1 감소
        self.nodeCount -= 1
        return data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0