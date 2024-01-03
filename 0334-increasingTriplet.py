"""Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false."""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         continue
        #     for j in range(i+1, len(nums)-1):
        #         if nums[j] == nums[j+1]:
        #             continue
        #         for k in range(j+1, len(nums)-1):
        #             if nums[k] == nums[k+1]:
        #                 continue
        #             if (nums[i] < nums[j] < nums[k]):
        #                 return True
        # return False
    
print(Solution().increasingTriplet(nums = [1,2,3,4,5]))
print(Solution().increasingTriplet(nums = [5,4,3,2,1]))
print(Solution().increasingTriplet(nums = [4,10,5,1,2,3,-9,-7,-10]))
print(Solution().increasingTriplet(nums =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                                          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))