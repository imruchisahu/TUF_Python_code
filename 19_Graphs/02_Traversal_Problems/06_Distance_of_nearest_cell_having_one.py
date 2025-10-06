'''
Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.



The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.


Examples:


Input: grid = [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]

Output: [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]

Explanation: 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1),(0,2), (0,2), (2,3), (1,0) and (1,1) respectively.



Input: grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]

Output: [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]

Explanation: 0's at (0,1), (1,2), (2,1) and (2,2) are at a distance of 1, 1, 1 and 2 from 1's at (0,0),(0,2), (2,0) and (1,1) respectively.

Input : grid = [ [0, 1], [1, 0] ]

Output:
[ [0, 1], [1, 0] ]
[ [1, 1], [1, 1] ]
[ [1, 0], [0, 1] ]
[ [0, 0], [0, 0] ]

Submit
Constraints:
  1 <= N, M <= 500
  grid[i][j] == 0 or 1
There is atleast one 1 in the grid

Intuition:
To find the nearest 1 in the grid for each cell, the breadth-first search algorithm will come in handy. BFS will take a step from cells containing 1 and will reach out to all zeros that are at a distance of one.

It can be said that the nearest 1 to the 0s is at a distance of one. Again if another step is taken, the next set of zeros will be found, and for these zeros, 1 is at a distance of two. Continuing the same, all the cells having 0 can be reached.

Why using BFS and not DFS?
BFS ensures that the first time we reach a cell, we do so via the shortest path. Checking neighbors and updating distances ensures we explore all possible paths systematically.

Approach:
Create two matrices: one for keeping track of visited cells and another for storing distances. Use a queue to facilitate the Breadth-First Search (BFS).
Traverse the entire grid. For each cell that contains a '1', mark it as visited, set its distance to 0, and add it to the queue with a step count of 0.
While the queue is not empty, repeat the following steps:
Get the front element, which provides the current cell coordinates and the number of steps taken to reach it. Update the distance matrix with the current step count for the current cell.
Check the four neighboring cells (up, down, left, right). For each neighbor, if it is within grid boundaries and has not been visited, mark it as visited, increment the step count by 1, and push the neighbor with the updated step count in the queue.
After the BFS traversal completes, the distance matrix will have the shortest distance to the nearest '1' for each cell in the grid. Return this matrix as the result.

from collections import deque

class Solution:
    # delRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
    # Helper Function to check if a 
    # the cell is within boundaries
    def isValid(self, i, j, n, m):
        # Return false if the cell is invalid
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        
        # Return true if the cell is valid
        return True
    
    # Function to find the distance of the 
    # nearest 1 in the grid for each cell.
    def nearest(self, grid):
        
        # Determine the dimensions
        n = len(grid)
        m = len(grid[0])
        
        # visited and distance matrix
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        
        # Queue to store the pair {coordinates, steps}
        q = deque()
        
        # Traverse the matrix
        for i in range(n):
            for j in range(m):
                
                # Start BFS if the cell contains 1
                if grid[i][j] == 1:
                    q.append(((i, j), 0))
                    vis[i][j] = 1
                else:
                    # mark unvisited 
                    vis[i][j] = 0
        
        # Traverse till the queue becomes empty
        while q:
            
            # Determine the top of the queue
            it = q.popleft()
            
            # Determine the coordinates of the cell
            row, col = it[0]
            
            # Get the steps
            steps = it[1]
            
            # Update the distance matrix
            dist[row][col] = steps
            
            # Traverse the 4 neighbors
            for i in range(4):
                
                # Coordinates of new cell
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]
                
                # Check for valid, unvisited cell
                if (self.isValid(nRow, nCol, n, m) and 
                    vis[nRow][nCol] == 0):
                    
                    # Mark the cell as visited
                    vis[nRow][nCol] = 1
                    q.append(((nRow, nCol), steps + 1))
        
        # return distance matrix
        return dist

if __name__ == "__main__":
    grid = [
        [0, 1, 1, 0], 
        [1, 1, 0, 0], 
        [0, 0, 1, 1]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the distance of the 
    # nearest 1 in the grid for each cell.
    ans = sol.nearest(grid)
    
    n = len(ans)
    m = len(ans[0])
    
    # Output
    print("The distance of the nearest 1 in the grid for each cell is: ")
    for i in range(n):
        for j in range(m):
            print(ans[i][j], end = " ")
        print()

Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of grid)
For the worst case, the BFS function will be called for (N x M) nodes, and for every node, we are traversing for 4 neighbors, so it will take O(N x M x 4) time.

Space Complexity: O(N*M) The visited array and distance matrix will take O(N*M) space each, and the queue will store at maximum of O(N*M) cells (in case of grid having all cells as 1).

'''
from collections import deque
class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    def isValid(self, i, j, n, m):
        # Return false if the cell is invalid
        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False
        return True
    
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                
                # Start BFS if the cell contains 1
                if grid[i][j] == 1:
                    q.append(((i, j), 0))
                    vis[i][j] = 1
                else:
                    # mark unvisited 
                    vis[i][j] = 0
        while q:
            it = q.popleft()
            row, col = it[0]
            steps = it[1]
            dist[row][col] = steps
            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                if (self.isValid(nRow, nCol, n, m) and 
                    vis[nRow][nCol] == 0):
                    
                    # Mark the cell as visited
                    vis[nRow][nCol] = 1
                    q.append(((nRow, nCol), steps + 1))
        return dist
  