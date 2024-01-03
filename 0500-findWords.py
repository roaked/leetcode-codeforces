"""Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard   
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm"."""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        sol = []
        rows = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]
        
        for word in words:
            word_set = set(word.lower())  
            for row in rows:
                if word_set.issubset(row): 
                    sol.append(word)        
        return sol

words = ["Hello","Alaska","Dad","Peace"]
print(Solution().findWords(words))
print("\n")

words = ["omk"]
print(Solution().findWords(words))
print("\n")

words = ["adsdf","sfd"]
print(Solution().findWords(words))
print("\n")

words = ["ads1321df","sfd"]
print(Solution().findWords(words))
print("\n")