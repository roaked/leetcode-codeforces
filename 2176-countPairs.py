"""Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, 
such that nums[i] == nums[j] and (i * j) is divisible by k"""


from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and  (i * j) % k == 0:
                    ans += 1
        return ans


print(Solution().countPairs(nums = [3,1,2,2,2,1,3], k = 2))