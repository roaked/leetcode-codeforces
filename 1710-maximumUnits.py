"""You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, w
here boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck."""

from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0
        for boxes, units_per_box in boxTypes:
            boxes_to_take = min(boxes, truckSize)
            total_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
            if truckSize == 0:
                break 

        return total_units

print(Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
print(Solution().maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))