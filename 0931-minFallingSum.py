"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either 
directly below or diagonally left/right. Specifically, the next element from position (row, col) will be 
(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)."""

from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dp = matrix.copy()
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])):
                if j == 0: # wall left
                    dp[i+1][j] += min(dp[i][j], dp[i][j+1])

                elif 0 < j < len(matrix[0]) - 1: # mid             
                    dp[i+1][j] += min(dp[i][j], dp[i][j+1], dp[i][j-1])

                else: # wall right
                    dp[i+1][j] += min(dp[i][j], dp[i][j-1])

        return min(dp[-1])
            
print(Solution().minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))