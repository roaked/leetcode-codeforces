"""Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices."""

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        ans =  [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)): #rows
            for j in range(len(matrix[0])): #columns 
                ans[j][i] = matrix[i][j]
        return ans
    
        # return list(zip(*matrix))
    
# print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().transpose(matrix = [[1,2,3],[4,5,6]]))

