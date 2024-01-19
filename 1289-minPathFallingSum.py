"""Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that
 no two elements chosen in adjacent rows are in the same column."""

from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        if len(grid) == 1:
            return min(min(grid))

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp = grid.copy()
        for i in range(len(grid)-1):
            for j in range(len(grid[0])):
                if j == 0: # wall left
                    dp[i+1][j] += min(dp[i][j+1:])

                elif 0 < j < len(grid[0]) - 1: # mid 
                    #ans1, ans2 = min(dp[i][:j]), min(dp[i][j+1:])           
                    dp[i+1][j] += min(min(dp[i][:j]), min(dp[i][j+1:])  )

                else: # wall right
                    dp[i+1][j] += min(dp[i][:j])

        return min(dp[-1])
    
print(Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]), '\n')
print(Solution().minFallingPathSum(grid = [[7]]))
print(Solution().minFallingPathSum(grid = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]])) #-192