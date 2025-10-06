'''
Given an n x m grid, where each cell has the following values : 



2 - represents a rotten orange

1 - represents a Fresh orange

0 - represents an Empty Cell

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten. 



Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.


Examples:
Input: grid = [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]

Output: -1

Explanation: Orange at (3,0) cannot be rotten.





Input: grid = [ [2,1,1] , [1,1,0] , [0,1,1] ] 

Output: 4

Explanation:



Input: grid = [[0,1,2],[0,1,2],[2,1,1]]

Output:
0
2
1
3

Submit
Constraints:
  1 <= n, m <= 500
  grid[i][j] == 0 or 1 or 2
  
  Intuition:
The idea is that for each rotten orange, the number of fresh oranges that are there its 4 directions can be found. With the passing of every minute, these fresh oranges will be rottened which will further rotten other fresh oranges in contact.

Consider each minute as level, where all the oranges will be rotten at once. Keeping this in mind, a level order traversal (BFS) can be performed making sure at each level, the fresh oranges in contact with the already rotten oranges gets rotten.

The number of levels for which the BFS is performed will denote the time taken by all oranges to rotten.

How to identify if all the oranges are rotten or not?
For this, a count can be maintained for the oranges that gets rotten after the traversal is complete. And a total count of oranges can be found by traversing the grid.
If the total count matches with the count of rotten oranges, it can be concluded that all the oranges were rotten.

Approach:
Determine the dimensions of grid. Variables are initialized to track time, total number of oranges, and the count of rotten oranges. A queue is taken for BFS traversal that will store the coordinates of the rotten oranges at that current level.
Traverse the grid and update the count of total oranges. If any cell containing rotten orange is found, add it to the queue.
Perform BFS to spread Rot. Continue until the queue is empty and for each level (each minute)
Record the size of the queue, which represents the number of rotten oranges at that moment. And update the count of rotten oranges by adding the size of the queue.
Process each rotten orange, by removing it from the queue, marking its four fresh oranges (if any) as rotten and adding them to the queue.
If new oranges are marked rotten during this process, increment the time.
After processing, if the count of rotten oranges matches the total number of oranges, return the time taken. If not all oranges are rotten, return -1 to indicate it's not possible to rot all oranges.
from collections import deque

class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
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
    
    # Function to find number of minutes 
    # so that all oranges get rotten
    def orangesRotting(self, grid):
        # Get the dimensions of grid
        n = len(grid)
        m = len(grid[0])
        
        # Variable to store time taken
        # to get all oranges rotten
        time = 0
        
        # Variable to store 
        # total count of oranges
        total = 0
        
        # Variable to store count of 
        # oranges that are rotten
        count = 0
        
        # Queue to perform BFS
        q = deque()
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                
                # If cell contains orange, 
                # increment total
                if grid[i][j] != 0:
                    total += 1
                    
                # If cell contains rotten 
                # orange, push in queue
                if grid[i][j] == 2:
                    q.append((i, j))
        
        # Perform BFS
        # Until the queue is empty
        while q:
            # Get the size of queue
            k = len(q)
            
            # Update count of rotten oranges
            count += k
            
            # Perform BFS for current level
            for _ in range(k):
                
                # Get the cell from queue
                row, col = q.popleft()
                
                # Traverse its 4 neighbors
                for i in range(4):
                    
                    # Coordinates of new cell
                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]
                    
                    # check for valid, unvisited 
                    # cells having fresh oranges
                    if (self.isValid(nRow, nCol, n, m) 
                        and grid[nRow][nCol] == 1):
                            
                        # Mark the new orange as rotten
                        # and add it to the queue
                        grid[nRow][nCol] = 2
                        q.append((nRow, nCol))
            
            # If new oranges are rotten, then
            # the time must be incremented
            if q:
                time += 1
        
        # If all the oranges are rotten,
        # return the time taken
        if total == count:
            return time
        
        # Otherwise return -1
        return -1

# Main function to test the solution
if __name__ == "__main__":
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find number of minutes 
    # so that all oranges get rotten
    ans = sol.orangesRotting(grid)
    
    print("The minimum number of minutes required for all oranges to rotten are:", ans)


Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of grid)
In the worst case, each fresh orange in the grid will be rotten and for each rotten orange, its 4 neighbors are checked taking O(4*N*M) time.

Space Complexity: O(N*M)
Using a queue data structure, which will store all cells if a grid is full of rotten oranges taking O(N*M) space.

  '''
from collections import deque

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    
    # Function to find number of minutes 
    # so that all oranges get rotten
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        time = 0
        total = 0
        count = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total += 1

                if grid[i][j] == 2:
                    q.append((i, j))
    
        while q:
            k = len(q)
            count += k
            for _ in range(k):
                row, col = q.popleft()
                for i in range(4):
                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]
                    
                    # check for valid, unvisited 
                    # cells having fresh oranges
                    if (self.isValid(nRow, nCol, n, m) 
                        and grid[nRow][nCol] == 1):
                        grid[nRow][nCol] = 2
                        q.append((nRow, nCol))
            if q:
                time += 1
        if total == count:
            return time
        return -1