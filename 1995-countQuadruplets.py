
"""Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d"""

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for w in range(k + 1, len(nums)):
                        if (nums[i] + nums[j] + nums[k] == nums[w]):
                            ans += 1

        return ans

print(Solution().countQuadruplets(nums = [1,2,3,6]))
print(Solution().countQuadruplets(nums = [3,3,6,4,5]))