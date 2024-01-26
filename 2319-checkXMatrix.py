"""A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false."""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if((i!=j and i+j!=len(grid)-1) and grid[i][j] != 0):
                    return False
                elif((i==j or i+j==len(grid)-1) and grid[i][j] == 0):
                    return False
        return True
    
print(Solution().checkXMatrix(grid = [[2,0,0,0,1],[0,4,0,1,5],[0,0,5,0,0],[0,5,0,2,0],[4,0,0,0,2]]))