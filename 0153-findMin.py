"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
 For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time."""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:  # min right side
               l = mid + 1
            else:
                r = mid
            
        return nums[l]
    
print(Solution().findMin(nums = [3,4,5,1,2]))
print('\n')
print(Solution().findMin(nums = [4,5,6,7,0,1,2]))
print('\n')
print(Solution().findMin(nums = [11,13,15,17]))