"""Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.  """

class Solution:
    def countVowelStrings(self, n: int) -> int:

        if n == 0:
            return 1
        
        dp = [[0] * 5 for _ in range(n + 1)]

        for i in range(5): #base case 'a','e','i','o','u' ending
            dp[1][i] = 1
        #print(dp)

        for i in range(2, n + 1):
            for j in range(5):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        for row in dp:
            print(row)

        return sum(dp[n]) 

# print(Solution().countVowelStrings(n = 1))
# print(Solution().countVowelStrings(n = 2))
print(Solution().countVowelStrings(n = 0))
# print(Solution().countVowelStrings(n = 33))