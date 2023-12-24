"""Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution."""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        n = len(nums)

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum

                if curr_sum < target:
                    l += 1
                else:
                    r -= 1

            if min_diff == 0:
                break

        return closest_sum

print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))

print(Solution().threeSumClosest(nums = [0,0,0], target = 1))