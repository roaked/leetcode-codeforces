"""An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise."""

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        if nums[-1] > nums[0]: #increasing
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
        return True
    
print(Solution().isMonotonic(nums = [1,2,2,3]))
print(Solution().isMonotonic(nums = [6,5,4,4]))
print(Solution().isMonotonic(nums = [1,3,2]))