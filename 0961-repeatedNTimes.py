"""You are given an integer array nums with the following properties:

- nums.length == 2 * n.
-nums contains n + 1 unique elements.
- Exactly one element of nums is repeated n times.
Return the element that is repeated n times."""


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int: #multiple 2
        nums.sort()
        size = len(nums)
        n, cnt = size / 2, 1
        for _ in range(size):
            if cnt == n:
                return nums[_]       
            else: 
                cnt += 1 if nums[_+1] == nums[_] else cnt == 1

    
print(Solution().repeatedNTimes(nums = [1,2,3,3]))
print('\n')
print(Solution().repeatedNTimes(nums = [2,1,2,5,3,2])) # 2
print('\n')
print(Solution().repeatedNTimes(nums = [5,1,5,2,5,3,5,4])) # 5 - (1,2,3,4,5,5,5,5)
print('\n')
print(Solution().repeatedNTimes(nums = [9,5,3,3]))
