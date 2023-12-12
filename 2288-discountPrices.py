
"""
A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. 
A word represents a price if it is a sequence of digits preceded by a dollar sign.

For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
You are given a string sentence representing a sentence and an integer discount.
For each word representing a price, apply a discount of discount% on the price and update the word in the sentence.
All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.
Note that all prices will contain at most 10 digits.
"""

class Solution(object):
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split() # words in a list
        discounted_value = 1- (discount / 100) # discounted value
        print(words)

        for i, word in enumerate(words):
            if word.startswith("$") and word[1:].isdigit():
                num = int(word[1:]) * discounted_value
                words[i] = "$" + "{:.2f}".format(num) # $ + .2float decimals 

        return " ".join(words)   
    
sentence = "there are $1 $2 and 5$ candies in the shop"
discount = 50
print(Solution().discountPrices(sentence, discount))

sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
discount = 100
print(Solution().discountPrices(sentence, discount))
