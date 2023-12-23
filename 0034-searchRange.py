"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]: #increasing order

        l, r = 0, len(nums) -1
        lc, rc = -1, -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
            if nums[mid] == target:
                lc = mid

        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            if nums[mid] == target:
                rc = mid
                
        return [lc, rc]
    
print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
print('\n')
print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
print('\n')
print(Solution().searchRange(nums = [], target = 0))
print('\n')
