"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool: 
        occurrences = {}
        
        for num in arr:
            occurrences[num] = occurrences.get(num, 0) + 1
        
        return len(set(occurrences.values())) == len(occurrences)

print(Solution().uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])) #array.length = 10; 4 diff uniques

# 1 -> 1 //1
# 2 -> 0
# 3 -> 2 // 0.5
# 4 -> 0  // 1
# 5 -> 0 // 1.5
# 6 -> 3 // 2
# 10 -> 4 // 2.5
# 15 -> 5  // 3
# 21 -> 6 // 3.5
# 28 -> 7  // 4
# 36 -> 8  // 4.5

