"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."""

class Solution:
    def reverseVowels(self, s: str) -> str:
        b, e, vowels = 0, (len(s)-1), ['a','e','i','o','u','A','E','I','O','U']
        res = list(s)
        while(e > b):
            if res[b] in vowels and res[e] in vowels:
                res[b], res[e] = res[e], res[b]
                b += 1
                e -= 1
            elif res[b] in vowels and res[e] not in vowels:
                e -=1
            else:
                b +=1                  
        return ''.join(res)
    
print(Solution().reverseVowels(s = 'hello'))