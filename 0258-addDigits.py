"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""


class Solution:
    def addDigits(self, num: int) -> int:

        ans = 0
        s = str(num)
        for c in s:
            ans += int(c)
            
        if ans < 10:
            return ans
        else:
            return self.addDigits(ans)
    
print(Solution().addDigits(num = 38))