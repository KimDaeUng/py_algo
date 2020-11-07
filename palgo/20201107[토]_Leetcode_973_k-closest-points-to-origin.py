# https://leetcode.com/problems/k-closest-points-to-origin/submissions/
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda k: k[0]**2+k[1]**2)[:K]