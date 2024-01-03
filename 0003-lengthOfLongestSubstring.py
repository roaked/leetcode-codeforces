"""Given a string s, find the length of the longest substring without repeating characters."""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = {}
        max_length = start = 0
        
        for i, char in enumerate(s):
            if char in res and res[char] >= start:
                start = res[char] + 1
            res[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length
    
print(Solution().lengthOfLongestSubstring(s = "abcabcbb"))
print('\n')   
print(Solution().lengthOfLongestSubstring(s = "bbbbb"))
print('\n')
print(Solution().lengthOfLongestSubstring(s = "pwwkew"))
