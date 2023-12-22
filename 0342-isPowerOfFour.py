"""Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x."""
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n == 4**round(math.log(n, 4))
    
n = 16
print(Solution().isPowerOfFour(n))

n = 5
print(Solution().isPowerOfFour(n))

n = 1
print(Solution().isPowerOfFour(n))

n = 0
print(Solution().isPowerOfFour(n))

n = -1
print(Solution().isPowerOfFour(n))
