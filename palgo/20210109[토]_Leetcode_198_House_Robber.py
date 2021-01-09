# https://leetcode.com/problems/house-robber/


# Solution 1 : Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            print("max(_rob({}), _rob({}) + nums[{}])".format(i-1, i-2, i))
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)
'''
-------------------
_rob(3)
max(_rob(2), _rob(1) + nums[3])
-------------------
    _rob(2)
    max(_rob(1), _rob(0) + nums[2])
    -------------------
        _rob(1)
        max(_rob(0), _rob(-1) + nums[1])
        -------------------
            _rob(0)
            max(_rob(-1), _rob(-2) + nums[0])
            -------------------
                _rob(-1)
                i<0, return 0
                -------------------
                _rob(-2)
                i<0, return 0
                -------------------
            _rob(-1)
            i<0, return 0
            -------------------
        _rob(0)
        max(_rob(-1), _rob(-2) + nums[0])
        -------------------
            _rob(-1)
            i<0, return 0
            -------------------
            _rob(-2)
            i<0, return 0
            -------------------
    _rob(1)
    max(_rob(0), _rob(-1) + nums[1])
    -------------------
        _rob(0)
        max(_rob(-1), _rob(-2) + nums[0])
        -------------------
            _rob(-1)
            i<0, return 0
            -------------------
            _rob(-2)
            i<0, return 0
            -------------------
        _rob(-1)
        i<0, return 0
        '''

# Solution 2 : Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0],  nums[1]) 
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp.popitem()[1]


