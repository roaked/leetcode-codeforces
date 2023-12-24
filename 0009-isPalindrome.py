"""Given an integer x, return true if x is a palindrome , and false otherwise."""
#An integer is a palindrome when it reads the same forward and backward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        
        while x>=0:
            for i in range(len(ans)-1):
                if ans[i] != ans[len(ans)-1-i]:
                    return False
            return True       
        return False #negatives

print(Solution().isPalindrome(x = 121)) #t
print(Solution().isPalindrome(x = 123123)) #f
print(Solution().isPalindrome(x = 10)) #f
print(Solution().isPalindrome(x = -10)) #false
print(Solution().isPalindrome(x = 0)) #t
print(Solution().isPalindrome(x = 1)) #t
print(Solution().isPalindrome(x = 100)) #f
print(Solution().isPalindrome(x = 123)) #f
