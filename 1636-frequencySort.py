"""Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array."""

from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        r = Counter(nums).most_common()
        r.sort(key = lambda x: x[0], reverse=True)
        r.sort(key = lambda x: x[1])
        
        t = []
        for i in r:
            a, b = i
            t.extend([a]*b)
            
        return t

print(Solution().frequencySort(nums = [1,1,2,2,2,3]))