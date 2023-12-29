
"""You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.

Consider calculating the following values:

The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
Return an integer array answer of size 2 containing the two values in the above order."""

from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [sum(n in nums2 for n in nums1), sum(n in nums1 for n in nums2)]

print(Solution().findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]))

print(Solution().findIntersectionValues(nums1 = [3,4,2,3], nums2 = [1,5]))