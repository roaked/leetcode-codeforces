"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
 If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        if (len(nums)) == 1:
            if(nums[0] == target):
                return 0
            else:
                return -1

        l, r, m = 0, -1, len(nums)//2
        if (nums[m] > target):
            while(nums[l] < nums[r]):
                if (nums[l] == target):
                    return l
                l += 1

        else:
            while(nums[r] >= nums[m]):
                if (nums[r] == target):
                    return len(nums) + r
                
                r -= 1

        return -1
        

print(Solution().search(nums = [-1,0,3,5,9,12], target = 9))
print('\n')
print(Solution().search(nums = [-1,0,3,5,9,12], target = 2))
print('\n')
print(Solution().search(nums = [-1], target = 2))
