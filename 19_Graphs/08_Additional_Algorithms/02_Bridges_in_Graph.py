'''
Given an undirected connected Graph with V vertices (Numbered from 0 to V-1) and E edges. An edge is represented [ai, bi] denoting that there is an edge from vertex ai to bi . An edge is called a bridge if its removal makes some vertex unable to reach another vertex.



Return all bridges in the graph in any order.


Examples:




Input: V = 4, E = [ [0,1],[1,2],[2,0],[1,3] ]

Output: [ [1, 3] ]

Explanation: The edge [1, 3] is the critical edge because if we remove the edge the graph will be divided into 2 components.





Input: V = 3, E = [[0,1],[1,2],[2,0]]

Result: []

Explanation: There no bridges in the graph.

Input: V = 2, E = [[0,1]]

Output:
[[0,1]]
[ ]

Submit
Constraints:
2 <= V, E <= 104
0 <= ai, bi <= V - 1

Intuition:
Any edge in a component of a graph is called a bridge when the component is divided into 2 or more components if that particular edge is removed.

Example:
Consider the following graph: If in this graph, if the edge (5,6) is removed, the component gets divided into 2 components making this edge a bridge. But the edge (2,3) is removed, the component remains connected. So, this edge is not a bridge. In this graph, we have a total of 3 bridges i.e. (4,5), (5,6), and (10, 8).

To solve this problem, the Tarjan's algorithm for finding bridges (or cut-edges) in a graph will come into picture. It is based on depth-first search (DFS) which uses the concept of discovery and low times for nodes. The core idea is to identify edges that, when removed, increase the number of connected components in the graph.
Understanding:
Before moving to the algorithm, it is important to know about the two arrays that play a crucial role in the algorithm:
Discovery time / Time of insertion Array: During the DFS call, the time when a node is visited first (discovered first), is called its time of insertion or discovery time. This array will store the discovery times of the nodes.
Usage: It helps keep track of when each node was first visited. This value is unique and incremental, meaning it increases as the DFS progresses.
Lowest time of insertion Array: The lowest time of insertion for a node refers to The minimum discovery time that can be reached from a node, considering all its descendants and back edges to its ancestors.
Usage: It helps determine if there is a back edge that connects the node or its descendants to an ancestor, which is essential for identifying bridges.
By tracking the discovery and lowest reachable times of nodes during DFS, it can identify edges that, when removed, increase the number of connected components, thus identifying bridges.
How the two arrays help in identifying the bridges in a graph?
Consider two nodes, node u and node v, where v is the neighbor of u. Let us assume that tin[u] represents the discovery time of node u and low[v] represents the lowest discovery time reachable from node v.

If low[v] > tin[u]:
It implies that v and its descendants cannot reach u or any of u's ancestors without the edge (u, v). Therefore, removing (u, v) would disconnect u and v, making (u, v) a bridge.

Thus, when the DFS calls to the descendants are completed, this condition can be checked to identify all the edges that are a bridge.
Approach:
Create adjacency lists from the graph edges. Initialize two arrays to store discovery (insertion) and lowest times for each node. Initialize a visited array to keep track of visited nodes and a timer to keep track of discovery time. Create a list to store the bridges.
Begin DFS from an arbitrary node (node 0 or any other if the graph has multiple components). Set the parent of the starting node to -1 (indicating no parent).
For each node, mark it as visited and set its discovery and lowest time to the current timer value, then increment the timer.
Process Neighbors: For each neighbor of the current node:
Skip the parent node to avoid backtracking.
If the neighbor is not visited, recursively perform DFS on this neighbor:
After returning from the recursive call, update the lowest time of the current node.
If the lowest time of the neighbor is greater than the discovery time of the current node, it indicates a bridge.
If the neighbor is already visited and not the parent, update the lowest time of the current node based on the neighbor's discovery time.
During the DFS, check the condition low[neighbor] > tin[current_node] to determine if the edge is a bridge. Add the bridge to the list of bridges if the condition is met.
After completing the DFS for all nodes, return the list of identified bridges.

class Solution:
    def __init__(self):
        self.timer = 1
    
    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        # Mark the node as visited
        vis[node] = 1
        
        # Time of insertion and the lowest time of 
        # insert for node will be the current time
        tin[node] = low[node] = self.timer
        
        # Increment the current time
        self.timer += 1
        
        # Traverse all its neighbors
        for it in adj[node]:
            # Skip the parent
            if it == parent:
                continue
            
            # If a neighbor is not visited
            if vis[it] == 0:
                # Make a recursive DFS call
                self.dfs(it, node, vis, adj, tin, low, bridges)
                
                # Once the recursive DFS call returns, update
                # the lowest time of insertion for the node
                low[node] = min(low[it], low[node])

                # If the lowest time of insertion of the 
                # node is found to be greater than the 
                # time of insertion of the neighbor
                if low[it] > tin[node]:
                    # The edge represents a bridge
                    bridges.append([it, node])
            else:
                # Update the lowest time of insertion of the node
                low[node] = min(low[node], tin[it])

    def criticalConnections(self, n, connections):
        # Adjacency list
        adj = [[] for _ in range(n)]
        
        # Add all the edges to the adjacency list
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # Visited array
        vis = [0] * n
        
        # To store the time of insertion (discovery time) of nodes
        tin = [0] * n
        
        # To store the lowest time of insert of the nodes
        low = [0] * n
        
        # To store the bridges of the graph
        bridges = []
        
        # Start a DFS traversal from node 0 with its parent as -1
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        
        # Return the computed result
        return bridges

# Main function
if __name__ == "__main__":
    V = 4
    E = [
        [0, 1],
        [1, 2],
        [2, 0],
        [1, 3]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to identify the bridges in a graph
    ans = sol.criticalConnections(V, E)
    
    print("The critical connections in the given graph are:")
    for bridge in ans:
        print(bridge[0], bridge[1])

Complexity Analysis:
Time Complexity: O(V+E) (where E represents the number of edges in the graph)
A DFS traversal is performed which takes O(V+E) time.

Space Complexity: O(V) The algorithm uses two arrays to store the discovery time and lowest
 time of insertion taking O(V) space. The list of bridges returned will take O(E) space in worst-case when all the edges are bridges in the graph.

'''
class Solution:
    def __init__(self):
        self.timer = 1
    
    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        for it in adj[node]:
            if it == parent:
                continue
            if vis[it] == 0:
                self.dfs(it, node, vis, adj, tin, low, bridges)
                low[node] = min(low[it], low[node])
                if low[it] > tin[node]:
                    bridges.append([it, node])
            else:
                low[node] = min(low[node], tin[it])

    def criticalConnections(self, V, E):
        adj = [[] for _ in range(V)]
        for u, v in E:
            adj[u].append(v)
            adj[v].append(u)
    
        vis = [0] * V
        tin = [0] * V
        low = [0] * V
        bridges = []
        
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges
    
     
