# https://leetcode.com/problems/hamming-distance/submissions/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(map(lambda x : int(x), bin(x ^ y)[2:]))


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')