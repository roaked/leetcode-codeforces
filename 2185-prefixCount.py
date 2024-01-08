"""You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s."""

from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if pref == word[0:len(pref)]:
                ans+=1
        return ans
    
print(Solution().prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))
