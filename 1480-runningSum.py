"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums."""


from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cnt, ans = 0, []
        for i in range(len(nums)):      
            cnt += nums[i]
            ans.append(cnt)
        return ans


print(Solution().runningSum(nums = [1,2,3,4]))