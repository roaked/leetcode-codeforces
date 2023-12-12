"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
#Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        value, cnt = None, 0
        if len(nums) == 1:
            return nums[0]
        
        for idx in range(0, len(nums), 2):
            if idx == len(nums) - 1 or nums[idx] != nums[idx + 1]:
                return nums[idx]
        return -1  
        
    def singleNumberDict(self, nums: list[int]) -> int:
        return True

nums = [2,2,1]
print(Solution().singleNumber(nums))
print("\n")
nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))
print("\n")
nums = [1]
print(Solution().singleNumber(nums))
