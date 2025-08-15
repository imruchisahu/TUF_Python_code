'''
The challenge of arranging n queens on a n × n chessboard so that no two queens attack one another is known as the "n-queens puzzle."



Return every unique solution to the n-queens puzzle given an integer n. The answer can be returned in any sequence.



Every solution has a unique board arrangement for the placement of the n-queens, where 'Q' and '.' stand for a queen and an empty space, respectively.


Examples:
Input : n = 4

Output : [[".Q.." , "...Q" , "Q..." , "..Q."] , ["..Q." , "Q..." , "...Q" , ".Q.."]]

Explanation : There are two possible combinations as shown below.





Input : n = 2

Output : [ [] ]

Explanation : There is no possible combination for placing two queens on a board of size 2*2.

Input : n = 1

Output:
[["Q"]]
Constraints:
1 <= n <= 9

Real-Life Solution
Imagine arranging a group of people in a hall where each person must have their own private space without being disturbed. Each person represents a queen and the hall represents the chessboard. The goal is to position each person such that no two people can see each other directly either in the same row, the same column, or along any diagonal. The task is to ensure that all individuals are placed in a way that respects these constraints, creating a harmonious arrangement.

Intuitive Recursion Process
The recursive process mimics placing each individual (queen) in a valid position (row) for a given column and then proceeding to place the next individual in the next column. Visualize this as a step-by-step arrangement where each step involves checking if a specific spot is free from conflicts. Start with an empty board and place the first queen in the first row of the first column. Move to the next column and try placing a queen in each row, one by one. If a spot is found where the queen can be placed without attacking others, move to the next column and repeat the process. If no safe spot is found in the current column, remove the last placed queen (backtrack) and try the next possible position for the previous queen. Continue this pattern of placing and removing queens until all columns have a queen or all possible configurations have been explored. This step-by-step placement ensures every possible arrangement is considered, and only valid solutions are kept.

Approach
Initialize an empty board of size n x n with all positions set to empty ('.').
Start with the first column (col = 0).
For the current column, try placing a queen in each row:
Check if the current position (row, col) is safe by ensuring no queens are in the same row, column, or diagonal.
If the position is safe, place a queen ('Q') at (row, col).
Recursively attempt to place queens in the next column (col + 1).
If placing the queen in the next column is successful, the solution is found.
If no valid position is found for the next column, backtrack: remove the queen from (row, col) and try the next row in the current column.
If all columns are filled, add the current board configuration to the list of solutions.
Repeat the process until all possibilities are explored.
Return the list of all valid board configurations.

class Solution:
    # Check if it's safe to place a queen at board[row][col]
    def safe(self, board, row, col):
        r, c = row, col
        
        # Check upper left diagonal
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Reset to the original position
        r, c = row, col
        
        # Check left side
        while c >= 0:
            if board[r][c] == 'Q':
                return False
            c -= 1

        # Reset to the original position
        r, c = row, col
        
        # Check lower left diagonal
        while r < len(board) and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        # If no queens are found, it's safe
        return True

    # Function to place queens on the board
    def func(self, col, ans, board):
        # If all columns are filled, add the solution to the answer
        if col == len(board):
            ans.append(list(board))
            return

        # Try placing a queen in each row for the current column
        for row in range(len(board)):
            # Check if it's safe to place a queen
            if self.safe(board, row, col):
                # Place the queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                
                # Recursively place queens in the next columns
                self.func(col + 1, ans, board)
                
                # Remove the queen and backtrack
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    # Solve the N-Queens problem
    def solveNQueens(self, n):
        # List to store the solutions
        ans = []
        # Initialize the board with empty cells
        board = ["." * n for _ in range(n)]

        # Start placing queens from the first column
        self.func(0, ans, board)
        return ans

# Main method to test the solution
if __name__ == "__main__":
    solution = Solution()
    n = 4 # Example with 4 queens
    solutions = solution.solveNQueens(n)

    # Print all solutions
    for sol in solutions:
        for row in sol:
            print(row)
        print()
Complexity Analysis
Time Complexity : The time complexity is O(N!), where N is the number of queens, due to the recursive search through potential placements and backtracking.

Space Complexity : The space complexity is O(N), for the recursion stack and the storage of the solutions.
'''
class Solution:
    def safe(self, board, row, col):
        r, c = row, col
        # Check upper left diagonal
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Reset to the original position
        r, c = row, col
        
        # Check left side
        while c >= 0:
            if board[r][c] == 'Q':
                return False
            c -= 1
        r, c = row, col
        
        # Check lower left diagonal
        while r < len(board) and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1
        return True

    # Function to place queens on the board
    def func(self, col, ans, board):
        if col == len(board):
            ans.append(list(board))
            return
        for row in range(len(board)):
            if self.safe(board, row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.func(col + 1, ans, board)
            
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]
        self.func(0, ans, board)
        return ans
