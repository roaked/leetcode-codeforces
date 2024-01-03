"""There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations."""

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        ans = 0
        for i in range(len(operations)):
            if operations[i] == 'X++' or operations[i] == '++X':
                ans += 1
            else: 
                ans -= 1
        return ans
    
    def finalValueAfterOperationsV2(self, operations: list[str]) -> int:

        A = operations.count("++X") 
        B = operations.count("X++")
	
        return A+B-(len(operations)-A-B)
    
print(Solution().finalValueAfterOperations(operations = ["--X","X++","X++"]))
print(Solution().finalValueAfterOperationsV2(operations = ["--X","X++","X++"]))