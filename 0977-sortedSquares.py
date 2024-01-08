"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num ** 2 for num in nums)

print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))

    