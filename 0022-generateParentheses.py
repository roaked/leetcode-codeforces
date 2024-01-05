"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
               
        def backtrack(ans, s, left, right):
            if left==0 and right==0:
                ans.append(s)               
            if left>0:
                backtrack(ans, s+'(', left-1, right)              
            if right>0 and left<right:
                backtrack(ans, s+')', left, right-1)
        
        ans = []
        backtrack(ans, '', n, n)    
        return ans
    
print(Solution().generateParenthesis(n = 3))