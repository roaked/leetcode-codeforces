"""A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or 
equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3,
 they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies."""

from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans, skip = 0, 0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            skip += 1
            if skip == 3:
                skip = 0
                continue
            ans += cost[i]
        return ans

print(Solution().minimumCost(cost = [1,2,3]))
print(Solution().minimumCost(cost = [6,5,7,9,2,2]))