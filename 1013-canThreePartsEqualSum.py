"""Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == 
arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])"""

from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        part_sum, curr_sum, parts = sum(arr) / 3, 0, 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if(curr_sum == part_sum):
                parts += 1
                curr_sum = 0
                if (parts >= 3):
                    return True
                continue 
        return False
    
print(Solution().canThreePartsEqualSum(arr = [0,2,1,-6,6,-7,9,1,2,0,1]))

print(Solution().canThreePartsEqualSum(arr = [0,2,1,-6,6,7,9,-1,2,0,1])) #3

print(Solution().canThreePartsEqualSum(arr = [3,3,6,5,-2,2,5,1,-9,4]))

print(Solution().canThreePartsEqualSum(arr = [1,-1,1,-1])) #false