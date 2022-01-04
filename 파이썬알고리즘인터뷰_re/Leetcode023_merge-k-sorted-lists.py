# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional, 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        
        heap = []
        
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # 힙 추출 이후 다음 노드는 다시 저장
        
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        
        return root.next


class Solution(object):
    def mergeKLists(self, lists):
        nodes = []
        head = cur_node = ListNode(None)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        sorted_nodes = sorted(nodes)
        for x in sorted_nodes:
            cur_node.next = ListNode(x)
            cur_node = cur_node.next
        return head.next