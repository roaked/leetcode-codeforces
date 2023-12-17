"""You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets."""

#diff - nums[j] = nums[i] or diff + nums[j] = nums[k]

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n, cnt = len(nums), 0 
        while nums:
            for j in range(n):
                if nums[j] - diff in nums and nums[j] + diff in nums:
                    cnt += 1
            return cnt

print(Solution().arithmeticTriplets(nums = [4,5,6,7,8,], diff = 2))
print('\n')
print(Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print('\n')
print(Solution().arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))
print('\n')