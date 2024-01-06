"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area."""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0]) # rows, columns
        dp, ans = [[0] * (m) for _ in range(n)], 0
        for row in range(n):
            for col in range(m):
                if matrix[row][col] != "0": # not null
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1

                    ans = max(ans, dp[row][col])  
        for row in matrix:
            print(row)
        for row in dp:
            print(row)

        return ans * ans


print(Solution().maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 6