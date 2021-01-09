# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = nums[:]
        for i in range(1, len(nums)):
            cache[i] = max(cache[i-1] + nums[i], nums[i])
            
        return max(cache)

# Solution 1 : Memoization
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            print(sums)
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        print(sums)
        return max(sums)

'''
앞에서부터 누적합을 계산해 sums에 저장, 이전 값을 계속 더해나가되
0 이하가 되면 버리고 현재 수부터 새로 시작

input : 
[-2,1,-3,4,-1,2,1,-5,4]

output :
index : 1 | sums : [-2]
index : 2 | sums : [-2, 1]
index : 3 | sums : [-2, 1, -2]
index : 4 | sums : [-2, 1, -2, 4]
index : 5 | sums : [-2, 1, -2, 4, 3]
index : 6 | sums : [-2, 1, -2, 4, 3, 5]
index : 7 | sums : [-2, 1, -2, 4, 3, 5, 6]
index : 8 | sums : [-2, 1, -2, 4, 3, 5, 6, 1]
Last | sums : [-2, 1, -2, 4, 3, 5, 6, 1, 5]
'''

# Solution 2 : Kadane Algorithm
'''
최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2)
-> 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제 O(n)
매 단계마다 best_sum 계산(속도 동일)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum