"""You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array."""

from typing import List
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        ans = Counter(nums)
        max_freq_elements = [key for key, value in ans.items() if value == max(ans.values())]  
        return len(max_freq_elements) * max(ans.values())

print(Solution().maxFrequencyElements(nums = [1,2,2,3,1,4]))