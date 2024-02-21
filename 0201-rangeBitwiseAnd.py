"""Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive."""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
    
print(Solution().rangeBitwiseAnd(left = 1, right = 2147483647))