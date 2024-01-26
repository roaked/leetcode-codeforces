"""Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr"""

from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans, min_value, l, r = [], float('inf'), 0, 1
        arr.sort()
        while r < len(arr):
            min_value = min(min_value, arr[r]-arr[l])
            l, r = l+1, r+1

        l,r = 0,1
        while r < len(arr):
            if (arr[r]-arr[l]) == min_value:
                ans.append([arr[l],arr[r]])
            l, r = l+1, r+1
        return ans


print(Solution().minimumAbsDifference(arr = [4,2,1,3]))