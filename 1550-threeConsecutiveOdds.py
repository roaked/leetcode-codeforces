"""Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false."""

from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False
    
print(Solution().threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12]))
print(Solution().threeConsecutiveOdds(arr = [1,1,1])) # true
print(Solution().threeConsecutiveOdds(arr = [1,2,1,1])) # false