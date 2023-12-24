"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) <= 2:
            return False
        
        peak_index = arr.index(max(arr))
        
        if peak_index == 0 or peak_index == len(arr) - 1:
            return False
        
        for i in range(peak_index):
            if arr[i] >= arr[i + 1]:
                return False
        
        for i in range(peak_index, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        
        return True
        

print(Solution().validMountainArray(arr = [0,1,2,3,4,5,6,7,8,9])) #f
print(Solution().validMountainArray(arr = [3,5,5])) #f
print(Solution().validMountainArray(arr = [0,1,2,4,2,1])) #t