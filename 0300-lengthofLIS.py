"""Given an integer array nums, return the length of the longest strictly increasing subsequence."""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n, curr, ans = len(nums), 1, -1
        if n == 1: # case len 1
            return 1

        for i in range(n-1):
            if(nums[i+1] > nums[1]):
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1

        
        return ans if ans != -1 else 1
    

print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print('\n')
print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))
print('\n')
print(Solution().lengthOfLIS(nums = [7,7,7,7,7,7,7]))