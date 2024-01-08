"""You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character 
where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right]"""

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = 0

        for word in range(left, right+1):
            if words[word][0] in ['a', 'e', 'i', 'o', 'u'] and words[word][-1] in ['a', 'e', 'i', 'o', 'u']:
                ans+=1
        return ans
    
print(Solution().vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))