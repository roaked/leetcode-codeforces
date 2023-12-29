"""Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order."""
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res, a, b = [], [], []
        a, b = set(nums1) - set(nums2), set(nums2) - set(nums1)
        res.append(a), res.append(b)
        return res
print(Solution().findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))