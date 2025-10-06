'''
Given an N x M binary matrix grid, where 0 represents a sea cell and 1 represents a land cell. A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid. Find the number of land cells in the grid for which we cannot walk off the boundary of the grid in any number of moves.


Examples:


Input: grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

Output: 3

Explanation:



The highlighted cells represents the land cells.



Input: grid = [[0, 0, 0, 1],[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]

Output:3

Explanation:



The highlighted cells represents the land cells.

Input: grid = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

Output:
4
3
5
2

Submit
Constraints:
  1 <= N, M <= 500
  grid[i][j] == 0 or 1
  
  Intuition:
The problem requires finding land cells in a binary matrix that are completely surrounded by other land cells and cannot connect to the boundary of the grid by moving up, down, left, or right. The initial thought is that any land cell directly connected to the boundary or indirectly connected via other land cells should not be counted as an enclave. Therefore, a clever way to solve this involves identifying and marking all land cells that are reachable from the boundary. The remaining unmarked land cells will be the enclaves.

Approach:
Set up arrays to represent movements in four directions (up, right, down, left). Create a helper function to check if a given cell is within the grid boundaries.
Implement a BFS function to traverse the grid from a given starting cell, marking all connected land cells.
Use a queue to facilitate BFS traversal. Create a visited array to keep track of which cells have been processed.
Traverse the entire grid, and for each land cell on the boundary, mark it as visited and add it to the queue. Execute BFS from all boundary land cells. This will mark all land cells connected to the boundary, ensuring they are not counted as enclaves.
Traverse the grid again to count all unvisited land cells. These cells are enclaves since they are not connected to any boundary land cells. Return the total number of enclaves found.
from collections import deque

class Solution:
    def __init__(self):
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
    
    # Function to perform BFS traversal 
    def bfs(self, grid, q, vis):
        
        # Getting the dimensions of image
        n = len(grid)
        m = len(grid[0])
        
        # Until the queue is empty
        while q:
            # Get the cell from queue
            cell = q.popleft()
            
            # Get its coordinates
            row, col = cell
            
            # Traverse its 4 neighbors
            for i in range(4):
                
                # Coordinates of new cell
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]
                
                # check for valid, unvisited 
                # and land cells
                if (self.isValid(nRow, nCol, n, m) and 
                    grid[nRow][nCol] == 1 and 
                    vis[nRow][nCol] == False):
                    
                    # Mark the new cell as visited
                    # and add it to the queue
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))
    
    # Function to find number of enclaves 
    def numberOfEnclaves(self, grid):
        
        # Get the dimensions of grid
        n = len(grid)
        m = len(grid[0])
        
        # Queue for BFS traversal
        q = deque()
        
        # Visited array
        vis = [[False] * m for _ in range(n)]
        
        # Traverse the grid and add 
        # the border land cells to queue
        for i in range(n):
            for j in range(m):
                
                # If the land cell is at
                # border, add it to queue
                if ((i == 0 or i == n-1 or
                     j == 0 or j == m-1) and
                    grid[i][j] == 1):
                    
                    vis[i][j] = True
                    q.append((i, j))
       
        # Perform the bfs traversal 
        # from border land cells
        self.bfs(grid, q, vis)
        
        # Count to store number of enclaves
        count = 0
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                
                # If cell is a land cell and
                # unvisited, update the count
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1
        
        # Return count as answer
        return count

# Example usage
grid = [
    [0, 0, 0, 1], 
    [1, 0, 1, 0], 
    [0, 0, 1, 0], 
    [0, 0, 0, 0]
]

# Creating an instance of 
# Solution class
sol = Solution()

# Function call to get number of enclaves
ans = sol.numberOfEnclaves(grid)

print("The number of enclaves in given grid are:", ans)


Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of image)

In the worst case, all the cell will have land, and BFS call will be made for (N*M) nodes.
For every cell, its four neighbors are traversed, taking O(4*N*M) time.
Space Complexity: O(N*M)

Visited array takes O(N*M) space.
In worst scenario, the queue takes up O(N*M) space.

'''
from collections import deque

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True 
    def bfs(self, grid, q, vis):
        n = len(grid)
        m = len(grid[0])

        while q:
            cell = q.popleft()
            row, col = cell

            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]
                if (self.isValid(nRow, nCol, n, m) and 
                    grid[nRow][nCol] == 1 and 
                    vis[nRow][nCol] == False):
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))
    
    def numberOfEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if ((i == 0 or i == n-1 or
                     j == 0 or j == m-1) and
                    grid[i][j] == 1):
                    
                    vis[i][j] = True
                    q.append((i, j))
        self.bfs(grid, q, vis)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1
        return count