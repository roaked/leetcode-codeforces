"""Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer."""

from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0 and nums[i] % 2 == 0:
                ans += nums[i] 
                cnt += 1
        return ans // cnt if cnt > 0 else 0


print(Solution().averageValue(nums = [9,3,8,4,2,5,3,8,6,1]))