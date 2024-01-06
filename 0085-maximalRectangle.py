"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area."""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0]) # rows, columns
        dp, ans = [[0] * (m) for _ in range(n)], 0

        for row in range(n):
            dp[row][0] = 1 if matrix[row][0] == '1' else 0

        for row in range(n):
            for col in range(1, m):
                if matrix[row][col] == '1':
                    dp[row][col] = dp[row][col - 1] + 1 if dp[row][col - 1] else 1

        for j in range(m):
            column = []
            for i in range(n):
                column.append(dp[i][j])
            
            for p in range(len(column)):
                left = right = p
                val = column[p]
                cnt = 1

                while left >= 0 and column[left] >= val:
                    if left != p:
                        cnt += 1
                    left -= 1
                
                while right < len(column) and column[right] >= val:
                    if right != p:
                        cnt += 1
                    right += 1

                ans = max(ans, val * cnt)  
        # print(column, '\n')
        # for row in dp:
        #     print(row)
        return ans


print(Solution().maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 6