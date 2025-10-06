'''

Given a graph with n vertices and m edges. The graph is represented by an array Edges, where Edge[i] = [a, b] indicates an edge between vertices a and b. One edge can be removed from anywhere and added between any two vertices in one operation. Find the minimum number of operations that will be required to make the graph connected. If it is not possible to make the graph connected, return -1.


Examples:
Input : n = 4, Edge =[ [0, 1], [ 0, 2], [1, 2]]

Output: 1

Explanation: We need a minimum of 1 operation to make the two components connected. We can remove the edge (1,2) and add the edge between node 2 and node 3 like the following:

Input: n = 9, Edge = [[0,1],[0,2],[0,3],[1,2],[2,3],[4,5],[5,6],[7,8]]

Output: 2

Explanation: We need a minimum of 2 operations to make the two components connected. We can remove the edge (0,2) and add the edge between node 3 and node 4 and we can remove the edge (0,3) and add it between nodes 6 and 8 like the following:

Input: n = 4, Edge =[[0, 1]]

Output:
0
3
4
-1

Submit
Constraints:
  1 <= n <= 104
  1 <= Edge.length <= 104
  Edge[i].length == 2
  

Intuition:
The problem involves removing an edge and adding it between two other nodes, indicating that the graph is updating continuously. This gives the idea of using the Disjoint Set Data Structure.

Now, to make the graph connected, all the different components of the graphs must be connected to each other (directly or indirectly). The minimum number of edges required to connect all the components is always one lesser than the number of components. Hence, the problem boils down to finding the number of components in the given graph. Once found, the minimum number of edges to connect the graph can be found. If the number of edges present in the graph is less than that required to connect the graph, it is impossible to connect the graph and thus -1 can be returned.

Approach:
Check if it is possible to connect the graph or not. If found not possible, return -1.
Initialize a Disjoint Set to manage connected components.
Process each edge to unify connected vertices.
Count the number of connected components by identifying unique parents.
The required operations are the number of connected components minus one.

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

    # Function to get the number of 
    # operations to make network connected
    def solve(self, n, Edge):
        
        # Get the number of edges
        size = len(Edge)
        
        # Return -1 if connecting all 
        # vertices is not possible
        if size < n - 1:
            return -1
        
        # Disjoint Set data structure
        ds = DisjointSet(n)
        
        # Add all the edges in the set
        for i in range(size):
            ds.unionByRank(Edge[i][0], Edge[i][1])
        
        # To store count of required edges
        count = 0
        
        # Finding the number of components
        for i in range(n):
            if ds.parent[i] == i:
                count += 1
        
        # Return the result
        return count - 1

# Creating instance of Solution class
sol = Solution()

# Function call to get the number of 
# operations to make network connected
n = 4
Edge = [
    [0, 1], 
    [0, 2], 
    [1, 2]
]
ans = sol.solve(n, Edge)

print("The number of operations to make network connected is:", ans)

Complexity Analysis:
Time Complexity: O(N+M) (where N and M represent the number of vertices and edges in the graph)
Adding all M edges to the disjoint set takes O(M) time, and finding the number of components in the graph by finding unique ultimate parent node takes O(N) time.

Space Complexity: O(N)
The Disjoint Set data structure uses the parent and size/rank arrays of O(N) size each to perform the Union operation and to find the Ultimate parent.

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
    def solve(self, n, Edge):
        size = len(Edge)
        if size < n - 1:
            return -1
        ds = DisjointSet(n)
        for i in range(size):
            ds.unionByRank(Edge[i][0], Edge[i][1])
        count = 0
        for i in range(n):
            if ds.parent[i] == i:
                count += 1
        return count - 1
