"""A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence."""

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for words in sentences:
            cnt = 1
            for i in range(len(words)):
                if words[i] == " ":
                    cnt += 1
                ans = max(ans, cnt)
        return ans

print(Solution().mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print('\n')
print(Solution().mostWordsFound(sentences = ["please wait", "continue to fight", "continue to win"]))