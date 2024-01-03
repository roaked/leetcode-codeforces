"""Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array."""

from typing import List
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if list(set(nums1) & set(nums2)):
            return min(list(set(nums1) & set(nums2)))
        
        m1, m2 = min(nums1), min(nums2)
        if(m1 <= m2):
            return int(str(m1)+str(m2))
        else:
            return int(str(m2)+str(m1))

        

print(Solution().minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))
print(Solution().minNumber(nums1 = [4,1,3], nums2 = [5,7]))
