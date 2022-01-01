# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    cnt = Counter(nums)
    cnt, _ = zip(*sorted(cnt.items(), key=lambda x : -x[1]))
    return cnt[:k]