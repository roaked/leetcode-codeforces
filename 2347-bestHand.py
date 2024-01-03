"""You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive."""

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        ranks.sort()
        
        max_count = 1
        current_count = 1

        for i in range(1, len(ranks)):
            if ranks[i] == ranks[i - 1]:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            else:
                current_count = 1

        unique = set(suits)
        if len(unique) == 1: 
            return "Flush"
        
        elif max_count >= 3: 
            return "Three of a Kind"
        
        elif max_count == 2:
            return "Pair"

        else: 
            return  "High Card" #worst case
    
print(Solution().bestHand(ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]))

print(Solution().bestHand(ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]))

print(Solution().bestHand(ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]))
