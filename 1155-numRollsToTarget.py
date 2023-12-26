"""You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice,
 so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7."""


class Solution:
    mod = 10 ** 9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = [[-1] * (target + 1) for i in range(n+1)]
        print(dp)
        return self.recursion(dp, n, k, target)

    def recursion(self, dp: list, n: int, k: int, target: int) -> int:
        if target == 0 and n == 0:
            return 1
        if n == 0 or target < 0:
            return 0 
        
        if dp[n][target] != -1:
            return dp[n][target] % self.mod
        
        ways = 0
        for i in range(1, 1+k):
            ways = (ways + self.recursion(dp, n-1, k, target-i)) % self.mod

        dp[n][target] = ways % self.mod
        return dp[n][target]



print(Solution().numRollsToTarget(n = 1, k = 6, target = 3))

print(Solution().numRollsToTarget(n = 2, k = 6, target = 7))