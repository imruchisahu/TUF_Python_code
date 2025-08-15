'''
Given an integer M and an undirected graph with N vertices and E edges. The goal is to determine whether the graph can be coloured with a maximum of M colors so that no two of its adjacent vertices have the same colour applied to them.



In this context, colouring a graph refers to giving each vertex a different colour. If the colouring of vertices is possible then return true, otherwise return false.


Examples:
Input : N = 4 , M = 3 , E = 5 , Edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]

Output : true

Explanation : Consider the three colors to be red, green, blue.

We can color the vertex 0 with red, vertex 1 with blue, vertex 2 with green, vertex 3 with blue.

In this way we can color graph using 3 colors at most.



Input : N = 3 , M = 2 , E = 3 , Edges = [ (0, 1) , (1, 2) , (0, 2) ]

Output : false

Explanation : Consider the three colors to be red, green.

We can color the vertex 0 with red, vertex 1 with blue.

As the vertex 2 is adjacent to both vertex 1 and 0 , so we cannot color with red and green.

Hence as we could not color all vertex of graph we return false.



Input : N = 5 , M = 3 , E = 6 , Edges = [ (0, 1) , (1, 2) , (0, 2) , (2,3) , (2,4) , (3,4) ]

Output:
false
true

Submit
Constraints:
1 <= N <= 20
1 <= E <= (N*(N-1)/2)
1 <= M <= N

Real-Life Problem Solving
Consider a scenario where several tasks need to be scheduled, each task requiring a specific resource. The objective is to assign resources to tasks such that no two tasks requiring the same resource are scheduled simultaneously. This is akin to assigning colors to nodes in a graph, where no two adjacent nodes (tasks) share the same color (resource). The challenge is to determine if it's possible to schedule all tasks using a limited number of resources.

Recursion Process Intuition
Imagine attempting to assign a color to a node in a graph, starting from the first node and moving sequentially. For each node, every possible color is tried, ensuring it does not conflict with already colored adjacent nodes. If a valid color is found, the process moves to the next node. If a conflict arises, the current assignment is undone (backtracked), and the next color is attempted. This recursive process continues until all nodes are successfully colored or all possibilities are exhausted, indicating no valid coloring exists.

Approach
Represent the graph using an adjacency list for efficient traversal and initialize a colors array to keep track of the assigned colors for each node, starting with no colors assigned.
Define a function to check if it's safe to assign a specific color to a node by ensuring no adjacent node has the same color.
Implement a recursive function to attempt to color each node:
If all nodes are successfully colored, return true.
For the current node, try all possible colors from 1 to m.
Check if assigning a color is safe using the helper function.
If safe, assign the color and recursively attempt to color the next node.
If coloring the next node fails, reset the current node's color and try the next color.
If no valid color is found, return false.
Start the coloring process from the first node and continue recursively until all nodes are processed. The result of the recursive function indicates whether the graph can be colored with the given number of colors.

class Solution:
    def isSafe(self, col, node, colors, adj):
        # Function to check if it's safe to color the node with a given color
        # Check adjacent nodes
        for neighbor in adj[node]:
            # If an adjacent node has the same color
            if colors[neighbor] == col:
                return False
        return True # Safe to color

    def solve(self, node, m, n, colors, adj):
        # Recursive function to solve graph coloring problem
        # If all nodes are colored
        if n == node:
            return True
        # Try all colors from 1 to m
        for i in range(1, m + 1):
            # Check if it is safe to color the node with color i
            if self.isSafe(i, node, colors, adj):
                colors[node] = i # Assign color i to node
                # Recursively try to color the next node
                if self.solve(node + 1, m, n, colors, adj):
                    return True
                colors[node] = 0 # Reset color if it doesn't lead to a solution
        return False # No color can be assigned

    def graphColoring(self, edges, m, n):
        # Function to check if the graph can be colored with m colors
        adj = [[] for _ in range(n)] # Create adjacency list representation of the graph
        # Build the graph from edges
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        colors = [0] * n # Initialize all colors to 0 (uncolored)
        # Start solving from the first node
        return self.solve(0, m, n, colors, adj)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    edges = [
        [0, 1], [0, 2], [1, 2], [1, 3]
    ]
    m = 3 # Number of colors
    n = 4 # Number of nodes

    # Check if the graph can be colored with m colors
    if sol.graphColoring(edges, m, n):
        print("The graph can be colored with", m, "colors.")
    else:
        print("The graph cannot be colored with", m, "colors.")
Complexity Analysis
Time Complexity : O(M^N) where m is the number of colors and n is the number of nodes, since each node can be colored in m ways and there are n nodes to color.

Space Complexity : O(N) for the colors array and O(n) for the adjacency list, resulting in O(N) total space complexity.

'''
class Solution:
    def isSafe(self, col, node, colors, adj):
        for neighbor in adj[node]:
            if colors[neighbor] == col:
                return False
        return True

    def solve(self, node, m, n, colors, adj):
        if n == node:
            return True
        for i in range(1, m + 1):
            if self.isSafe(i, node, colors, adj):
                colors[node] = i 
                if self.solve(node + 1, m, n, colors, adj):
                    return True
                colors[node] = 0 
        return False 

    def graphColoring(self, edges, m, n):
        adj = [[] for _ in range(n)] 
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        colors = [0] * n 
        return self.solve(0, m, n, colors, adj)