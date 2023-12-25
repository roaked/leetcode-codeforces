"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

from itertools import product
from 0036-isValidSudoku import isValidSudoku


class Solution:

    def emptyLocation(self, board: list[list[int]]):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return -1, -1

    def solveSudoku(self, board: list[list[int]]):
        row, col = emptyLocation(board)
        
        if row == -1 and col == -1:
            return True
        
        for num in range(1, 10):
            if isValidSudoku(board):
                board[row][col] = num
                if solveSudoku(board):
                    return True
                board[row][col] = 0
        
        return False

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(Solution().solveSudoku(board))