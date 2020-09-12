# https://leetcode.com/problems/jewels-and-stones/submissions/

# My Solution : Using defaultdict
from collections import defaultdict
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count_dic = defaultdict(int)
        for s in S:
            if s in J:
                count_dic[s] += 1
        return sum(count_dic.values())


# Other Solution : Using Counter Module
from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = Counter(S)
        count = 0
        for char in J:
            count += freqs[char]
        return count

# Other Solution : Pythonic Way
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)