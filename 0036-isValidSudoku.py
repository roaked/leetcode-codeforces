"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

C1 - Each row must contain the digits 1-9 without repetition.
C2 - Each column must contain the digits 1-9 without repetition.
C3 - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""

class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def valid(arr):
            s=''.join(arr).replace('.','')
            return len(s) == len(set(s))
        
        def checkrow(): #C1
            for row in board:
                if not valid(row):
                    return False
            return True
        
        def checkcol(): #C2
            for col in zip(*board):
                if not valid(col):
                    return False
            return True
        
        def square(): #C3
            for r in range(0,9,3):
                for c in range(0,9,3):
                    nums=[board[r+i][c+j] for i in range(3) for j in range(3)]
                    if not valid(nums):
                        return False
            return True
        
        return checkrow() and checkcol() and square()
    
print(Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print('\n')

    
print(Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
