# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = nums[:]
        for i in range(1, len(nums)):
            cache[i] = max(cache[i-1] + nums[i], nums[i])
        return max(cache)
        