"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""


from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = []
        for n in range(len(nums)+1):
            ans.append(n)
        
        for num in ans:
            if num not in nums:
                return num