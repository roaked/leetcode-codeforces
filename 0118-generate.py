"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1], [1,1]]

        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return ans
        
        for i in range(2, numRows): 
            row = [1] #first element in row
            for j in range(1, i): #columns
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            row.append(1) #last element in row
            ans.append(row)
        return ans

print(Solution().generate(numRows = 5))
print(Solution().generate(numRows = 1))