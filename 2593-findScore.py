"""You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm."""


from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [False] * n
        score = 0
        for v, k in sorted((i, e) for e, i in enumerate(nums)):
            if dp[k]: continue
            if k > 0: dp[k - 1] = True
            if k < n - 1: dp[k + 1] = True
            score += v
        return score
    
# print(Solution().findScore(nums = [2,1,3,4,5,2]))
# print(Solution().findScore(nums = [2,3,5,1,3,2]))
print(Solution().findScore(nums = [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))   