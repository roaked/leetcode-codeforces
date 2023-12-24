"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack."""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    return i
                    
        return -1

print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
print(Solution().strStr(haystack = "leetcode", needle = "leeto"))
print(Solution().strStr(haystack = "hello", needle = "ll"))
print(Solution().strStr(haystack = "mississippi", needle = "issip"))
