'''
Create a program that fills in the blank cells in a Sudoku puzzle to solve it.



Every sudoku solution needs to follow to these guidelines:



1) In every row, the numbers 1 through 9 must appear exactly once.

2) In every column, the numbers 1 through 9 must appear exactly once.

3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.



Empty cells are indicated by the '.' character.


Examples:
Input : board = [ ["5", "3", ".", ".", "7", ".", ".", ".", "."] ,
 ["6", ".", ".", "1", "9", "5", ".", ".", "."] , 
 [".", "9", "8", ".", ".", ".", ".", "6", "."] , 
 ["8", ".", ".", ".", "6", ".", ".", ".", "3"] , 
 ["4", ".", ".", "8", ".", "3", ".", ".", "1"] , 
 ["7", ".", ".", ".", "2", ".", ".", ".", "6"] , 
 [".", "6", ".", ".", ".", ".", "2", "8", "."] , 
 [".", ".", ".", "4", "1", "9", ".", ".", "5"] , 
 [".", ".", ".", ".", "8", ".", ".", "7", "9"] ]







Output : [["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]







Explanation : The Input and Output boards are shown above.

Input : board = [ [ ".", ".", ".", ".", ".", ".", "7", ".", ".", ], 
[ "7", ".", "5", ".", ".", ".", "9", ".", ".", ], 
[ ".", ".", ".", "9", "7", "5", "4", "3", "1", ],
 [ "9", ".", ".", ".", "4", "1", ".", ".", "7", ], 
 [ ".", "5", ".", "8", ".", "7", "6", "4", ".", ], 
 [ ".", "7", ".", ".", "2", ".", ".", ".", ".", ], 
 [ ".", "4", ".", ".", ".", ".", ".", "6", "9", ], 
 [ "1", "6", ".", "4", "3", ".", ".", ".", ".", ], 
 [ ".", ".", ".", ".", "6", "2", "3", ".", "4", ] ]


Output : [ [ "4", "1", "9", "3", "8", "6", "7", "5", "2", ], 
[ "7", "3", "5", "2", "1", "4", "9", "8", "6", ], 
[ "8", "2", "6", "9", "7", "5", "4", "3", "1", ], 
[ "9", "8", "3", "6", "4", "1", "5", "2", "7", ],
 [ "2", "5", "1", "8", "9", "7", "6", "4", "3", ], 
[ "6", "7", "4", "5", "2", "3", "1", "9", "8", ], 
[ "3", "4", "7", "1", "5", "8", "2", "6", "9", ], 
[ "1", "6", "2", "4", "3", "9", "8", "7", "5", ], 
[ "5", "9", "8", "7", "6", "2", "3", "1", "4", ] ]

Explanation : The Input and output board are shown above.

Constraints:
board.length = 9
board[i].length = 9
board[i][j] is a digit or '.'
It is guaranteed that input board has only one solution.

Solving Sudoku with Recursion
To solve a Sudoku puzzle in real life, imagine the task as filling in a partially completed grid so that every row, column, and 3x3 sub-box contains the digits from 1 to 9 exactly once. This involves trial and error, checking for conflicts with existing digits, and backtracking when a conflict arises. Think of it as trying to fit pieces into a jigsaw puzzle, where each piece (digit) must fit perfectly without violating any rules.

Intuition
Solving this question can be likened to fitting pieces into a jigsaw puzzle where each piece must fit perfectly without violating any rules. In real life, this means filling in the partially completed grid so that every row, column, and 3x3 sub-box contains the digits from 1 to 9 exactly once. This is done through trial and error: identifying empty cells, attempting to place digits, and checking for conflicts. When a conflict arises, backtrack and try a different digit. This process is naturally recursive, as solving the grid involves solving smaller sub-problems (filling in each cell) that depend on previous placements. By treating each empty cell as a sub-problem and recursively attempting to solve the entire grid, the puzzle can be systematically and efficiently solved.

Approach
Traverse the grid to find the first empty cell. For the empty cell, try placing digits from '1' to '9' one by one.
For each digit, check if it is valid according to Sudoku rules (i.e., it doesn't conflict with any digit in the same row, column, or 3x3 sub-box). If a digit is valid, place it in the cell.
Recursively attempt to solve the rest of the grid with the current digit placed. If placing the current digit doesn't lead to a solution, reset the cell and try the next digit.
Repeat the process until the entire grid is correctly filled, or determine that the puzzle is unsolvable.

class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    # Recursive method to solve the Sudoku
    def solve(self, board):
        # Size of the board
        n = 9  
        for i in range(n):
            for j in range(n):
                # Empty cell found
                if board[i][j] == '.':  
                    for digit in '123456789':
                        # Check if digit can be placed
                        if self.are_rules_met(board, i, j, digit):  
                             # Place digit
                            board[i][j] = digit 
                            # Recur to place next digits
                            if self.solve(board):  
                                return True
                            else:
                                # Reset if placing digit doesn't solve Sudoku
                                board[i][j] = '.'
                    # If no digit can be placed, return False              
                    return False  
        # Sudoku solved            
        return True  

    # Method to check if placing a digit follows Sudoku rules
    def are_rules_met(self, board, row, col, digit):
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit:
                # Digit already in row or column
                return False  
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == digit:
                     # Digit already in 3x3 sub-box
                    return False 
         # Digit can be placed            
        return True 


if __name__ == "__main__":
    solution = Solution()
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    solution.solveSudoku(board)
    for row in board:
        print(" ".join(row))
Complexity Analysis
Time Complexity: O(9E), where E (<= 81) is the number of empty cells.
As each empty cell can be filled with 1 to 9 digits.

Space Complexity: O(E), because of the recursive stack space.
'''
class Solution:
    def solveSudoku(self, board):
        self.solve(board)
    def solve(self, board):
        n = 9  
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':  
                    for digit in '123456789':
                        if self.are_rules_met(board, i, j, digit):  
                            board[i][j] = digit 
                            # Recur to place next digits
                            if self.solve(board):  
                                return True
                            else:
                                board[i][j] = '.'              
                    return False             
        return True  

    def are_rules_met(self, board, row, col, digit):
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit:
                return False  
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == digit:
                    return False            
        return True 
