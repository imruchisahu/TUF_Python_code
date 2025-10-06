'''
Given a Undirected Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges, where there is a edge from vertex edges[i][0] to vertex edges[i][1] of unit weight.



Find the shortest path from the source to all other nodes in this graph. In this problem statement, we have assumed the source vertex to be ‘0’. If a vertex is unreachable from the source node, then return -1 for that vertex.


Examples:
Input: n = 9, m = 10, edges = [[0,1],[0,3],[3,4],[4,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]



Output: 0 1 2 1 2 3 3 4 4



Explanation:

The above output array shows the shortest path to all 

the nodes from the source vertex (0), Dist[0] = 0, Dist[1] = 1 , Dist[2] = 2 , …. Dist[8] = 4.Where Dist[node] is the shortest path between src and the node. For a node, if the value of Dist[node]= -1, then we conclude that the node is unreachable from the src node.

Input: n = 8, m = 10, edges =[[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]



Output: 0 1 2 1 2 3 3 2



Explanation: 

The above output list shows the shortest path to all the nodes from the source vertex (0), Dist[0] = 0, Dist[1] = 1, Dist[2] = 2,.....Dist[7] = 2.

Input: n = 3, m = 1, edges = [[1,2]]

Output:
0 -1 -1
-1 -1 -1
0 1 1
0 0 0

Submit
Constraints:
1<=n,m<=104
0<=edges[i][j]<=n-1

Intuition:
This problem was solved for directed graphs. One way is to convert the undirected graph into a directed one that requires converting every undirected edge between node a and node b to two directed edges:

From node a to node b. (a->b)
From node b to node a. (b->a)

But this approach will require a significant time to convert the undirected graph to a directed graph due to which it is not a preferred way to solve this problem.
Observation:
Since the question is asking for shortest path to every node, let's try using simple BFS traversal starting from source node (node 0) for the given graph:
Image 1
Image 2
Image 3

1/3




It can be seen that for a particular level, all the nodes that are present in the queue have the distance from source node 0 equal to the level number. And since a BFS traversal is performed, it ensures that whenever a node is visited for the first time, it is visited by the shortest path (provided all the edges in the graph are of unit weight).

Hence, a simple BFS traversal can be performed and the distances of the nodes can be found based on the level of BFS traversal. Also, if for particular node is visited from two paths, the distance of the shorter path will be considered.
Modification:
In a BFS traversal, a visited array is required to avoid visiting nodes that are already visited. But since a distance array will be used to store the minimum distance of nodes from source node (node 0), having all values initialized as infinity, the distance array itself can be used as a visited array. It ensures that if a node is visited by a distance larger than the distance in the array, then it is already been visited via a shorter path. Hence, the use of visited array can be avoided optimizing the code.
Approach:
Use an adjacency list to represent the graph. Create a distance array initialized to infinity for all nodes. Set the distance of the source node (0) to 0.
Perform BFS traversal starting from the source node (node 0). Use a queue to perform BFS from the source node.
For each node, update the distance of its adjacent nodes if a shorter path is found and push the node in the queue. Update distances to -1 for nodes that remain unreachable.
Return the result stored.

from collections import deque

class Solution:

    # Function to perform BFS traversal
    def bfs(self, src, adj, dist):
        
        # Distance of source node from itself is zero
        dist[src] = 0 
        
        # Queue to facilitate BFS traversal
        q = deque()
        
        # Adding source node to queue
        q.append(src) 
        
        # Until the queue is empty
        while q:
            
            # Get the node from queue
            node = q.popleft()
            
            # Traverse all its neighbors
            for adjNode in adj[node]:
                
                # If a shorter distance is found
                if dist[node] + 1 < dist[adjNode]:
                    
                    # Update the distance
                    dist[adjNode] = 1 + dist[node]
                    
                    # Add the node to the queue
                    q.append(adjNode)
    
    # Function to get the shortest path 
    # for every node from source node 0
    def shortestPath(self, edges, N, M):
        
        # To store the graph
        adj = [[] for _ in range(N)]
        
        # Add edges to the graph
        for edge in edges:
            u = edge[0] # first node
            v = edge[1] # second node
            
            # Add the edge
            adj[u].append(v)
            adj[v].append(u)
        
        # Distance array to store the shortest paths
        dist = [float('inf')] * N
        
        # Start the BFS traversal from source node
        self.bfs(0, adj, dist)
        
        # If a node is unreachable, 
        # updating its distance to -1
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        # Return the result
        return dist

# Main function to execute the code
if __name__ == "__main__":
    
    N = 9
    M = 10
    edges = [
        [0, 1], [0, 3], [3, 4], 
        [4, 5], [5, 6], [1, 2], 
        [2, 6], [6, 7], [7, 8], [6, 8]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to determine shortest paths
    ans = sol.shortestPath(edges, N, M)
    
    # Output
    print("The shortest distance of every node from source node is:")
    for i in range(N):
        print(ans[i], end=" ")

Complexity Analysis:
Time Complexity: O(N+M)

Creating the graph takes O(M) time.
BFS traversal of graph takes O(N+M) time.
Updating distance of unreachable node takes O(N) time.
Space Complexity: O(N+M)

Storing the graph requires O(M) space.
Visited array takes O(N) space.
The queue space taken during BFS traversal will be O(N) in worst case.

'''
from collections import deque


class Solution:
    def bfs(self, src, adj, dist):
        
        # Distance of source node from itself is zero
        dist[src] = 0 
        
        # Queue to facilitate BFS traversal
        q = deque()
        
        # Adding source node to queue
        q.append(src) 
        
        # Until the queue is empty
        while q:
            
            # Get the node from queue
            node = q.popleft()
            
            # Traverse all its neighbors
            for adjNode in adj[node]:
                
                # If a shorter distance is found
                if dist[node] + 1 < dist[adjNode]:
                    
                    # Update the distance
                    dist[adjNode] = 1 + dist[node]
                    
                    # Add the node to the queue
                    q.append(adjNode)
    
    # Function to get the shortest path 
    # for every node from source node 0
    def shortestPath(self, edges, N, M):
        
        # To store the graph
        adj = [[] for _ in range(N)]
        
        # Add edges to the graph
        for edge in edges:
            u = edge[0] # first node
            v = edge[1] # second node
            
            # Add the edge
            adj[u].append(v)
            adj[v].append(u)
        
        # Distance array to store the shortest paths
        dist = [float('inf')] * N
        
        # Start the BFS traversal from source node
        self.bfs(0, adj, dist)
        
        # If a node is unreachable, 
        # updating its distance to -1
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        # Return the result
        return dist

      