"""Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. 
Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array."""

from typing import List
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        subarrays = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] == nums[k] + nums[j]:
                        subarray = nums[i:k+1]
                        subarrays.append(subarray)
        return subarrays
    
print(Solution().findSubarrays(nums = [1,2,3,1,0,2]))