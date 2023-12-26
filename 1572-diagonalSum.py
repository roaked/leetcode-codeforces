"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements
 on the secondary diagonal that are not part of the primary diagonal."""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cnt, n, i, j = 0, len(mat), 0, 0
        while(0 <= i < n and 0 <= j < n):
            cnt += mat[i][j]
            mat[i][j] = 0
            i += 1
            j += 1

        i,j = len(mat)-1, 0
        while(0 <= i < n and 0 <= j < n):
            cnt += mat[i][j]
            i -=1
            j +=1
        
        return cnt

print(Solution().diagonalSum(mat = [[1,2,3],[4,5,6],[7,8,9]])) 
print(Solution().diagonalSum(mat = [[1,1,1,2],[1,3,4,1],[1,1,1,1],[1,1,1,1]])) 