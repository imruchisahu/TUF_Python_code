'''
Given a grid of n x m dimension grid of characters board and a string word.The word can be created by assembling the letters of successively surrounding cells, whether they are next to each other vertically or horizontally. It is forbidden to use the same letter cell more than once.

Return true if the word exists in the grid otherwise false.


Examples:
Input : board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , word = "ABCCED"

Output : true

Explanation : The word is coloured in yellow.





Input : board = [["A", "B", "C", "E"] , ["S", "F", "C", "S"] , ["A", "D", "E", "E"]] , word = "SEE"

Output : true

Explanation : The word is coloured in yellow.





Input : board = [["A", "B", "C", "E"] , ["S", "F", "C", "S"] , ["A", "D", "E", "E"]] , word = "ABCB"

Output:
false
Constraints:
n = board.length
m = board[i].length
1 <= n, m <=6
1 <= word.length <= 15
board and word consist of only lowercase and uppercase English letters.

Real Life Intuition
To solve this problem in real life, imagine being in a grid-like garden where each cell contains a different flower with a letter on it. The goal is to trace a path through adjacent flowers to spell out a given word. Starting from each flower that matches the first letter of the word, inspect neighboring flowers in all four directions (up, down, left, right). Temporarily mark each flower as visited to avoid revisiting it, and backtrack if the current path does not lead to the complete word, restoring the garden's state for subsequent attempts. This process continues until the word is found or all possibilities are exhausted.

Recursive Process Intuition
The recursive process mimics this real-life approach. Begin at any cell matching the first letter of the word. Recursively explore adjacent cells for the next letter. Temporarily mark cells as visited to avoid repetition. If a path spells out the word, return true. If not, go back by unmarking the cell and continue exploring other paths. This continues until all possible paths from each starting cell are checked.

Approach
Start by iterating through each cell in the grid.
For each cell, check if it matches the first character of the word. f it matches, invoke a helper function to explore all possible paths from this cell.
In the helper function, perform the following checks:
Check if the current index matches the length of the word, indicating the word is found.
Check boundary conditions and character mismatch to prevent invalid accesses.
If the character matches, mark the current cell as visited by temporarily changing its value. Recursively explore all four directions (up, down, left, right) from the current cell for the next character in the word. If any recursive call returns true, propagate this result up the call stack.
After exploring all directions, restore the current cell's original value to allow other paths to use it. Continue this process until all cells and paths are exhausted.
Return true if any path successfully spells out the word; otherwise, return false.


class Solution:
    # Helper function to check if the word exists starting from cell (i, j)
    def func(self, board, i, j, word, k):
        # If all characters of the word are found
        if k == len(word):
            return True
        # Boundary conditions and character mismatch check
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
            return False

        # Temporarily mark the cell as visited
        temp = board[i][j]
        board[i][j] = ' '

        # Check all four possible directions (down, up, right, left)
        ans = (self.func(board, i + 1, j, word, k + 1) or
               self.func(board, i - 1, j, word, k + 1) or
               self.func(board, i, j + 1, word, k + 1) or
               self.func(board, i, j - 1, word, k + 1))

        # Restore the original character in the cell
        board[i][j] = temp
        
        return ans

    # Main function to check if the word exists in the board
    def exist(self, board, word):
        # Iterate through each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If the first character matches, start the search
                if board[i][j] == word[0]:
                    # If the word is found, return true
                    if self.func(board, i, j, word, 0):
                        return True
        # If the word is not found, return False
        return False

# Main function to test the solution
solution = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"

if solution.exist(board, word):
    print("Word found!")
else:
    print("Word not found!")
Complexity Analysis
Time Complexity : O(N * M * 4^L) where N is rows, M is columns and L is the word length; recursive search through board.

Space Complexity : O(L) due to recursive call stack depth, where L is the length of the word.

'''
class Solution:
    def func(self, board, i, j, word, k):
        if k == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = ' '
        ans = (self.func(board, i + 1, j, word, k + 1) or
               self.func(board, i - 1, j, word, k + 1) or
               self.func(board, i, j + 1, word, k + 1) or
               self.func(board, i, j - 1, word, k + 1))
        board[i][j] = temp
        
        return ans
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.func(board, i, j, word, 0):
                        return True
        return False