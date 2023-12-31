"""Given a string s, return the length of the longest substring between two equal characters, excluding the two characters.
If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string."""

from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = defaultdict(lambda: -1)
        max_distance = -1
        for i, char in enumerate(s):
            if char_index[char] == -1:
                char_index[char] = i
            else:
                max_distance = max(max_distance, i - char_index[char] - 1)     
        return max_distance

print(Solution().maxLengthBetweenEqualCharacters(s = "aa"))
print(Solution().maxLengthBetweenEqualCharacters(s = "abca"))