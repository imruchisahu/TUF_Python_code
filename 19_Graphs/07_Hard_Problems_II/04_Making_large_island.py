'''
Given an n x n binary matrix grid, it is allowed to change at most one 0 to 1. A group of connected 1s forms an island, where two 1s are connected if they share one of their sides.



Return the size of the largest island in the grid after applying this operation.


Examples:
Input: grid = [[1,0],[0,1]]

Output: 3

Explanation: We change any one 0 to 1 and connect two 1s, then we get an island with maximum area = 3.

Input: grid = [[1,1],[1,1]]

Output: 4

Explanation: The largest island already exists with size 4.

Input: grid = [[1,1],[1,0]]

Output:
3
4
2
1

Submit
Constraints:
1 <= n <= 500
0 <= grid[i][j] <= 1 

Intuition:
In the given grid, there are different sizes of connected 1s already present. The problem allows converting a single cell containing 0 to 1, and the goal is to form the largest island.

One way to solve this is by using the brute force approach by finding the largest island formed in the grid by successively converting each cell containing 0 to 1. The largest island found in all such cases will be the island with the most 1s which can be returned as our answer.

Understanding:
As each time, a cell having 0 is turned into 1, it forms an edge with its four neighbors(islands), if existing. This indicates that the graph is dynamic in nature. Now, adding an edge in a dynamic graph can be easily achieved using the Disjoint Set data structure.
Using the Union By Size method in the Disjoint Set data structure, not only the efficient addition of edges can be done but also, the size of islands after merging can be found.
How to store cells as nodes in the Disjoint Set?
The cells can be numbered sequentially as shown in the following figure:

Thus, a number can be assigned to a cell having coordinates (i, j) in the following way:
 Node number = i*n + j, where n is the number of columns in the grid
Edge Cases:
Consider the following graph:

In the given grid, all the cells with 0 will be converted one by one to check for the largest island. Considering 0-based indexing, the cell (3,3) will be converted to 1, and while checking:
Left Island: The size of island will be incremented by 7.
Top Island: The size of island will be incremented by 6.
Right Island: No change in the size of the island as there is no island present on the right.
Bottom Island: Again the size of the island will be incremented by 7.

But the island of size 7 should have been considered only once while finding the size of the large island. This case can be avoided by storing the ultimate parents for the neighboring islands in a set data structure. This will ensure that one island will never be considered more than once in the size of large island.
What if all the cells are 1 in the grid?
In such case, only one island will be formed which will be the largest for which the size of the ultimate parent of the island can be returned as the answer.
Approach:
Create a Disjoint Set data structure to manage connected components (islands) in the grid. Each cell is treated as a separate component initially.
Traverse through the grid to identify initial islands (connected 1s) and perform union operations to merge adjacent land cells into the same component using the union by size method.
Traverse the grid again to consider each 0 cell, and determine the potential island size if this 0 is changed to 1.
For each 0 cell, check all its neighboring cells to find unique components (using ultimate parents) and calculate the combined size of these components.
Keep track of the maximum island size encountered during the above calculations. Additionally, handle edge cases where no 0 cells are present in the grid by checking the sizes of existing islands.
Return the size of the largest possible island after changing at most one 0 to 1.

class DisjointSet:
    # To store the ranks, parents and 
    # sizes of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
    def getSize(self, node):
        return self.size[self.findUPar(node)]

# Solution class
class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
    # Helper function to check if a 
    # pixel is within boundaries
    def isValid(self, i, j, n):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= n:
            return False
        # Return true if pixel is valid
        return True
    
    # Function to add initial islands to the 
    # disjoint set data structure
    def addInitialIslands(self, grid, ds, n):
        # Traverse all the cells in the grid
        for row in range(n):
            for col in range(n):
                # If the cell is not land, skip
                if grid[row][col] == 0:
                    continue
                
                # Traverse on all the neighbors
                for ind in range(4):
                    # Get the coordinates of neighbor
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    # If the cell is valid and a land cell
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                            
                        # Get the number for node
                        nodeNo = row * n + col
                        # Get the number for neighbor
                        adjNodeNo = newRow * n + newCol
                        
                        # Take union of both nodes as 
                        # they are part of the same island
                        ds.unionBySize(nodeNo, adjNodeNo)
    
    # Function to get the size of the largest island
    def largestIsland(self, grid):
        # Dimensions of grid
        n = len(grid)
        
        # Disjoint set data structure
        ds = DisjointSet(n * n)
        
        # Function call to add initial 
        # islands in the disjoint set
        self.addInitialIslands(grid, ds, n)
        
        # To store the answer
        ans = 0
        
        # Traverse on the grid
        for row in range(n):
            for col in range(n):
                # If the cell is a land cell, skip
                if grid[row][col] == 1:
                    continue
                
                # Set to store the ultimate 
                # parents of neighboring islands
                components = set()
                
                # Traverse on all its neighbors
                for ind in range(4):
                    # Coordinates of neighboring cell
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                        # Perform union and store 
                        # ultimate parent in the set
                        nodeNumber = newRow * n + newCol
                        components.add(ds.findUPar(nodeNumber))
                
                # To store the size of current largest island
                sizeTotal = 0
                
                # Iterate on all the neighboring ultimate parents
                for parent in components:
                    # Update the size
                    sizeTotal += ds.getSize(parent)
                
                # Store the maximum size of island
                ans = max(ans, sizeTotal + 1)
        
        # Edge case
        for cellNo in range(n * n):
            # Keep the answer updated
            ans = max(ans, ds.getSize(cellNo))
        
        # Return the answer
        return ans

# Main function to test the Solution class
if __name__ == "__main__":
    grid = [
        [1, 0],
        [0, 1]
    ]

    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to get the size of the largest island
    ans = sol.largestIsland(grid)
    
    # Output
    print("The size of the largest island is:", ans)

Complexity Analysis:
Time Complexity: O(N2) Using nested loops, and within the loops, all the operations take constant time.

Space Complexity: O(N2) The Disjoint set storing N2 nodes (cells) will take up 2*N2 space due to parent and size arrays.

'''
class DisjointSet:
    # To store the ranks, parents and 
    # sizes of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
    def getSize(self, node):
        return self.size[self.findUPar(node)]

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
    # Helper function to check if a 
    # pixel is within boundaries
    def isValid(self, i, j, n):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= n:
            return False
        # Return true if pixel is valid
        return True
    
    # Function to add initial islands to the 
    # disjoint set data structure
    def addInitialIslands(self, grid, ds, n):
        # Traverse all the cells in the grid
        for row in range(n):
            for col in range(n):
                # If the cell is not land, skip
                if grid[row][col] == 0:
                    continue
                
                # Traverse on all the neighbors
                for ind in range(4):
                    # Get the coordinates of neighbor
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    # If the cell is valid and a land cell
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                            
                        # Get the number for node
                        nodeNo = row * n + col
                        # Get the number for neighbor
                        adjNodeNo = newRow * n + newCol
                        
                        # Take union of both nodes as 
                        # they are part of the same island
                        ds.unionBySize(nodeNo, adjNodeNo)
    
    # Function to get the size of the largest island
    def largestIsland(self, grid):
        # Dimensions of grid
        n = len(grid)
        
        # Disjoint set data structure
        ds = DisjointSet(n * n)
        
        # Function call to add initial 
        # islands in the disjoint set
        self.addInitialIslands(grid, ds, n)
        
        # To store the answer
        ans = 0
        
        # Traverse on the grid
        for row in range(n):
            for col in range(n):
                # If the cell is a land cell, skip
                if grid[row][col] == 1:
                    continue
                
                # Set to store the ultimate 
                # parents of neighboring islands
                components = set()
                
                # Traverse on all its neighbors
                for ind in range(4):
                    # Coordinates of neighboring cell
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                        # Perform union and store 
                        # ultimate parent in the set
                        nodeNumber = newRow * n + newCol
                        components.add(ds.findUPar(nodeNumber))
                
                # To store the size of current largest island
                sizeTotal = 0
                
                # Iterate on all the neighboring ultimate parents
                for parent in components:
                    # Update the size
                    sizeTotal += ds.getSize(parent)
                
                # Store the maximum size of island
                ans = max(ans, sizeTotal + 1)
        
        # Edge case
        for cellNo in range(n * n):
            # Keep the answer updated
            ans = max(ans, ds.getSize(cellNo))
        
        # Return the answer
        return ans
       