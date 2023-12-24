"""Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements."""

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                print(matrix[i][j], matrix[j][i])
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
    
print(Solution().isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

print(Solution().isToeplitzMatrix(matrix = [[1,2],[2,2]]))