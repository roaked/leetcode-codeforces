
"""Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border,
 or 0 if such a subgrid doesn't exist in the grid."""

from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_square = 0
        dp_horizontal = [[0] * m for _ in range(n)]
        dp_vertical = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp_horizontal[i][j] = 1 if j == 0 else dp_horizontal[i][j - 1] + 1
                    dp_vertical[i][j] = 1 if i == 0 else dp_vertical[i - 1][j] + 1

        for i in range(n):
            for j in range(m):
                side = min(dp_horizontal[i][j], dp_vertical[i][j])
                while side > max_square:
                    if min(dp_vertical[i][j - side + 1], dp_horizontal[i - side + 1][j]) >= side:
                        max_square = side
                        break
                    side -= 1

        return max_square * max_square

# print(Solution().largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]), '\n')
print(Solution().largest1BorderedSquare(grid = [[1,1,0,0]])) # 1
print(Solution().largest1BorderedSquare(grid = [[1,1,1,1]])) # 1
print(Solution().largest1BorderedSquare(grid = [[0,0,0,0]])) # 0
print(Solution().largest1BorderedSquare(grid = [[0]])) # 0
