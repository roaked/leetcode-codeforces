"""You are given positive integers n and m.

Define two integers, num1 and num2, as follows:

num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.
Return the integer num1 - num2."""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = [], []
        for i in range(1, n+1):
            if i % m == 0:
                num2.append(i)
            else:
                num1.append(i)
                
                
        return sum(num1) - sum(num2)
        
print(Solution().differenceOfSums(n = 10, m = 3))