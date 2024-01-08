"""Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column."""

from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [num for num in [min(row) for row in matrix] if num in [max(row) for row in zip(*matrix)]]



print(Solution().luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))