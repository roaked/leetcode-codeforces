from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            n = target - num
            print(n, idx, num, d)
            if n in d:
                return [idx, d[n]]
            else:
                d[num] = idx

print(Solution().twoSum(nums = [2,7,11,15], target = 9))