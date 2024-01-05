"""Given a m * n matrix of ones and zeros, return how many square submatrices have all ones."""


from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0]) # rows, columns
        dp = [[0] * (m+1) for _ in range(n+1)] #solutions have 1 

        for row in range(n):
            for col in range(m):
                if matrix[row][col]: # non null
                    dp[row+1][col+1] = min(dp[row][col+1], dp[row+1][col], dp[row][col]) + 1

        return sum(sum(row) for row in dp)
    
print(Solution().countSquares(matrix =
                              [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])) # output = 15