"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, t = len(nums1), len(nums2), len(nums1) + len(nums2)
        l, r = 0, t
        ans = [0] * t # size of ans
        mid = l + (r - l) //2
        while():
            pass

        return ans
    
print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print('\n')
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print('\n')