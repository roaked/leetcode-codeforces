"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
 Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if 
 two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police."""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def find(nums):
                dp = [0] * len(nums)
                dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]
                for i in range(3, len(nums)):
                    dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
                return max(dp[-1], dp[-2])
        
        return max(find(nums[1:]), find(nums[:-1]))

print(Solution().rob(nums = [2,3,2]))
print(Solution().rob(nums = [1,2,3,1]))
print(Solution().rob(nums = [1,2,1,1]))