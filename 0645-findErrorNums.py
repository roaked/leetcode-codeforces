"""You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array."""

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set([i for i in range(1, len(nums)+1)])

        for i in nums: 
            if i in seen:
                seen.remove(i)
            else: 
                dupe = i
        return [dupe, seen.pop()]


print(Solution().findErrorNums(nums = [3,2,2]))
print(Solution().findErrorNums(nums = [1,2,2,4]))
print(Solution().findErrorNums(nums = [3,2,3,4,6,5]))
print(Solution().findErrorNums(nums = [1,5,3,2,2,7,6,4,8,9]))
