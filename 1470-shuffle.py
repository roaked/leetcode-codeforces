"""Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ans = []
        for i in range(n):
            ans.append(nums[i]), ans.append(nums[i + n])
        return ans

print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))
print(Solution().shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(Solution().shuffle(nums = [1,1,2,2], n = 2))
