"""There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible."""

class Solution:
    def search(self, nums: list[int], target: int) -> bool: #increasing

        if len(nums) == 1:
            return nums[0] == target
        
        l, r = 0, len(nums)-1

        while (l <= r):
            while(l < r) and nums[l] == nums[r]:
                l += 1

            mid = (l + r) //2

            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1 
            
            elif nums[l] <= nums[mid]:  # left side is sorted
                if nums[l] <= target < nums[mid]:  # if target is in the left side
                    r = mid - 1
                else:
                    l = mid + 1

            else:  
                if nums[mid] < target <= nums[r]:  # if target is in the right side
                    l = mid + 1
                else:
                    r = mid - 1

        return False
    
print(Solution().search(nums = [2,5,6,0,0,1,2], target = 0))
print('\n')
print(Solution().search(nums = [2,5,6,0,0,1,2], target = 3))
print('\n')
print(Solution().search(nums = [1,0,1,1,1], target = 0))

