"""Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings 
(i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring."""


class Solution:
    def maxScore(self, s: str) -> int:
        results, ones, zeros = 0,0, s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0': 
                zeros +=1
            elif s[i] == '1':
                ones -=1

            results = max(results, zeros+ones)

        return results
     
print(Solution().maxScore(s = "011101"))
print('\n')
print(Solution().maxScore(s = "00111"))
print('\n')
print(Solution().maxScore(s = "1111"))
print('\n')