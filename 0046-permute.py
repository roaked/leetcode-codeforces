"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(path, nums): #paths, available nums
            if not nums:
                result.append(path)
                return

            for i in range(len(nums)):
                dfs(path + [nums[i]], nums[:i] + nums[i + 1:]) #skip value i for available nums

        result = []
        dfs([], nums)
        return result
    
print(Solution().permute(nums = [1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(Solution().permute(nums = [0,1]))
print(Solution().permute(nums = [1]))