"""Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.   """

from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool: 
        return ''.join(word2) == ''.join(word1)   

print(Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))