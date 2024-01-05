"""Given an integer array nums, return the length of the longest strictly increasing subsequence."""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print('\n')
print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))
print('\n')
print(Solution().lengthOfLIS(nums = [7,7,7,7,7,7,7]))