'''
Given a grid of size N x M (N is the number of rows and M is the number of columns in the grid) consisting of '0's (Water) and ‘1's(Land). Find the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.


Examples:

Input: grid = [ ["1", "1", "1", "0", "1"], ["1", "0", "0", "0", "0"], ["1", "1", "1", "0", "1"], ["0", "0", "0", "1", "1"] ]

Output: 2

Explanation: This grid contains 2 islands. Each '1' represents a piece of land, and the islands are formed by connecting adjacent lands horizontally or vertically. Despite some islands having a common edge, they are considered separate islands because there is no land connectivity in any of the eight directions between them. Therefore, the grid contains 2 islands.

Input: grid = [ ["1", "0", "0", "0", "1"], ["0", "1", "0", "1", "0"], ["0", "0", "1", "0", "0"], ["0", "1", "0", "1"," 0"] ]

Output: 1

Explanation: In the given grid, there's only one island as all the '1's are connected either horizontally, vertically, or diagonally, forming a single contiguous landmass surrounded by water on all sides.

Input: grid = [ ["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"] ]

Output:
1
2
4
3

Submit
Constraints:
·  N == grid.length

·  M == grid[i].length

·  1 <= N, M <= 300

·  grid[i][j] is '0' or '1'.

Intuition:
How to solve this problem using a graph?
Think of all the cells in the grid as nodes or vertices which are connected through each other via 8 edges.

How to traverse the neighbours efficiently?
The 8 neighbours of the current cell can be shown like this:


It is clear from the above image that:

row can be row-1, row, row+1. Or deltaRow varies from -1 to 1.
col can be col-1, col, col+1. Or deltaCol varies from -1 to 1.

Therefore, to effectively traverse all the neighbors, two loops can be used.
Approach:
Determine the dimensions of grid. Create a 2D visited array and initialize all values as false. Initialize a counter for the number of islands.
Loop through each cell in the grid. If the cell is land and not yet visited, it signifies the start of a new island.
Use BFS to explore all connected land cells starting from this cell and mark them visited.Increase the island count after completing the BFS for the current island.

from collections import deque

class Solution:
    # Function to determine if the cell is
    # valid (within grid's boundaries)
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        
        # Return true if cell is valid
        return True
    
    def bfs(self, i, j, vis, grid):
        # mark it visited
        vis[i][j] = True
        
        # Queue required for BFS traversal
        q = deque()
        
        # push the node in queue
        q.append((i, j))
        
        # Dimensions of grid
        n = len(grid)
        m = len(grid[0])
        
        # Until the queue becomes empty
        while q:
            # Get the cell from queue
            row, col = q.popleft()
            
            # Traverse the 8 neighbours
            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    # Coordinates of new cell
                    newRow = row + delRow
                    newCol = col + delCol
                    
                    # Check if the new cell is valid,
                    # unvisited, and a land cell
                    if (
                        self.isValid(newRow, newCol, n, m) and 
                        grid[newRow][newCol] == '1' and 
                        not vis[newRow][newCol]
                    ):
                        # Mark the node as visited
                        vis[newRow][newCol] = True
                        
                        # Push new cell in queue
                        q.append((newRow, newCol))
    
    # Function to find the number of islands in given grid
    def numIslands(self, grid):
        # Size of the grid
        n = len(grid)
        m = len(grid[0])
        
        # Visited array
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        # To store the count of islands
        count = 0
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                # If not visited and is a land, 
                # start a new traversal
                if not vis[i][j] and grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, vis, grid)
        
        return count

if __name__ == "__main__":
    grid = [
        ['1', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0'],
        ['1', '1', '1', '0', '1'],
        ['0', '0', '0', '1', '1']
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the number of islands in given grid
    ans = sol.numIslands(grid)
    
    print("The total islands in given grids are:", ans)
Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of the grid)
Running a nested loop to traverse every cell of grid takes O(N*M) time.
In total, the traversal will be performed on grids taking overall at most of O(9*N*M) time.
Space Complexity: O(N*M)

Because of the visited array, it takes up O(N*M) space and the queue space will also be O(N*M) at most.

'''
from collections import deque
class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    
    def bfs(self, i, j, vis, grid):
        vis[i][j] = True
        q = deque()
        q.append((i, j))
        n = len(grid)
        m = len(grid[0])
        while q:
            row, col = q.popleft()
            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    newRow = row + delRow
                    newCol = col + delCol
                    
                    # Check if the new cell is valid,
                    # unvisited, and a land cell
                    if (
                        self.isValid(newRow, newCol, n, m) and 
                        grid[newRow][newCol] == '1' and 
                        not vis[newRow][newCol]
                    ):
                        vis[newRow][newCol] = True
                        q.append((newRow, newCol))
    
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
    
        vis = [[False for _ in range(m)] for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, vis, grid)
        
        return count
       