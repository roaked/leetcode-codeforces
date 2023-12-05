# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
#i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

print(Solution().threeSum(self,nums))

Input: nums = [0,1,1]
Output: []

print(Solution().threeSum(self,nums))

Input: nums = [0,0,0]
Output: [[0,0,0]]

print(Solution().threeSum(self,nums))