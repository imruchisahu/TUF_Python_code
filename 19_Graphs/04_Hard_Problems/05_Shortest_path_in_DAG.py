'''
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges, where there is a directed edge from vertex edge[i][0] to vertex edge[i][1] with a distance of edge[i][2] for all i.



Find the shortest path from source vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex. The source vertex is assumed to be 0.


Examples:


Input: N = 4, M = 2 edge = [[0,1,2],[0,2,1]]



Output: 0 2 1 -1



Explanation:

Shortest path from 0 to 1 is 0->1 with edge weight 2. 

Shortest path from 0 to 2 is 0->2 with edge weight 1.

There is no way we can reach 3, so it's -1 for 3.

Input: N = 6, M = 7 edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]



Output: 0 2 3 6 1 5



Explanation:

Shortest path from 0 to 1 is 0->1 with edge weight 2. 

Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.

Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.

Shortest path from 0 to 4 is 0->4 with edge weight 1.

Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.

Input: N = 3, M = 3 edge = [[0, 1, 4], [0, 2, 2], [1, 2, 5]]

Output:
4 4 2
0 4 4
0 2 2
0 4 2

Submit
Constraints:
1 ≤ N,M ≤ 5*104
0 ≤ edge[i][0],edge[i][1] < N-1
1 ≤ edge[i][2] < 104

Intuition:
Finding the shortest path to a node is easy if the shortest paths to all the nodes that can precede it are known. Processing the nodes in topological order ensures that by the time a node is reached, all the nodes that can precede have already been processed, reducing the computation time significantly.
Thus, for the solution, the nodes will be traversed sequentially according to their reachability from the source.

Once the topological ordering is obtained, all the nodes can be processed one by one. For every vertex being processed, we update the distances of its adjacent using the distance of the current vertex.

Approach:
The graph is represented using an adjacency list where each node points to its neighboring nodes along with the edge weights.
Perform a Depth First Search (DFS) to obtain a topological order of the nodes, ensuring each node is processed before its successors.
Initialize a distance array with a high value (indicating infinity) for all nodes except the source node, which is set to zero.
Using the topological order, update the shortest distance for each node by relaxing the edges, meaning if a shorter path is found to a neighboring node, update its distance.
Mark nodes that remain unreachable with a distance of -1. Return the shortest distances from the source to all nodes.

from collections import defaultdict
from typing import List

class Solution:
    
    # Function to perform DFS traversal
    def topoSort(self, node, adj, vis, st):
        # Mark the node as visited 
        vis[node] = True
        
        # Traverse all the neighbors
        for v, _ in adj[node]:
            
            # If not visited, recursively perform DFS
            if not vis[v]:
                self.topoSort(v, adj, vis, st)
        
        """ Add the current node to stack 
        once all the nodes connected to it 
        have been processed """
        st.append(node)
    
    # Function to get the shortest path 
    # for every node from source node 0
    def shortestPath(self, N, M, edges):
        
        # To store the graph
        adj = defaultdict(list)
        
        # Add edges to the graph
        for u, v, wt in edges:
            # Add the weighted edge 
            adj[u].append((v, wt))
        
        # Visited array
        vis = [False] * N
        
        """ Stack to facilitate topological 
        sorting using DFS traversal """
        st = []
        
        # Get the topological ordering
        for i in range(N):
            if not vis[i]:
                self.topoSort(i, adj, vis, st)
        
        # Distance array to store the shortest paths
        dist = [1e9] * N
        
        # Distance of source node to itself is zero
        dist[0] = 0
        
        # Until the stack is not empty
        while st:
            
            # Get the node from top of stack
            node = st.pop()
            
            # Update the distances of adjacent nodes
            for v, wt in adj[node]:
                """ Relaxing the edge, i.e., if a 
                shorter path is found, update its
                distance to new shorter distance """
                if dist[node] + wt < dist[v]:
                    dist[v] = wt + dist[node]
        
        """ If a node is unreachable, 
        updating its distance to -1 """
        for i in range(N):
            if dist[i] == 1e9:
                dist[i] = -1
        
        # Return the result
        return dist


# Example usage
N, M = 4, 2
edges = [
    [0, 1, 2], [0, 2, 1]
]

# Creating an instance of Solution class
sol = Solution()

# Function call to determine order of 
# letters based on alien dictionary
ans = sol.shortestPath(N, M, edges)

# Output
print("The shortest distance of every node from source node is:")
print(*ans)

Complexity Analysis:
Time Complexity: O(N+M)
Topological Sorting takes O(N+M) time.
To relax all the vertices, each node and its adjacent nodes are traversed taking O(M) time.
Space Complexity: O(N+M)
Storing the graph takes O(M) space.
The stack storing the topological ordering takes O(N) space.
The topological sorting algorithm uses O(N) space due to visited array and recursion stack space.
'''
from collections import defaultdict


class Solution:
    def topoSort(self, node, adj, vis, st):
        vis[node] = True
        for v, _ in adj[node]:
            
            # If not visited, recursively perform DFS
            if not vis[v]:
                self.topoSort(v, adj, vis, st)
        st.append(node)
    
    def shortestPath(self, N, M, edges):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
        vis = [False] * N
        st = []
    
        for i in range(N):
            if not vis[i]:
                self.topoSort(i, adj, vis, st)
        dist = [1e9] * N
        dist[0] = 0
        while st:
            node = st.pop()
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = wt + dist[node]
        for i in range(N):
            if dist[i] == 1e9:
                dist[i] = -1
        return dist

