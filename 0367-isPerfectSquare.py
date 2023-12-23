"""Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt."""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num > 0:
            t = int(num**0.5)
            return t*t == num

    
print(Solution().isPerfectSquare(num = 16))
print('\n')
print(Solution().isPerfectSquare(num = 14))
print('\n')
print(Solution().isPerfectSquare(num = 36)) 