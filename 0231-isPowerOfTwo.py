"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if not n > 0: return False
        return pow(2, int(math.log(n, 2))) == n


print(Solution().isPowerOfTwo(n = 3))
print(Solution().isPowerOfTwo(n = 1))