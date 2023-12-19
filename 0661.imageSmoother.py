
"""An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell 
and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). 
If one or more of the surrounding cells of a cell is not present,
 we do not consider it in the average (i.e., the average of the four cells in the red smoother)."""

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        r, c = len(img), len(img[0]) # rows, columns
        n = [0] * r
        m = [0] * r

        for row in range(r):
            for column in range(c):
                while img:
                    m[row][column] = m[row][column] // 4
            

        return 1
    

print(Solution().imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))