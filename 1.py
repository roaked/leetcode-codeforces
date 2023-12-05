# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#num_idx   Ex1  t = 9
# 0 -> 2
# 1 -> 7
# 2 -> 11
# 3 -> 15

class Solution:
    def twoSum(self, nums, target):
        num_idx = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_idx:
                return [num_idx[diff], idx]
            else:
                num_idx[num] = idx

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target)) 

nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target)) 


