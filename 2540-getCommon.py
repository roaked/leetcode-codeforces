"""Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
 If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer."""

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        while(len(nums1) > 0 and len(nums2) > 0):
            if nums1[0] == nums2[0]:
                return nums1[0]
            elif nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        return -1


print(Solution().getCommon(nums1 = [1,2,3], nums2 = [2,4]))