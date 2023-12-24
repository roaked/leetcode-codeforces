"""You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly
 k times in order to maximize your score:

Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing the operation exactly k times."""

import math

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        curr = 0
        while (k != 0):
            curr += nums[0]
            nums[0] += 1
            k -= 1
        return curr

    # nums[0] + nums[0] + 1 + nums[0] + 2 (k=3)

    def maximizeSum2(self, nums, k):
        nums.sort(reverse=True)
        return int(nums[0]*k + (k-1)*k/2)

print(Solution().maximizeSum2(nums = [1,2,3,4,5], k = 3))

print(Solution().maximizeSum2(nums = [5,5,5], k = 2))
