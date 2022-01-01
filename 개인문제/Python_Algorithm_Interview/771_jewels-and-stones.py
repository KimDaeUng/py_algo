# https://leetcode.com/problems/jewels-and-stones/submissions/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for jewel in jewels:
            answer += stones.count(jewel)
        return answer
            