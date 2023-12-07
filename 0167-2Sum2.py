# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
# they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

#Dictionary
class Solution(object):
    def twoSum(self, nums, target):
        num_idx = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_idx:
                #print('\nInput: {0}\nTarget: {1}\nIndex 1: {2}\nIndex 2: {3}'.format(nums, target, num_idx[diff]+1, idx+1))
                return [num_idx[diff]+1, idx+1]
            else:
                num_idx[num] = idx

nums = [2,7,11,15]
target = 9
Solution().twoSum(nums, target)

nums = [2,3,4]
target = 6
Solution().twoSum(nums, target)

nums = [-1,0]
target = -1
Solution().twoSum(nums, target)