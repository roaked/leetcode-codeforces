"""You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. 
Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array."""


class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:

        n, val = len(nums), None
        numsOriginal = nums.copy()
        numsOriginal.sort()
        cnt = 0
        minimum, maximum = numsOriginal[0], numsOriginal[n-1]
        while minimum and maximum in nums:
            for i in range(n-1):
                nums.pop()
                cnt += 1 
            return val 

        return 0


print(Solution().minimumDeletions(nums = [2,10,7,5,4,1,8,6]))
print('\n')
print(Solution().minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))
print('\n')