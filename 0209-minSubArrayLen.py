"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if target in nums:
            return 1

        if not nums: 
            return 0
        
        left, curr_sum, ans, found = 0, 0, float('inf'), False
        
        # def dfs(start, curr_sum):
        #     if curr_sum >= target:
        #         ans = min(ans, start - left)    
        #         return
        #     if start == len(nums):
        #         return
            
        #     dfs(start + 1, curr_sum + nums[start])
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                found = True
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
        #dfs(0, 0)
        return ans if found else 0

        
    
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print('\n')
print(Solution().minSubArrayLen(target = 4, nums = [1,4,4]))
print('\n')
print(Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))