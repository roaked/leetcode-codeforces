"""Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        #already sorted and distinct ints ---> binary search O(log n) time complexity
        size = len(nums)
        left, right = 0, size - 1
        
        if size == 1:
            return 0 if target <= nums[0] else 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
print(Solution().searchInsert(nums = [1,3,5,6], target = 5))

print(Solution().searchInsert(nums = [1,3,5,6], target = 2))

print(Solution().searchInsert(nums = [1,3,5,6], target = 7))

print(Solution().searchInsert(nums = [1], target = 1))

print(Solution().searchInsert(nums = [1, 3], target = 3))