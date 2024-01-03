"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top"""

class Solution:
    def climbStairsRecursive(self, n: int) -> int:

        if n <= 3:
            return n  
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n  
        
        dp = [0] * (n+1) # n+1 places
        dp[1], dp[2], dp[3] = 1, 2, 3

        for i in range(4,n+1):
            dp[i] = dp[i-1] +dp[i-2]

        return dp[n]


print(Solution().climbStairs(n=2)) #2
print(Solution().climbStairs(n=3)) #3
print(Solution().climbStairs(n=4)) #5
print(Solution().climbStairs(n=5)) #8
print(Solution().climbStairs(n=44)) #int