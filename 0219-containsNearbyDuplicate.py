"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}

        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i

        return False



print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))