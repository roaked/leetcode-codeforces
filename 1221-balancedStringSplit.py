"""Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain."""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, pair = 0, 0
        for char in s:
            if char == 'R':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                pair += 1
        return pair


print(Solution().balancedStringSplit(s = "RLRRLLRLRL"))
print(Solution().balancedStringSplit(s = "RRLRRLRLLLRL"))
