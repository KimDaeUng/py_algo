# https://leetcode.com/problems/majority-element/


# 1. Defalutdict를 이용한 풀이(DP)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import Defaultdict

        dic = Defaultdict(int)
        half_len_nums = len(nums) // 2

        for i in nums:
            dic[i] += 1
        
        for i in nums:
            if dic[i] > half_len_nums:
                return dic[i]

# 2. Pythonic Way
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

# 3. 분할 정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half_len_nums = len(nums)//2
        
        if len(nums) == 1:
            return nums[0]
        
        a = self.majorityElement(nums[:half_len_nums])
        b = self.majorityElement(nums[half_len_nums:])
        
        return [b, a][nums.count(a) > half_len_nums]