"""You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums."""

from collections import Counter
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums = Counter(nums)
        sums = 0
        for key in nums:
            if nums[key] == 1:
                sums += key
        return sums
    
print(Solution().sumOfUnique(nums = [1,2,3,2]))
print(Solution().sumOfUnique(nums = [1,1,1,1,1]))