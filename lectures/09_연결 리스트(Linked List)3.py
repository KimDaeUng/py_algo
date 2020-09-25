class Node:
    
	def __init__(self, item):
		self.data = item
		self.next = None


class LinkedList:

	def __init__(self):
		self.nodeCount = 0
        # Head Node에 Dummy Node
		self.head = Node(None)
		self.tail = None
        # 빈 연결리스트의 기본값으로 head.next는 tail을 가리킴
		self.head.next = self.tail


	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s


	def getLength(self):
		return self.nodeCount


	def traverse(self):
		result = []
		curr = self.head
        # Head에 Dummy Node 넣음으로써 달라지는 부분
		while curr.next:
			curr = curr.next
			result.append(curr.data)
        ##########################################
		return result


	def getAt(self, pos):
        # Head에 Dummy Node 넣어서 달라진 부분
        # getAt(0) -> head이므로 0번 인덱스까지 가능함
		if pos < 0 or pos > self.nodeCount:
			return None
		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1

		return curr

    # 삽입을 용이하게 하기 위해 새롭게 추가된 메서드
    # 매번 처음부터 getAt으로 직전 노드 탐색하지 않게 함

	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
        # Tail Node에 이어 붙이는 경우 : Tail 갱신
		if prev.next is None:
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True


	def insertAt(self, pos, newNode):
        # pos 범위 조건 확인
		if pos < 1 or pos > self.nodeCount + 1:
			return False
        # pos == 1 인 경우는 head 뒤에 새 node 삽입
		# Tail에 새로 붙이는 경우, prev는 tail
        if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail
        # Tail에 붙이는 걸 제외한 나머지 경우
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode)


	def concat(self, L):
        # Head에 Dummy Node 추가되어 달라짐
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount
