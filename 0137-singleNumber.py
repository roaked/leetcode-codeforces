"""Given an integer array nums where every element appears three times except for one, which appears exactly once.
 Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) <= 0:
            return None

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]          
        return nums[-1]
    
    def singleNumberXOR(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            twos |= ones & num

            ones ^= num
            threes = ones & twos

            ones &= ~threes
            twos &= ~threes

        return ones 
    
print(Solution().singleNumberXOR(nums = [2,2,3,2]))
print('\n')
print(Solution().singleNumberXOR(nums = [0,1,0,1,0,1,99]))