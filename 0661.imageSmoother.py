
"""An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell 
and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). 
If one or more of the surrounding cells of a cell is not present,
 we do not consider it in the average (i.e., the average of the four cells in the red smoother)."""

class Solution:
    def imageSmoother(matrix):
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for r in range(max(0, i - 1), min(m, i + 2)):
                    for c in range(max(0, j - 1), min(n, j + 2)):
                        total += matrix[r][c]
                        count += 1

                result[i][j] = total // count

        return result
    

print(Solution().imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))