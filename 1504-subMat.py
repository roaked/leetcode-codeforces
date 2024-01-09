"""Given an m x n binary matrix mat, return the number of submatrices that have all ones."""

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        result = 0
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1

        for i in range(rows):
            for j in range(cols):
                min_width = float('inf')
                for k in range(i, -1, -1):  
                    min_width = min(min_width, dp[k][j])
                    if min_width == 0:
                        break
                    result += min_width
        
        return result

    
print(Solution().numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]]))

