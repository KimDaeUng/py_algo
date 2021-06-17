# https://leetcode.com/problems/maximum-subarray/
'''
DP 문제
입력받은 배열을 그대로 복사하여 DP 테이블 만든 후,
dp[i] : i번째까지의 연속된 합의 최대값
매번 현재까지의 연속된 합의 최대값과, 현재값과 비교하여 현재값이 더 크다면
그 지점부터 현재값으로 새로 갱신함
dp[i] = max(dp[i-1] + nums[i], nums[i])
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = nums[:]
        for i in range(1, len(nums)):
            cache[i] = max(cache[i-1] + nums[i], nums[i])
        return max(cache)
        