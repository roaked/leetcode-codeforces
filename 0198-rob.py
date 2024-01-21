"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it 
 will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. """


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])
        return dp[-1] if dp[-1] > dp[-2] else dp[-2]

print(Solution().rob(nums = [1,2,3,1]))
print(Solution().rob(nums = [2,7,9,3,1]))