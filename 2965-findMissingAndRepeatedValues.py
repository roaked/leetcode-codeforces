"""You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
 Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b."""

from typing import List
from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash_map = defaultdict(int)
        n = len(grid)

        for num in range(1 , (n**2) + 1):
            hash_map[num] = 0

        for row in grid:
            for num in row:
                hash_map[num] = hash_map[num] + 1

        a , b = 0 , 0

        for key in hash_map:

            if hash_map[key] == 2:
                a = key

            if hash_map[key] == 0:
                b = key

        return [a , b]

print(Solution().findMissingAndRepeatedValues(grid = [[1,3],[2,2]]))
print(Solution().findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))

#1+3+2+2 = 8  // 1+2+3+4 = 10 ()

