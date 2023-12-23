"""Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order."""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        sol = []
        while nums1 < nums2:
            for num in nums1:
                if num in nums2:
                    sol.append(num)
                    nums2.remove(num)
            return sol

        while nums1 >= nums2:
            for num in nums2:
                if num in nums1:
                    sol.append(num)
                    nums1.remove(num)
            return sol     
        return sol
    
    
print(Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print('\n')
print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))