"""You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums."""

from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = Counter(nums)
        filtered_dict = {key: value for key, value in dic.items() if value == 1}
        return sum(filtered_dict)
    
print(Solution().sumOfUnique(nums = [1,2,3,2]))
print(Solution().sumOfUnique(nums = [1,1,1,1,1]))