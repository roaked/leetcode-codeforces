"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

from operations import isValidSudoku

class Solution:

    def emptyLocation(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return -1, -1

    def solveSudoku(self, board):
        row, col = self.emptyLocation(board)
        
        if row == -1 and col == -1:
            return True
        
        for num in range(1, 10):
            next_num = str(num)
            board[row][col] = next_num
            if isValidSudoku(self, board) and self.solveSudoku(board):
                return True
            board[row][col] = '.'
        
        return False
    

################################################################

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Solution().solveSudoku(board)
for row in board:
    print(row)
