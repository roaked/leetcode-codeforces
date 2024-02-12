"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""

from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d, l = Counter(nums), len(nums) // 2
        return [key if value > l else None for key, value in d.items()]

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))

