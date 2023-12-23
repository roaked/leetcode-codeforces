"""Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order."""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sol = []
        while nums1 < nums2:
            for num in nums1:
                if num in nums2 and num not in sol:
                    sol.append(num)
            return sol

        while nums1 >= nums2:
            for num in nums2:
                if num in nums1 and num not in sol:
                    sol.append(num)
            return sol     
        return sol
    
    def intersection2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        intersection_set = set1.intersection(set2)
        
        return list(intersection_set)
    
print(Solution().intersection2(nums1 = [1,2,2,1], nums2 = [2,2]))
print('\n')
print(Solution().intersection2(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
