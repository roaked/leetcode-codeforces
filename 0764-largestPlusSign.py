"""You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines.
 The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1
 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, 
only the relevant area of the plus sign is checked for 1's."""

from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * (n) for _ in range(n)] # comprehension dp
        for mine in mines:
            grid[mine[0]][mine[1]] = 0

        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
        ans = 0

        for i in range(n):
            count_left, count_up, count_right, count_down = 0, 0, 0, 0
            for j in range(n):
                count_left = count_left + 1 if grid[i][j] else 0
                dp[i][j][0] = count_left
                
                count_up = count_up + 1 if grid[j][i] else 0
                dp[j][i][1] = count_up
                
            for j in range(n - 1, -1, -1):
                count_right = count_right + 1 if grid[i][j] else 0
                dp[i][j][2] = count_right
                
                count_down = count_down + 1 if grid[j][i] else 0
                dp[j][i][3] = count_down
        
        for i in range(n):
            for j in range(n):
                ans = max(ans, min(dp[i][j]))

        for row in dp:
            print(row)
        
        return ans
    
print(Solution().orderOfLargestPlusSign(n = 5, mines = [[4,2]]), '\n')
print(Solution().orderOfLargestPlusSign(n = 2, mines = [[0,0],[0,1],[1,0],[1,1]]))