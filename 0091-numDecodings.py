"""A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse 
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer."""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        counts = [0] * (n + 1)
        counts[0] = 1
        counts[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                counts[i] += counts[i - 1]

            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                counts[i] += counts[i - 2]

        return counts[n]
    
print(Solution().numDecodings(s = '12'))

print(Solution().numDecodings(s = '226'))

print(Solution().numDecodings(s = '06'))