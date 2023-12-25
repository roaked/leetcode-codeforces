"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(set(nums)) == len(nums))


print(Solution().containsDuplicate(nums = [1,2,3,1]))
print(Solution().containsDuplicate(nums = [1,2,3,4]))
print(Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
