"""Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed)."""

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_count = [0] * rows
        col_count = [0] * cols
        cnt = 0

        for i in range(rows): #ro
            for j in range(cols): #co
                if mat[i][j] == 1:
                   row_count[i] += 1
                   col_count[j] += 1

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    cnt += 1

        return cnt

mat = [[1,0,0],[0,0,1],[1,0,0]]
print(Solution().numSpecial(mat))
print("\n")


mat = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().numSpecial(mat))
print("\n")