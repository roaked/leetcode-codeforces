"""Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that 
are present in at least two out of the three arrays. You may return the values in any order."""

from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        nums1c = nums1.copy()
        nums1.extend(nums2), nums1.extend(nums3)
        nums = set(nums1)
        for num in nums:
            if (num in nums1c and num in nums2) or (num in nums2 and num in nums3) or (num in nums1c and num in nums3):
                ans.append(num)
        return ans

print(Solution().twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))

print(Solution().twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))

print(Solution().twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))