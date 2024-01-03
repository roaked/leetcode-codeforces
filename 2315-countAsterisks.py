"""You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, 
the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair."""


class Solution:
    def countAsterisks(self, s: str) -> int:
        s, cnt = s.split(sep = '|'), 0
        if(len(s)) % 2 == 0:
            s.remove[0]

        for word in s[0::2]:
            l = 0
            while(l < len(word)):
                if (word[l]) == '*':
                    cnt += 1
                l += 1
        return cnt

print(Solution().countAsterisks(s = "l|*e*et|c**o|*de|"))
print(Solution().countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l"))