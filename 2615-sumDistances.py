"""You are given a 0-indexed integer array nums. There exists an array arr of length nums.length,
 where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.
"""

class Solution:
    def sumDistances(self, nums: list[int]) -> list[int]:
        sol, dfs_sol, SIZE = [], [], len(nums)
        nums_initial = nums.copy()
        nums.sort()
        print(nums_initial)
        def dfs(combination, current_sum, idx):
            if len(combination) == 0:
                sol.append(idx)
            for i in range(idx, SIZE):
                dfs(combination + [nums[idx]], current_sum + abs(idx - i), i)
                
        dfs([],0,0)

        return sol
    

print(Solution().sumDistances(nums=[1,3,5,1,2]))

#print(Solution().sumDistances(nums=[0,5,3]))