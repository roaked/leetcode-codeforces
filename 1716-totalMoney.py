"""Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 
more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day."""

class Solution:
    def totalMoney(self, n: int) -> int:
        if n > 7:
            pairs, remain, ans = n // 7, n % 7, 0
            one_round = sum(num for num in range(1,8))
            for i in range(pairs):
                ans += one_round + 7 * i
            for i in range(remain):
                ans += i + pairs + 1
            return ans
        else:
            return sum(num for num in range(1, n+1))
    
print(Solution().totalMoney(n = 10))
print(Solution().totalMoney(n = 20))