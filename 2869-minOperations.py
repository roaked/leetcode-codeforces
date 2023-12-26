"""You are given an array nums of positive integers and an integer k.

In one operation, you can remove the last element of the array and add it to your collection.

Return the minimum number of operations needed to collect elements 1, 2, ..., k."""


from typing import List
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt, seen = 0, set()
        while(len(seen) < k):
            if (nums[-1] <= k):                     
                seen.add(nums[-1])
            cnt += 1
            nums.pop()              

        return cnt


print(Solution().minOperations(nums = [3,1,5,4,2], k = 2))
        