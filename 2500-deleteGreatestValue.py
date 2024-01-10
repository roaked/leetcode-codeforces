"""You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above."""

from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for i in range(0, len(grid)):
            grid[i].sort()

        n = len(grid[0])
        res = 0
        for j in range(0, n):
            ans = 0
            for i in range(0, len(grid)):
                ans = max(ans, grid[i].pop())
            res += ans
        return res

print(Solution().deleteGreatestValue(grid = [[1,2,4],[3,3,1]]))   