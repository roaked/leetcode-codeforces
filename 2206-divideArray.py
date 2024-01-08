"""You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false."""

from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        pairs = len(nums) // 2
        for _ in range(0, 2*pairs, 2):
            if nums[_] != nums[_+1]:    
                return False
        return True
    
print(Solution().divideArray(nums = [3,2,3,2,2,2]))