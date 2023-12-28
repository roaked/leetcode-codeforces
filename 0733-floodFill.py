"""An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill."""

from typing import List
from collections import deque

class Solution():
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            m, n = len(image), len(image[0])
            init = image[sr][sc]

            if init == color:
                return image
            
            image[sr][sc] = color
            q = deque()
            q.append([sr,sc])

            while len(q)>0:
                a,b=q.popleft()

                if b>0 and image[a][b-1] == init: #left
                    image[a][b-1]=color
                    q.append([a,b-1])

                if b<n-1 and image[a][b+1] == init: #right
                    image[a][b+1]=color
                    q.append([a,b+1])

                if a>0 and image[a-1][b] == init: #up
                    image[a-1][b]=color
                    q.append([a-1,b])

                if a<m-1 and image[a+1][b] == init: #down
                    image[a+1][b]=color
                    q.append([a+1,b])
                    
            return image
    
print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
print(Solution().floodFill(image = [[0,0,0],[0,0,0]], sr = 1, sc = 0, color = 2))