"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram. """

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic stack
        max_area = 0
        index = 0
        
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
        
        while stack:
            top = stack.pop()
            width = index if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
        
        return max_area
    
print(Solution().largestRectangleArea(heights = [2,1,5,6,2,3]))