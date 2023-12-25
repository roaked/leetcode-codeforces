
import math

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ans = ''
        for char in nums:
            ans += str(char)
        res = 0
        for i in range(len(ans)):
            res += int(ans[i])
        return abs(sum(nums) - res) 
    

    def differenceOfSum2(self, nums: list[int]) -> int:
        ans = 0
        temp = None
        for i in range(len(nums)):
            temp = nums[i]
            if(nums[i]>9):
                while(temp > 9):
                    rest = temp % 10
                    temp = temp // 10
                    ans+= rest
                ans += temp
            else:
                ans += nums[i]
                

            return abs(sum(nums) - ans)


        
print(Solution().differenceOfSum(nums = [1,15,6,3]))
        