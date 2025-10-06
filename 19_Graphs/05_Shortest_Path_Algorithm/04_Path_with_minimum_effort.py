'''
A hiker is preparing for an upcoming hike. Given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of the cell (row, col). The hiker is situated in the top-left cell, (0, 0), and hopes to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,0-indexed). He can move up, down, left, or right. He wishes to find a route that requires the minimum effort.



A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.


Examples:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]

Output: 2

Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells. This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]

Output: 1

Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

Output:
1
0
2
3

Submit
Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

Intuition:
The problem resembles a pathfinding problem in a weighted graph, where we need to find a path with minimal maximum effort. We already know, traditional shortest path algorithms like Dijkstra's Algorithm are used to find the path with the minimum total cost. This gives an idea of using Dijkstra's algorithm to get to the solution. But there will be definitely some modifications needed.

Adapting Dijkstra's algorithm:
By slightly modifying the algorithm, it can be adapted to minimize the maximum effort:
Instead of accumulating total distances, the maximum effort encountered so far can be tracked.
And the priority queue (min-heap) can be used to store the pair {difference, {row of cell, column of cell}} which will help to always expand the least difference (effort) path first.
Comparing Edge Relaxation Steps in Dijkstra's Algorithms:
Normal Dijkstra: Updates the distance if the new distance is smaller.
new_distance = current_distance + edge_weight
new_distance = current_distance + edge_weight
Modified Dijkstra: Updates the effort if the new effort (max of current effort and edge effort) is smaller.
new_effort = max(current_effort, edge_effort)
Approach:
Define arrays to represent possible movement directions: up, down, left, and right. Create a matrix to track the minimum effort needed to reach each cell, initialized to a very large value.
Use a priority queue to explore cells starting from the top-left corner with an initial effort of 0. Extract the cell with the lowest effort from the priority queue. If this cell is the bottom-right corner, return the current effort as the result.
For each neighboring cell, calculate the effort required to move there, considering the maximum height difference encountered so far. Update the tracking matrix if this path offers a smaller maximum effort to reach the neighbor.
Push the neighboring cell with the updated effort into the priority queue. Continue this process until the queue is empty or the destination is reached.
If the priority queue is exhausted without reaching the destination, return a special value indicating failure (though this will never occur).
Dry Run:

import heapq

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

    # Function to determine minimum efforts 
    # to go from top-left to bottom-right
    def MinimumEffort(self, heights):
        
        # Get the dimensions of grid
        n = len(heights)
        m = len(heights[0])

        # To store maximum difference
        maxDiff = [[float('inf')] * m for _ in range(n)]
        
        # Min-Heap storing the pair: 
        # {diff, {row of cell, column of cell}}
        pq = []
        
        # Mark the initial position as 0
        maxDiff[0][0] = 0
        
        # Push the starting cell to min-heap
        heapq.heappush(pq, (0, 0, 0))

        # Until the min-heap is not empty
        while pq:
            
            # Get the cell with minimum 
            # difference (effort)
            diff, row, col = heapq.heappop(pq)
            
            # If the destination cell is reached, 
            # return the difference
            if row == n-1 and col == m-1: 
                return diff
            
            # Traverse its neighbors
            for i in range(4):
                
                # Get the coordinates 
                # of neighboring cell
                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]
                
                # Check if the cell is valid
                if self.isValid(newRow, newCol, n, m):
                    
                    # Get the current difference 
                    # in heights of cells
                    currDiff = abs(heights[newRow][newCol] - 
                                   heights[row][col])
                    
                    # Check if the current difference is 
                    # less than earlier known difference
                    if (max(currDiff, diff) < 
                        maxDiff[newRow][newCol]):
                        
                        # Store the current difference
                        maxDiff[newRow][newCol] = max(currDiff, diff)
                        
                        # Add the new pair found in the min-heap
                        heapq.heappush(pq, (max(currDiff, diff), newRow, newCol))
        
        # Return -1
        return -1

# Example usage
if __name__ == "__main__":
    
    heights = [
        [1, 2, 2], 
        [3, 8, 2], 
        [5, 3, 5]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to determine minimum efforts 
    # to go from top-left to bottom-right
    ans = sol.MinimumEffort(heights)
    
    # Output
    print(f"The minimum efforts required to go from cell (0,0) to cell (row-1, col-1) is: {ans}")

Complexity Analysis:
Time Complexity: O(N*M*log(N*M))

The algorithm processes each cell and explores its neighbors using a priority queue taking O(4*N*M) time.
The priority queue operations (insertion and extraction) are logarithmic in nature making overall complexity as O(4*N*M*log(N*M)).
Space Complexity: O(N*M)

Matrix to store maximum differences for each cell takes O(N*M) space.
Priority queue will store N*M elements in worst case contributing to O(N*M) space.

'''
import heapq
class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]

    # Function to check if a cell is valid
    def isValid(self, row, col, n, m):
        # Return false if the cell is invalid
        if row < 0 or row >= n: return False
        if col < 0 or col >= m: return False
        
        # Return true if the cell is valid
        return True
    def MinimumEffort(self, heights):
        n = len(heights)
        m = len(heights[0])
        maxDiff = [[float('inf')] * m for _ in range(n)]
        pq=[]
        maxDiff[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))
        while pq:
            diff, row, col = heapq.heappop(pq)
            if row == n-1 and col == m-1: 
                return diff
            for i in range(4):
                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]
            
                if self.isValid(newRow, newCol, n, m):
                    currDiff = abs(heights[newRow][newCol] - 
                                   heights[row][col])
                    if (max(currDiff, diff) < 
                        maxDiff[newRow][newCol]):
                        maxDiff[newRow][newCol] = max(currDiff, diff)
                        heapq.heappush(pq, (max(currDiff, diff), newRow, newCol))
        return -1


