"""There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink."""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            res += newBottles
            numBottles = newBottles + numBottles % numExchange
        return res

print(Solution().numWaterBottles(numBottles = 9, numExchange = 3))
print('\n')
print(Solution().numWaterBottles(numBottles = 15, numExchange = 4))
print('\n')
print(Solution().numWaterBottles(numBottles = 5, numExchange = 5))
print('\n')
print(Solution().numWaterBottles(numBottles = 15, numExchange = 7))