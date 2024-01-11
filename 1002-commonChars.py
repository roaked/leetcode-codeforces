"""Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates).
 You may return the answer in any order."""

from typing import List
from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for char in words[0]:
            cnt[char] += 1

        for i in range(1, len(words)):
            word = words[i]
            char_cnt = defaultdict(int)
            for char in word:
                char_cnt[char] += 1
            for char in cnt:
                cnt[char] = min(cnt[char], char_cnt[char])

        ans =[]
        for char, char_cnt in cnt.items():
            if char_cnt != 0:
                for i in range(char_cnt):
                    ans.append(char)


        return ans
    
print(Solution().commonChars(words = ["cool","lock","cook"]))