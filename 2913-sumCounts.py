"""You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. 
Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        def count(l):
            s = set(l)
            return len(s)**2
    
        for i in range(n):
            for j in range(i+1, n+1):
                ans += count(nums[i:j])
        
        return ans

print(Solution().sumCounts(nums = [1,2,1]))

print(Solution().sumCounts(nums = [1,1]))