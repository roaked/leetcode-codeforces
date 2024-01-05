"""Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time."""


from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m, ans = len(grid), len(grid[0]), 0
        dp = [[0] * (m) for _ in range(n)]
        dp[0][0] = grid[0][0] # base case

        if (n == 1):
            return sum(grid[0][:])
        
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                if row == 0:
                    dp[row][col] = dp[row][col-1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row-1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
        return min(dp[n-2][m-1], dp[n-1][m-2]) + grid[n-1][m-1]
    
print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]), '\n')
print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]), '\n')
print(Solution().minPathSum(grid = [[1]]), '\n')
print(Solution().minPathSum(grid = [[9,1,4,8]]), '\n')
print(Solution().minPathSum(grid = [[0,2,2,6,4,1,6,2,9,9,5,8,4,4],
                                    [0,3,6,4,5,5,9,7,8,3,9,9,5,4],
                                    [6,9,0,7,2,2,5,6,3,1,0,4,2,5],
                                    [3,8,2,3,2,8,8,7,5,9,6,3,4,5],
                                    [4,0,1,3,9,2,0,1,6,7,9,2,8,9],
                                    [6,2,7,9,0,9,5,2,7,5,1,4,4,7],
                                    [9,8,3,3,0,6,8,0,8,8,3,5,7,3],
                                    [7,7,4,5,9,1,5,0,2,2,2,1,7,4],
                                    [5,1,3,4,1,6,0,4,3,8,4,3,9,9],
                                    [0,6,4,9,4,1,5,5,4,2,5,7,4,0],
                                    [0,1,6,6,4,9,2,7,8,2,1,3,3,7],
                                    [8,4,9,9,2,3,8,6,6,5,4,1,7,9]]), '\n')  