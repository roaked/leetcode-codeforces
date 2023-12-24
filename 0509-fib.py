"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
 such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n)."""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if 1 < n <= 3:
            return n-1

        dp = [0] * (n+1) # n+1 places
        dp[1], dp[2], dp[3] = 1, 1, 2

        for i in range(4,n+1):
            dp[i] = dp[i-1] +dp[i-2]

        return dp[n]

        #return self.fib(n-1) + self.fib(n-2)

print(Solution().fib(n=1))
print(Solution().fib(n=2))
print(Solution().fib(n=3))
print(Solution().fib(n=4))