"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        size = len(nums)

        if target not in nums:
            return -1
        if target in nums and size == 1:
            return 0
        
        left, right = 0, size - 1
        
        while left <= right:
            mid = (left + right) // 2 # 1+3 -> 4 // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # left side is sorted
                if nums[left] <= target < nums[mid]:  # if target is in the left side
                    right = mid - 1
                else:
                    left = mid + 1

            else:  # right side is sorted
                if nums[mid] < target <= nums[right]:  # if target is in the right side
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1 #no case
    
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0)) #4
print('\n')
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3)) #-1
print('\n')
print(Solution().search(nums = [1], target = 0)) #-1 
print('\n')
print(Solution().search(nums = [1,3], target = 1)) 
print('\n')
print(Solution().search(nums = [1,3], target = 3)) 
