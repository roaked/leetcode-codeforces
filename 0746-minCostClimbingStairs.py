"""You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor."""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        price_first = cost[0]
        price_second = cost[1]
        
        for i in range(2, len(cost)):
            current_price = cost[i] + min(price_first, price_second)
            price_first, price_second = price_second, current_price
            
        return min(price_first, price_second)

print(Solution().minCostClimbingStairs(cost = [10,15,20]))
print(Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))