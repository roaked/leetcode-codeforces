"""Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted."""

from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        cnt, rem = 0, .05*len(arr)
        arr.sort()
        while (cnt < rem):
            arr.pop(-1)
            arr.pop(0)
            cnt +=1
        return sum(arr) / len(arr)
    
print(Solution().trimMean(arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])) 
#4.77778