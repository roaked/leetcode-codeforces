"""You are given a 0-indexed integer array nums. There exists an array arr of length nums.length,
 where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. 
 If there is no such j, set arr[i] to be 0.

Return the array arr.
"""
from collections import defaultdict

class Solution:
    def sumDistances(self, nums: list[int]) -> list[int]:
        size = len(nums)
        arr = [0] * size
        
        sums = defaultdict(int)
        counts = defaultdict(int)
        
        for i, x in enumerate(nums):
            arr[i] = i * counts[x] - sums[x]
            sums[x] += i
            counts[x] += 1
            
        sums = defaultdict(int)
        counts = defaultdict(int)
        for i, x in enumerate(reversed(nums)):
            arr[size - i - 1] += i * counts[x] - sums[x]
            sums[x] += i
            counts[x] += 1
        return arr

print(Solution().sumDistances(nums=[1,3,5,1,2]))

#print(Solution().sumDistances(nums=[0,5,3]))