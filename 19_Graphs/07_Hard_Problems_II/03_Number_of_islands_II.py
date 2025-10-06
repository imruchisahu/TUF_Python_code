'''
Given n, m denoting the row and column of the 2D matrix, and an array A of size k denoting the number of operations. Matrix elements are 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integers A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many islands are there in the matrix after each operation.



The answer array will be of size k.


Examples:
Input: n = 4, m = 5, k = 4, A = [[1,1],[0,1],[3,3],[3,4]] 

Output: [1, 1, 2, 2]

Explanation: The following illustration is the representation of the operation:



Input: n = 4, m = 5, k = 12, A = [[0,0],[0,0],[1,1],[1,0],[0,1],[0,3],[1,3],[0,4], [3,2], [2,2],[1,2], [0,2]] 

Output: [1, 1, 2, 1, 1, 2, 2, 2, 3, 3, 1, 1] 

Explanation: If we follow the process like in example 1, we will get the above result.

Input: n = 2, m = 2, k = 4, A = [[0,0],[0,1],[1,0],[1,1]] 

Output:
[1, 1, 1, 2]
[1, 1, 2, 1]
[1, 2, 2, 2]
[1, 1, 1, 1]

Submit
Constraints:
  1 <= n, m <= 1000
  1 <= k <= 104
  0 <= A[i][0] < n
  0 <= A[i][1] < m

Intuition:
It is clear that there is a need to find the number of islands after every operation. This implies that the problem statement refers to a dynamic graph (where edges are added after every operation). In such cases, the Disjoint Set data structure plays a huge role, using which the union(merge) operation can be performed in constant time.
Understanding:
Each cell in the matrix can be represented as a node in the disjoint set. An edge will be identified to be present between two land cells if and only if both the cells are in the same column or same row.

Every time a new cell is converted from sea to land, it can be assumed to be a single island, incrementing the count of islands by one. For every neighboring islands, the merging can be performed and the count of islands can be decremented with each merge.
How to store cells as nodes in the Disjoint Set?
The cells can be numbered sequentially as shown in the following figure:  Thus, a number can be assigned to a cell having coordinates (i, j) in the following way:
 Node number = i*n + j, where n is the number of columns in the grid
Approach:
Initialize a Disjoint Set Union (DSU) to manage the union and find operations for connected components. Use a visited matrix to keep track of cells that have been converted to land.
For each operation, convert the specified water cell to land:
If the cell is already land, skip to the next operation.
Assume the new land cell starts as a new island.Examine the four possible neighboring cells (up, down, left, right):
If a neighboring cell is also land, attempt to union the current cell with the neighboring cell.
If the cells are not already connected, decrement the island count and union the sets.
After processing each operation, store the current number of islands.
Output the number of islands after each operation.

class DisjointSet:
    # To store the ranks, parents and sizes
    # of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
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

# Solution class
class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    # Helper Function to check if a 
    # pixel is within boundaries
    def isValid(self, i, j, n, m):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        # Return true if pixel is valid
        return True

    # Function to return the number of 
    # islands after each operation
    def numOfIslands(self, n, m, A):
        # Disjoint set Data structure
        ds = DisjointSet(n * m)

        # Visited array
        vis = [[0] * m for _ in range(n)]

        # To store the count of islands
        cnt = 0

        # To store the result
        ans = []

        # Perform each operation
        for it in A:
            row = it[0]  # Row
            col = it[1]  # Column

            # If already a land cell, no new 
            # islands will be formed
            if vis[row][col] == 1:
                ans.append(cnt)
                continue

            # Make the cell as land
            vis[row][col] = 1

            # Increment the count considering 
            # the land cell was alone
            cnt += 1

            # Check all the neighbors
            for ind in range(4):
                # Get the coordinates of cell
                newRow = row + self.delRow[ind]
                newCol = col + self.delCol[ind]

                # If the cell is a valid land cell
                if (self.isValid(newRow, newCol, n, m) and 
                    vis[newRow][newCol] == 1):
                        
                    # Get the node and adjacent node number
                    nodeNo = row * m + col
                    adjNodeNo = newRow * m + newCol

                    # If not already connected, perform the union
                    if ds.findUPar(nodeNo) != ds.findUPar(adjNodeNo):
                        # Decrement count
                        cnt -= 1

                        # Perform the union
                        ds.unionBySize(nodeNo, adjNodeNo)

            # Store the number of islands after 
            # current operation in the result list
            ans.append(cnt)

        # Return the result
        return ans


# Main function
if __name__ == "__main__":
    n = 4
    m = 5
    k = 4
    A = [
        [1, 1],
        [0, 1],
        [3, 3],
        [3, 4]
    ]

    # Creating instance of Solution class
    sol = Solution()

    # Function call to return the number of
    # islands after each operation
    ans = sol.numOfIslands(n, m, A)

    # Output
    print("The number of islands after each operations are: ", end="")
    for num in ans:
        print(num, end=" ")

Complexity Analysis:
Time Complexity: O(K*4ɑ)
Each operation involves converting the sea cell to land cell and merging the nodes (if possible) taking an overall O(4ɑ) time. Since, there are a total of K operations, the overall time complexoty is O(K*4ɑ).

Space Complexity: O(K) + O(N*M)
The result list takes O(K) space. The visited array takes O(N*M) space and the Disjoint set uses parent and rank/size array storing all N*M nodes taking O(N*M) space.

'''
class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
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

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    def numOfIslands(self, n, m, A):
        ds = DisjointSet(n * m)
        vis = [[0] * m for _ in range(n)]
        cnt = 0
        ans = []

        for it in A:
            row = it[0]  # Row
            col = it[1]  # Column

            if vis[row][col] == 1:
                ans.append(cnt)
                continue
            vis[row][col] = 1
            cnt += 1

            for ind in range(4):
                newRow = row + self.delRow[ind]
                newCol = col + self.delCol[ind]
                if (self.isValid(newRow, newCol, n, m) and 
                    vis[newRow][newCol] == 1):
                    nodeNo = row * m + col
                    adjNodeNo = newRow * m + newCol
                    if ds.findUPar(nodeNo) != ds.findUPar(adjNodeNo):
                        cnt -= 1
                        ds.unionBySize(nodeNo, adjNodeNo)
            ans.append(cnt)
        return ans
        