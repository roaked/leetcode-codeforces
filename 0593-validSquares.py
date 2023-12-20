"""Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point p_i is represented as [x_i, y_i]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles)."""


class Solution:

    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        

        return True 
    
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print('\n')
print(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print('\n')
print(Solution().validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))
print('\n')