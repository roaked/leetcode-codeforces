"""You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

Choose two elements with equal values and delete them from the array.
Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible."""

from typing import List
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dictionary = Counter(nums)
        print(dictionary.values())
        count = 0
        for val in dictionary.values():
            print(val, '\n')
            if val == 1:
                return -1
            count += val // 3
            if val % 3:
                count += 1

        print('Ans:')
        return count
    
print(Solution().minOperations(nums = [2,3,3,2,2,4,2,3,4]))