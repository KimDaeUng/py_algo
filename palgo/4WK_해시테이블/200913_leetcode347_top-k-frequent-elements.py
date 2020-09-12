# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List

# My Solution
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for n in nums:
            freq_dict[n]+=1
        sorted_items =  sorted(freq_dict.items(), key=(lambda x : x[1]))[-k:]
        return [i[0] for i in sorted_items]


# Other Solution : Pop by descending order using Counter & Priority Queue
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk


# Other Solution 2 : Pythonic Way
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]