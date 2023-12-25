"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [[1], [1,1]]
            
        for i in range(2, rowIndex+1): #need +1 because start at 0 idx
            row = [1] #first element in row
            for j in range(1, i): #columns
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            row.append(1) #last element in row
            ans.append(row)
       
        return ans[rowIndex]


        

print(Solution().getRow(rowIndex = 3))
print(Solution().getRow(rowIndex = 0))
print(Solution().getRow(rowIndex = 1))