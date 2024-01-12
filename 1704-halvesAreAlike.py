"""You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false."""

class Solution:
    def halvesAreAlike(self, s: str) -> bool: 
        s = s.lower()
        cnt = 0
        vowels = ['a','e','i','o','u']
        ans = s[:len(s)//2], s[len(s)//2:]
        for i in range(len(ans[0])):
            if ans[0][i] in vowels:
                cnt += 1
        for i in range(len(ans[1])):
            if ans[1][i] in vowels:
                cnt -= 1
        return True if cnt == 0 else False



print(Solution().halvesAreAlike(s = "Uo"))
print(Solution().halvesAreAlike(s = "textbook"))