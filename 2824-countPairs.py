"""Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) 
where 0 <= i < j < n and nums[i] + nums[j] < target."""

from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans


print(Solution().countPairs(nums = [-1,1,2,3,1], target = 2))
print(Solution().countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))   