"""Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        ans = 0
        
        for num in nums:
            if num in count:
                ans += count[num]
                count[num] += 1
            else:
                count[num] = 1
        return ans
    
print(Solution().numIdenticalPairs(nums = [1,2,3,1,1,3]))

print(Solution().numIdenticalPairs(nums = [1,1,1,1]))

print(Solution().numIdenticalPairs(nums = [1,2,3]))