'''
You are given a matrix mat of size N x M where each cell contains either 'O' or 'X'.

Your task is to replace all 'O' cells that are completely surrounded by 'X' with 'X'.



Rules:

An 'O' (or a group of connected 'O's) is considered surrounded if it is not connected to any border of the matrix.
Two 'O' cells are considered connected if they are adjacent horizontally or vertically (not diagonally).
A region of connected 'O's that touches the border (i.e., first row, last row, first column, or last column) is not surrounded and should not be changed.

Examples:


Input: mat = [ ["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"] ]

Output: [ ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"] ]

Explanation:



The 'O' cells at positions (1,1), (1,2), (2,2), and (3,1) are surrounded by 'X' cells in all directions (horizontally and vertically).

However, the 'O' region at (3,1) is adjacent to an edge of the board, so it cannot be completely surrounded by 'X' cells. Therefore, it remains unchanged.

Input: mat = [ ["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"] ]

Output: [ ["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"] ]

Explanation: The only 'O' cell at position (1,1) is completely surrounded by 'X' cells in all directions (horizontally and vertically). Hence, it is replaced with 'X' in the output.

Input: mat = [ ["X", "X", "X", "O"], ["X", "X", "X", "X"], ["O", "X", "X", "X"], ["X", "X", "X", "X"] ]

Output:
[ ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['O', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'] ]
[ ['X', 'X', 'X', 'O'], ['X', 'X', 'X', 'X'], ['O', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'] ]
[ ['X', 'X', 'X', 'O'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'] ]
[ ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'] ]

Submit
Constraints:
  N == mat.length
  M == mat[i].length
  1 <= N, M <= 300
  mat[i][j] is 'X' or 'O'.

Intuition:
An important thing to note is that the boundary elements in the matrix cannot be replaced with 'X' as they are not surrounded by 'X' from all 4 directions. This means if 'O' (or a set of 'O') is connected to a boundary 'O' then it can't be replaced with 'X'.

Thus, to solve this problem efficiently, traversal can be started from the boundary 'O's. All the 'O's encountered during traversal will not be surrounded by 'X's in all 4 directions which can be marked as visited.

Once all the traversals are completed, the 'O's that are not marked as visited in the matrix will represent the 'O's that are completely surrounded by 'X's. For the particular problem, either of the traversal techniques can be used.

Approach:
Initialize two lists to help navigate through the four possible directions (up, right, down, left). Define a function to check if a cell is within the matrix boundaries.
Implement a recursive function for DFS traversal of connected 'O' cells. Mark the current cell as visited. Explore the four possible neighboring cells. If a neighboring cell contains 'O' and is not visited, recursively apply the traversal function on it.
For the main driver function, traverse the boundaries to find unvisited 'O' cells and start the DFS traversal from those cells. Mark each cell as visited during the traversal.
After processing boundary cells, traverse the entire matrix and convert all unvisited 'O' cells to 'X' as they are surrounded by 'X'.

class Solution:
    def __init__(self):
        # DelRow and delCol for neighbors
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    # Helper Function to check if a 
    # cell is within boundaries
    def isValid(self, i, j, n, m):
        
        # Return false if cell is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
            
        # Return true if cell is valid
        return True
    
    # Recursive function to perform DFS
    def dfs(self, row, col, vis, mat, n, m):
        # Mark the node as visited
        vis[row][col] = True
        
        # Check the 4 neighbors
        for i in range(4):
            # Determine coordinates of new cell
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            
            # If an unvisited, valid cell contains 'O'
            if (self.isValid(nRow, nCol, n, m) and 
                mat[nRow][nCol] == 'O' and 
                not vis[nRow][nCol]):
                    
                # Recursive DFS traversal
                self.dfs(nRow, nCol, vis, mat, n, m)
    
    # Function to replace surrounded 'O's with 'X's
    def fill(self, mat):
        # Determine the dimensions of matrix
        n = len(mat)
        m = len(mat[0])
        
        # Visited array
        vis = [[False] * m for _ in range(n)]
        
        # Traverse the boundaries
        
        # Traversal for boundary rows
        for j in range(m):
            # Check for unvisited 'O's in boundary rows
            
            # First row
            if not vis[0][j] and mat[0][j] == 'O':
                # Start DFS traversal from current node
                self.dfs(0, j, vis, mat, n, m)
            
            # Last row
            if not vis[n - 1][j] and mat[n - 1][j] == 'O':
                # Start DFS traversal from current node
                self.dfs(n - 1, j, vis, mat, n, m)
        
        # Traversal for boundary columns
        for i in range(n):
            # Check for unvisited 'O's in boundary columns
            
            # First column
            if not vis[i][0] and mat[i][0] == 'O':
                # Start DFS traversal from current node
                self.dfs(i, 0, vis, mat, n, m)
            
            # Last column
            if not vis[i][m - 1] and mat[i][m - 1] == 'O':
                # Start DFS traversal from current node
                self.dfs(i, m - 1, vis, mat, n, m)
        
        # Traverse the matrix and convert 
        # the unvisited 'O's into 'X'
        for i in range(n):
            for j in range(m):
                # Check for unvisited 'O's
                if (mat[i][j] == 'O' and 
                    not vis[i][j]):
                        
                    mat[i][j] = 'X'
        
        # Return the updated matrix
        return mat

# Creating an instance of Solution class
sol = Solution()

# Input matrix
mat = [
    ['X', 'X', 'X', 'X'], 
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

# Function call to replace surrounded 'O's with 'X's
ans = sol.fill(mat)

# Output
print("The updated matrix is:")
for row in ans:
    print(" ".join(row))

Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of matrix)

In the worst case, when all the elements in the matrix will be 'O', DFS call will be made for O(N*M) cells, and for each cell traversing its 4 neighbors will contribute to O(4*N*M) time.
Traversal of boundary (rows and columns) takes O(N+M) time.
Traversal of matrix to update the unvisited 'O' takes O(N*M) time.
Hence, O(4*N*M) + O(N+M) + O(N*M) contribute to overall O(N*M) time.
Space Complexity: O(N*M)
O(N*M) for visited array, and O(N*M) as recursive stack space for DFS traversal in worst case.

'''
class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    def isValid(self, i, j, n, m):
        
        # Return false if cell is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    
    # Recursive function to perform DFS
    def dfs(self, row, col, vis, mat, n, m):
        vis[row][col] = True
        for i in range(4):
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            
            # If an unvisited, valid cell contains 'O'
            if (self.isValid(nRow, nCol, n, m) and 
                mat[nRow][nCol] == 'O' and 
                not vis[nRow][nCol]):
                self.dfs(nRow, nCol, vis, mat, n, m)
    
    # Function to replace surrounded 'O's with 'X's
    def fill(self, mat):
        n = len(mat)
        m = len(mat[0])
        vis = [[False] * m for _ in range(n)]
        for j in range(m):
            # Check for unvisited 'O's in boundary rows
            
            # First row
            if not vis[0][j] and mat[0][j] == 'O':
                # Start DFS traversal from current node
                self.dfs(0, j, vis, mat, n, m)
            
            # Last row
            if not vis[n - 1][j] and mat[n - 1][j] == 'O':
                # Start DFS traversal from current node
                self.dfs(n - 1, j, vis, mat, n, m)
        for i in range(n):
            # First column
            if not vis[i][0] and mat[i][0] == 'O':
                # Start DFS traversal from current node
                self.dfs(i, 0, vis, mat, n, m)
            
            # Last column
            if not vis[i][m - 1] and mat[i][m - 1] == 'O':
                self.dfs(i, m - 1, vis, mat, n, m)
        
        # Traverse the matrix and convert 
        # the unvisited 'O's into 'X'
        for i in range(n):
            for j in range(m):
                # Check for unvisited 'O's
                if (mat[i][j] == 'O' and 
                    not vis[i][j]):
                    mat[i][j] = 'X'
        return mat