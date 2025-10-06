'''
There are n stones at integer coordinate points on a 2D plane, with at most one stone per coordinate point. Some stones need to be removed.A stone can be removed if it shares the same row or the same column as another stone that has not been removed.



Given an array of stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the maximum possible number of stones that can be removed.


Examples:
Input : n=6, stones = [[0, 0],[ 0, 1], [1, 0],[1, 2],[2, 1],[2, 2]]

Output: 5

Explanation: One of the many ways to remove 5 stones is to remove the following stones:

[0,0], [1,0], [0,1], [2,1], [1,2]

Input : n = 6, stones = [[0, 0], [0, 2], [1, 3], [3, 1], [3, 2], [4, 3]]

Output: 4

Explanation: We can remove the following stones: [0,0], [0,2], [1,3], [3,1]

Input: n = 2, stones = [[0, 0], [0, 2]]

Output:
1
3
2
4

Submit
Constraints:
  1 <= n <=1000
  0 <= x[i], y[i]<= 104
  No two stones are at same position.

Intuition:
Observation:
Consider the following example: 

Here, there are two different groups of stones possible (assuming 0-based indexing):
The first group includes the stones at [0,0], [0,2], [3,2], and [3,1].
The second group includes stones at [1,3] and [4,3]
Note that each group consists of all stones that share either a row or column with another stone in the same group. For a particular group, all the stones can be removed from the group except one (as there will be no stones sharing a row or column for the last stone).

If the stones are considered as nodes, the different groups will refer to the different components of the graph.
How to identify the maximum number of nodes that can be removed?
Let's assume there are n stones in total. And these n stones have formed k different components each containing Xi no. of stones. This indicates the following:  Thus, the maximum number of stones that can be removed can be found if the number of connected components(k) in the graph is known.
How to get the number of connected components?
One way to find the number of connected components is by traversing the graph using one of the two traversal techniques.
Another way is to use the Disjoint Set data structure, which will help in connecting the stones that belong to the same group(component).
How to connect the cells containing stones to form a component?
To connect the cells it can be assumed that each entire row and column of the 2D plane is a particular node. Now, each row can be connected(united) with the corresponding column where the stones are located. However, the column number may be the same as the row number.
To avoid this, each column number can be converted to (column no. + total no. of rows) and the union of row number and the converted column number i.e. (column no. + total no. of rows) can be performed as shown in the following example: 
For the above example, to connect the two stones in the cells [0, 0] and [0, 2] of the first row, firstly row number can be taken i.e. 0(because of 0-based indexing) as a node, and then the converted column numbers 0 to (0+5) and 2 to (2+5). Then, the union of (0 and 5) and (0 and 7) can be performed to form the connected components.
Approach:
Traverse the list of stones to find the maximum row and column indices. This helps in defining the size of the Disjoint Set data structure.
Create a Disjoint Set data structure large enough to accommodate all rows and columns. Each row and column is treated as a separate node.
For each stone, treat its row and column as nodes and unite them using the union by size method. This ensures that stones sharing the same row or column are in the same connected component.
Use a map to keep track of unique nodes that have stones. This helps in counting distinct connected components.
Iterate through the unique nodes and count how many distinct components there are by finding the ultimate parent of each node.
The maximum number of stones that can be removed is the total number of stones minus the number of connected components.
Return the calculated number of stones that can be removed.

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

# Solution class
class Solution:
    # Function to remove maximum stones 
    def maxRemove(self, stones, n):
        # To store the maximum row and column having a stone
        maxRow = 0
        maxCol = 0
        
        # Iterate on all the nodes
        for it in stones:
            maxRow = max(maxRow, it[0])
            maxCol = max(maxCol, it[1])
        
        # Disjoint Set data structure
        ds = DisjointSet(maxRow + maxCol + 1)
        
        # To store the nodes having a stone in Disjoint Set
        stoneNodes = {}
        
        # Iterate on all stones
        for it in stones:
            # Row number
            nodeRow = it[0]
            
            # Converted column number
            nodeCol = it[1] + maxRow + 1
            
            # United two nodes
            ds.unionBySize(nodeRow, nodeCol)
            
            # Add the nodes to the map
            stoneNodes[nodeRow] = 1
            stoneNodes[nodeCol] = 1
        
        # To store the number of connected components
        k = 0
        
        # Iterate on the set
        for key in stoneNodes:
            # Increment the count if a new component is found
            if ds.findUPar(key) == key:
                k += 1
        
        # Return the answer
        return n - k

# Main function to test the Solution class
if __name__ == "__main__":
    n = 6
    stones = [
        [0, 0], [0, 1], [1, 0],
        [1, 2], [2, 1], [2, 2]
    ]

    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to get the size of the largest island
    ans = sol.maxRemove(stones, n)
    
    # Output
    print("The size of the largest island is:", ans)

Complexity Analysis:
Time Complexity: O(N) The given stones array is traversed multiple times. Traversing the hashset will also take O(N) time.

Space Complexity: O(Max Row number + Max Column number) The Disjoint set will store the nodes using the parent and size/rank array which will take (2*number of nodes) space. Since, the number of nodes = max row number + max column number, the overall space complexity is O(Max Row number + Max Column number).

'''
class DisjointSet:
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

class Solution:
    def maxRemove(self, stones, n):
        maxRow = 0
        maxCol = 0
        for it in stones:
            maxRow = max(maxRow, it[0])
            maxCol = max(maxCol, it[1])
        ds = DisjointSet(maxRow + maxCol + 1)
        stoneNodes = {}
        for it in stones:
            nodeRow = it[0]
            nodeCol = it[1] + maxRow + 1
            
            # United two nodes
            ds.unionBySize(nodeRow, nodeCol)
            
            # Add the nodes to the map
            stoneNodes[nodeRow] = 1
            stoneNodes[nodeCol] = 1
        
        # To store the number of connected components
        k = 0
        
        # Iterate on the set
        for key in stoneNodes:
            # Increment the count if a new component is found
            if ds.findUPar(key) == key:
                k += 1
        return n - k