'''
Given a boolean 2D matrix grid of size N x M. Find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be same if and only if one island is equal to another (not rotated or reflected).


Examples:
Input: grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]]

Output: 1

Explanation:





Same colored islands are equal. We have 2 equal islands, so we have only 1 distinct island.

Input: grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1],[1, 1, 0, 1, 1]]

Output: 3

Explanation:



Same colored islands are equal. We have 4 islands, but 2 of them are equal, So we have 3 distinct islands..

Input: grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 1, 1]]

Output:
2
1
3
4

Submit
Constraints:
  1 <= N, M <= 500
  grid[i][j] == 0 or 1

Intuition:
The goal is to count how many distinct shapes of islands exist in the grid. For that, it must be known how can to distinguish unique islands.

How to identify if two islands are unique or not?
A set data structure is known for storing only unique entries, which can also be used here to store unique islands here.
How to store the islands as an enty in set?
A island can be represented as the path taken to traverse all the land cells in the island. But the problem isn't solved yet. 

Here both the islands will be represented as two paths which look identical but consist of different coordinatees and thus will be treated as different entries for the set.

To solve this problem, the relative coordinates of all the cell with respect to a base cell (starting cell) can be stored as path as shown in the illustration:


Approach:
Use a set to store the unique shapes of islands. Use a 2D array to keep track of visited cells. Define directions for moving up, down, left, and right. Create a helper function to check if a cell is within the grid boundaries.
Traverse through the grid. If a cell contains a 1 and hasn't been visited, it indicates the start of a new island.
Use DFS to explore all cells of the island starting from the current cell. Track the relative positions of the cells in the island based on the starting cell. Mark cells as visited during the traversal to avoid revisiting them.
After exploring an island, store its shape (relative positions) in the set. The number of distinct islands is the size of the set containing the unique shapes.

from typing import List

class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]
  
    # Helper function to check if a 
    # cell is within boundaries
    def isValid(self, i, j, n, m):
        # Return false if cell is invalid
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        # Return true if cell is valid
        return True
    
    # Function for DFS traversal of island
    def dfs(self, row, col, grid, visited, 
            path, base_row, base_col):
        # Get the dimensions of grid
        n = len(grid)
        m = len(grid[0])
        
        # add relative position of current 
        # cell with respect to the base cell
        path.append((row-base_row, col-base_col))
        
        # Traverse the 4 neighbors
        for i in range(4):
            # Get coordinates of new cell
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            
            # Traverse unvisited, valid, land cell
            if (self.isValid(nRow, nCol, n, m) and 
                grid[nRow][nCol] == 1 and 
                not visited[nRow][nCol]):
                    
                # Mark the cell as visited
                visited[nRow][nCol] = True
                
                # Recursively call DFS for the new cell
                self.dfs(nRow, nCol, grid, visited, 
                         path, base_row, base_col)
        
        # Return after all neighbors are explored
        return
    
    # Function to count the count of
    # distinct islands in the given grid
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        
        # Get the dimensions of grid
        n = len(grid)
        m = len(grid[0])
        
        # 2-D Visited array
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        # Set to store traversal of unique islands
        st = set()
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                
                # Start BFS traversal if an 
                # unvisited land cell is found
                if grid[i][j] == 1 and not visited[i][j]:
                    
                    # Mark the cell as visited
                    visited[i][j] = True
                    
                    # To store the path of cells
                    path = []
                    
                    # Start DFS traversal from the cell
                    self.dfs(i, j, grid, visited, path, i, j)
                    
                    # Add the path of explored island to the set
                    st.add(tuple(path))
        
        return len(st)

# Example usage
grid = [
    [1, 1, 0, 1, 1], 
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

# Creating an instance of Solution class
sol = Solution()

# Function to count the count of distinct islands in the given grid
ans = sol.countDistinctIslands(grid)

# Output
print("The count of distinct islands in the given grid is:", ans)

Complexity Analysis:
Time Complexity: O(N*M*log(N*M)) (where N and M are dimensions of grid)
In the worst case, the DFS call will be made for N*M cells taking O(N*M) time.
In worst case, the set will store O(N*M) entries that takes O(N*M*log(N*M)) time.
Space Complexity: O(N*M)
The visited array takes O(N*M) space and the set will store a maximum of O(N*M) cells.
'''

from typing import List
class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]
    def isValid(self, i, j, n, m):
        # Return false if cell is invalid
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True
    def dfs(self, row, col, grid, visited, 
            path, base_row, base_col):
        n = len(grid)
        m = len(grid[0])
        path.append((row-base_row, col-base_col))
        for i in range(4):
            
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            if (self.isValid(nRow, nCol, n, m) and 
                grid[nRow][nCol] == 1 and 
                not visited[nRow][nCol]):
                visited[nRow][nCol] = True
                self.dfs(nRow, nCol, grid, visited, 
                         path, base_row, base_col)
        
        # Return after all neighbors are explored
        return
    def countDistinctIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        # 2-D Visited array
        visited = [[False for _ in range(m)] for _ in range(n)]
        st = set()
        for i in range(n):
            for j in range(m):
                
                # Start BFS traversal if an 
                # unvisited land cell is found
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    path = []
                    self.dfs(i, j, grid, visited, path, i, j)
                    st.add(tuple(path))
        
        return len(st)
