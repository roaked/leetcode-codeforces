"""There are n teams numbered from 0 to n - 1 in a tournament.

Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger 
than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament."""


from typing import List
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        maxi = max(sum(grid[i]) for i in range(len(grid)))
        for i in range(len(grid)):
            if sum(grid[i]) == maxi:
                return i
    
# print(Solution().findChampion(grid = [[0,1],[0,0]]))
print(Solution().findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]]))