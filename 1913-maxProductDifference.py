"""The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference."""


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        size = len(nums)
        numsOriginal = nums.copy()
        nums.sort()
        # product = (a*b) - (c*d)
        while nums:
            print(nums[size-1]* nums[size-2] - nums[0] * nums[1])
            return nums[size-1]* nums[size-2] - nums[0] * nums[1]

        return 0
    
print(Solution().maxProductDifference(nums = [5,6,2,7,4]))      
print('\n')
print(Solution().maxProductDifference(nums = [4,2,5,9,7,4,8]))
print('\n')
