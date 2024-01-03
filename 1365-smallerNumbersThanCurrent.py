"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):

                if i == j:
                    continue
                if nums[i] > nums[j]:
                    cnt += 1
                
                ans[i] = cnt
        return ans 
    
print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3]))

print(Solution().smallerNumbersThanCurrent(nums = [6,5,4,8]))

print(Solution().smallerNumbersThanCurrent(nums = [7,7,7,7]))