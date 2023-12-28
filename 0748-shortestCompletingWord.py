"""Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, 
and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word
 the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
 Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. 
If there are multiple shortest completing words, return the first one that occurs in words."""

from typing import List
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        license_chars = [char.lower() for char in licensePlate if char.isalpha()]

        print(license_chars)
        license_count = Counter(license_chars)
        words.sort(key = len)

        for word in words:
            word_count = Counter(word)
            if all(word_count[char] >= license_count[char] for char in license_count):
                return word

print(Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))