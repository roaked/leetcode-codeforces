"""You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix."""

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
    
        n = len(grid) # rows = cols
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        print(ans)
        for i in range(n-2):
            for j in range(n-2):
                window = [row[j:j + 3] for row in grid[i:i + 3]]
                max_val = max(max(row) for row in window)
                ans[i][j] = max_val

        return ans
        

print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))