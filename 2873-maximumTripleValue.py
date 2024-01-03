"""You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k]."""

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans


        
print(Solution().maximumTripletValue(nums = [12,6,1,2,7]))
print(Solution().maximumTripletValue(nums = [2,3,1]))
print(Solution().maximumTripletValue(nums = [10,13,6,2]))