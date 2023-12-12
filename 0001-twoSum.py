# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: list, target: int):
        num_idx = {}
        for idx, num in enumerate(nums):  #0,2
            diff = target - num  #diff = 9 - 2 = 7
            if diff in num_idx: # if 7 in dictionary
                return [num_idx[diff], idx] # return (dictionary "7" : 0)
            else:
                num_idx[num] = idx # store { 2 : 0 }

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target)) 

nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target)) 


