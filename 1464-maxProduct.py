""""
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

# Beats 91.86% on Runtime / 71.50% on Memory

class Solution(object):
    def maxProduct(self, nums: list):
        size = len(nums)
        nums.sort()
        solution = (nums[size-1]-1) * (nums[size-2]-1)
        return solution

nums = [3,4,5,2]
print(Solution().maxProduct(nums))

nums = [1,5,4,5]
print(Solution().maxProduct(nums))

nums = [3,7]
print(Solution().maxProduct(nums))
