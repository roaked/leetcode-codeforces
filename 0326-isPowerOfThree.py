"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x -> log3 (n) = x
"""
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and n == 3**round(math.log(n, 3))
    
n = 45
print(Solution().isPowerOfThree(n))

n = 1000
print(Solution().isPowerOfThree(n))

n = 27
print(Solution().isPowerOfThree(n))

n = 0
print(Solution().isPowerOfThree(n))

n = -1
print(Solution().isPowerOfThree(n))