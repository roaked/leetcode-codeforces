"""Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
 The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is 
[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1]."""

from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l,r, cnt, ans = 0, 1, 1, 1
        while r < len(nums):
            if nums[r] > nums[l]:
                cnt += 1
                r, l = r+1, l+1
                ans = max(ans, cnt)
            else:
                cnt = 1
                l, r = r, r+1
        return ans


print(Solution().findLengthOfLCIS(nums = [1,3,5,4,7]))