"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] 
that do not appear in nums."""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        size = len(nums)
        mumsset = set(nums)
        sol = []
        for i in range(1,size+1):
            if i not in mumsset:
               sol.append(i)
        return sol

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))
print("\n")

nums = [1,1]
print(Solution().findDisappearedNumbers(nums))