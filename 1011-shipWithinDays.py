"""A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages
 on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days."""


from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        day, ans, res = sum(weights) / days, [], []
        for i in range(len(weights)):
            p, cnt = i, 0
            if i < p:
                continue
            while(cnt <= day and p < len(weights)):
                cnt += weights[p]
                res.append(weights[p])
                p += 1
        return res
    
print(Solution().shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(Solution().shipWithinDays(weights = [3,2,2,4,1,4], days = 3))