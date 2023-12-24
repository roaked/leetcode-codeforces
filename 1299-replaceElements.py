"""Given an array arr, replace every element in that array with the greatest element among the elements to its right,
 and replace the last element with -1.

After doing so, return the array."""

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr) 
        max_val = -1  

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = max_val  
            max_val = max(max_val, arr[i])  

        return ans
    
print(Solution().replaceElements(arr = [17,18,5,4,6,1]))

print(Solution().replaceElements(arr = [400]))