"""Given a string s, reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order."""


class Solution:
    def reverseWords(self, s: str) -> str:
        newS, reversed_words = s.split(), []
        for word in newS:
            l, r = 0, len(word)-1
            word_list = list(word)
            while(l <= r):
                word_list[l], word_list[r] = word_list[r], word_list[l]
                r -= 1
                l += 1
            reversed_words.append(''.join(word_list))
        return ' '.join(reversed_words) 
    

print(Solution().reverseWords(s = "Let's take LeetCode contest"))