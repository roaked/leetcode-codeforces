"""
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. 
Note that abs(x) is the absolute value of x.

Return abs(i - start).
It is guaranteed that target exists in nums.
"""


class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        while nums:
            size = len(nums)
            mini = 10000
            cnt = 0
            for i in range(size):
                if nums[i] == target and cnt == 0:
                    mini = abs(i-start) # min = abs(0-1) = 1
                    cnt += 1
                if nums[i] == target and abs(i-start) < mini: # abs(9-0) = 9 < min / abs(0-0) = 0
                    mini = abs(i-start)
            return mini
        
#nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
nums = [1,2,3,4,5]
target = 5
start = 3
print(Solution().getMinDistance(nums, target, start))
print("\n")

nums = [1]
target = 1
start = 0
print(Solution().getMinDistance(nums, target, start))
print("\n")

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0
print(Solution().getMinDistance(nums, target, start))
print("\n")
