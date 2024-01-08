"""A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of 
neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops."""

from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        print(sum(distance[start:destination]))
        return min(sum(distance[start:destination]), sum(distance[destination:]) + sum(distance[:start])) if destination > start else \
            min(sum(distance[destination:start]), sum(distance[:destination]) + sum(distance[start:]))

print(Solution().distanceBetweenBusStops(distance = [7,10,1,12,11,14,5,0], start = 7, destination = 2))
print(Solution().distanceBetweenBusStops(distance = [7,10,1,12,11,14,5,0], start = 2, destination = 7))