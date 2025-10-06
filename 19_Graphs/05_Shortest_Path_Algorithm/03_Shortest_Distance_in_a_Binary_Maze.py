'''
Given an n x m matrix grid where each cell contains either 0 or 1, determine the shortest distance between a source cell and a destination cell. You can move to an adjacent cell (up, down, left, or right) if that adjacent cell has a value of 1. The path can only be created out of cells containing 1. If the destination cell is not reachable from the source cell, return -1.


Examples:
Input: grid = [[1, 1, 1, 1],[1, 1, 0, 1],[1, 1, 1, 1],[1, 1, 0, 0],[1, 0, 0, 1]], source = [0, 1], destination = [2, 2]

Output: 3

Explanation: The shortest path from (0, 1) to (2, 2) is:

Move down to (1, 1)

Move down to (2, 1)

Move right to (2, 2)

Thus, the shortest distance is 3

Input: grid = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 0],[1, 0, 1, 0, 1]], source = [0, 0], destination = [3, 4]

Output: -1

Explanation: 

Since, there is no path possible between the source cell and the destination cell, hence we return -1.

Input: grid = [[1, 0, 1],[1, 1, 0],[1, 1, 1]], source = [0, 0], destination = [2, 2]

Output:
3
2
5
4

Submit
Constraints:
1 ≤ n, m ≤ 500
grid[i][j] == 0 or grid[i][j] == 1
The source and destination cells are always inside the given matrix.

Intuition:
The problem includes finding the shortest path from the source to destination which gives the idea of using a Dijsktra's Algorithm. But since, all the edges are of unit weight, instead of using Dijsktra's algorithm, a simple BFS traversal will get the job done.

This involves using the Queue data structure in place of the Min-heap data structure improving the time complexity. As BFS traversal visits all cells in a level order fashion, it will ensure that whenever the destination cell is reached, it is reached via the shortest path.

A distance array will be used to store the shortest path of the intermediate nodes from the source node which will also be used to identify if a shorter path is found leading to the destination cell.

How to traverse the neighbors efficiently?
The 4 neighbours of the current cell can be shown like this: 
For efficient traversal of all neighboring pixels, the delRow and delCol arrays can be used where:
delRow = {-1, 0, 1, 0}
delCol = {0, 1, 0, -1}
Edge Cases:
If the source and destination cell are identical, 0 can be returned as the answer.
If no path from the source node to the destination node is found, -1 can be returned as the answer.
Approach:
Create a queue to facilitate BFS traversal. Each element in the queue stores the distance from the source and the coordinates of the cell. Determine the dimensions of the grid.
Create a distance matrix initialized to infinity to store the shortest distance from the source to each cell. Set the distance of the source cell to 0 and add it to the queue.
While the queue is not empty, process each cell:
Dequeue a cell and retrieve its distance and coordinates.
Iterate through its neighbors using the delta row and column arrays.
For each valid neighbor that contains a 1 and offers a shorter path, update the distance matrix.
If the destination cell is reached, return the distance.
If the queue is exhausted without reaching the destination, return -1, indicating the destination is not reachable.

from collections import deque

class Solution:
    # Delta row and column array
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]
    
    # Function to check if a cell is valid
    def isValid(self, row, col, n, m):
        # Return false if the cell is invalid
        if row < 0 or row >= n: return False
        if col < 0 or col >= m: return False
        # Return true if the cell is valid
        return True

    # Function to determine the shortest distance
    # between source and destination
    def shortestPath(self, grid, source, destination):
        # Edge Case
        if source == destination:
            return 0

        # Queue data structure to store the pairs of the 
        # form: {dist, {coordinates of cell}}
        q = deque()
        
        # Dimensions of grid
        n = len(grid)
        m = len(grid[0])

        # Distance matrix
        dist = [[float('inf')] * m for _ in range(n)]
        
        # Distance of source from itself is zero
        dist[source[0]][source[1]] = 0
        
        # Add the source to queue
        q.append((0, source[0], source[1]))

        # Until the queue is empty
        while q:
            # Get the element
            dis, row, col = q.popleft()

            # Iterate through all the neighbors
            for i in range(4):
                # Coordinates of the new cell
                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]

                # Checking the validity of the cell and 
                # updating if a shorter distance is found
                if (self.isValid(newRow, newCol, n, m) and 
                    grid[newRow][newCol] == 1 and 
                    dis + 1 < dist[newRow][newCol]):
                    
                    # Update the distance
                    dist[newRow][newCol] = 1 + dis

                    # Return the distance if the destination is reached
                    if (newRow, newCol) == destination:
                        return dis + 1
                    
                    # Add the new cell to queue
                    q.append((1 + dis, newRow, newCol))
        
        # If no path is found from source to destination
        return -1

if __name__ == "__main__":
    source = (0, 1)
    destination = (2, 2)
    
    grid = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to determine the shortest 
    # distance between source and destination
    ans = sol.shortestPath(grid, source, destination)
    
    print(f"The shortest distance from the source to destination is: {ans}")

Complexity Analysis:
Time Complexity: O(N*M) (where N and M are the dimensions of the grid)
A simple BFS traversal takes O(V+E) time where V and E represent the number of cells and number of edges.
Because, V = N*M and E = 4*N*M, the overall time complexity is O(N*M).

Space Complexity: O(N*M) The distance array takes O(N*M) space and the queue space can go upto O(N*M) in the worst case.
'''
from collections import deque


class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]
    # Function to check if a cell is valid
    def isValid(self, row, col, n, m):
        if row < 0 or row >= n: return False
        if col < 0 or col >= m: return False
        return True
    def shortestPath(self, grid, source, destination):
        if source == destination:
            return 0

        # Queue data structure to store the pairs of the 
        # form: {dist, {coordinates of cell}}
        q = deque()
        n = len(grid)
        m = len(grid[0])

        dist = [[float('inf')] * m for _ in range(n)]

        dist[source[0]][source[1]] = 0
        q.append((0, source[0], source[1]))
        while q:
            
            dis, row, col = q.popleft()
            for i in range(4):
                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]
                if (self.isValid(newRow, newCol, n, m) and 
                    grid[newRow][newCol] == 1 and 
                    dis + 1 < dist[newRow][newCol]):
                    dist[newRow][newCol] = 1 + dis
                    if (newRow, newCol) == destination:
                        return dis + 1
                    q.append((1 + dis, newRow, newCol))
        return -1
