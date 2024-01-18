"""An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number."""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2

        while n % 3 == 0:
            n //= 3

        while n % 5 == 0:
            n //= 5
            
        return n == 1


print(Solution().isUgly(n = 6))