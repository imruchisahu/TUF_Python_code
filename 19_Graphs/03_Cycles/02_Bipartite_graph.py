'''
Given an undirected graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph is bipartite or not.



A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.


Examples:
Input: V=4, adj = [[1,3],[0,2],[1,3],[0,2]]



Output: True

Explanation: The given graph is bipartite since, we can partition the nodes into two sets: {0, 2} and {1, 3}.

Input: V=4, adj = [[1,2,3],[0,2],[0,1,3],[0,2]]

Output: False

Explanation: The graph is not bipartite. If we attempt to partition the nodes into two sets, we encounter an edge that connects two nodes within the same set, which violates the bipartite property.

Input: V=5, adj = [[1,3],[0,2],[1,4],[0,4],[2,3]]

Output:
True
False

Submit
Constraints:
E=number of edges
1 ≤ V, E ≤ 104

#BFS Technique
Intuition:
A bipartite graph is a graph that can be colored using 2 colors such that no adjacent nodes have the same color. Any linear graph with no cycle is always a bipartite graph. With a cycle, any graph with an even cycle length can also be a bipartite graph. So, any graph with an odd cycle length can never be a bipartite graph.

To check if the graph is bipartite, it can check if the nodes can be colored alternatingly. If alternate coloring of nodes is possible, the graph is bipartite, else not.

Approach:
Initialize a color array with all nodes initially uncolored represented by -1. Green and Yellow colors will be represented as integer value 0 and 1 respectively.
Start the BFS traversal from an unvisited node and perform the following steps:
If a node is uncolored, color it with alternating colors.
If a node is previously colored, check if it follows alternate colors. If not, the graph can be said as not bipartite.
If all the nodes can be colored with alternating colors, the graph can be classified as bipartite.

from collections import deque

class Solution:
    
    # Function to perform BFS traversal and color
    # the nodes with alternate colors in a component
    def bfs(self, start, V, adj, color):
        # Queue for BFS traversal
        q = deque()
        
        # Add initial node to queue
        q.append(start)
        color[start] = 0 # Mark it with a color
        
        # While queue is not empty
        while q:
            # Get the node
            node = q.popleft()
            
            # Traverse all its neighbors
            for it in adj[node]:
                
                # If not already colored
                if color[it] == -1:
                    
                    # Color it with opposite color.
                    color[it] = 1 - color[node]
                    
                    # Push the node in queue
                    q.append(it)
                
                # Else if the neighbor has same color as node
                elif color[it] == color[node]:
                    
                    # Return false, as the 
                    # component is not bipartite
                    return False
        
        # Return true if the component is bipartite
        return True
    
    # Function to check if the 
    # given graph is bipartite
    def isBipartite(self, V, adj):
        
        # To store the color of nodes, where 
        # each node is uncolored initially
        color = [-1] * V
        
        # Traverse all the nodes 
        for i in range(V):
            
            # If not colored, start the traversal
            if color[i] == -1:
                # Return false if graph is not bipartite
                if not self.bfs(i, V, adj, color):
                    return False
        
        # Return true if each 
        # component is bipartite
        return True

if __name__ == "__main__":
    
    V = 4
    adj = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to check 
    # if the given graph is bipartite
    ans = sol.isBipartite(V, adj)
    
    # Output
    if ans:
        print("The given graph is a bipartite graph.")
    else:
        print("The given graph is not a bipartite graph.")

Complexity Analysis:
Time Complexity: O(V+E) (where V is the number of nodes and E is the number of edges in the graph)
The BFS Traversal takes O(V+E) time.

Space Complexity: O(V)
The color array takes O(V) space and queue space for BFS is O(V) for the worst case.

#DFS Technique
Intuition:
A bipartite graph is a graph that can be colored using 2 colors such that no adjacent nodes have the same colour. Any linear graph with no cycle is always a bipartite graph. With a cycle, any graph with an even cycle length can also be a bipartite graph. So, any graph with an odd cycle length can never be a bipartite graph.

In order to check if the given graph is bipartite, it can checked if the nodes can be colors alternatingly. If alternate coloring of nodes is possible, the graph is bipartite, else not.

Approach:
Initialize a color array with all nodes initially uncolored represented by -1. Green and Yellow colors will be represented as integer value 0 and 1 respectively.
Start the DFS traversal from the node and perform the following steps:
If a node is uncolored, color it with alternating colors.
If a node is previously colored, check if it follows alternate colors. If not, the graph can be said as not bipartite.
If all the nodes can be colored with alternating colors, the graph can be classified as bipartite.

class Solution:
    
    # Function to perform DFS traversal and 
    # color the nodes with alternate colors
    def dfs(self, node, col, color, adj):
        
        # Color the current node
        color[node] = col
        
        # Traverse adjacent nodes
        for it in adj[node]:
            
            # if uncoloured
            if color[it] == -1:
                
                # Recursively color the nodes 
                if not self.dfs(it, 1 - col, color, adj):
                    return False
                    
            # if previously coloured and have the same colour
            elif color[it] == col:
                
                # Return false as it is not bipartite
                return False
        
        # Return true if all the nodes can 
        # be colored with alternate colors
        return True

    # Function to check if the given graph is bipartite
    def isBipartite(self, V, adj):
        
        # To store the color of nodes, where 
        # each node is uncolored initially
        color = [-1] * V
        
        # Start Traversal of connected components
        for i in range(V):
            
            # if a node is not colored, 
            # a new component is found
            if color[i] == -1:
                
                # Start DFS traversal 
                # and color each node
                if not self.dfs(i, 0, color, adj):
                    
                    # Return false if component 
                    # is found not to be bipartite
                    return False
        
        # Return true if each 
        # component is bipartite
        return True

if __name__ == "__main__":
    V = 4
    adj = [[] for _ in range(V)]
    adj[0].extend([1, 3])
    adj[1].extend([0, 2])
    adj[2].extend([1, 3])
    adj[3].extend([0, 2])

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to check if the given graph is bipartite
    ans = sol.isBipartite(V, adj)

    # Output
    if ans:
        print("The given graph is a bipartite graph.")
    else:
        print("The given graph is not a bipartite graph.")

Complexity Analysis:
Time Complexity: O(V+E) (where V is the number of nodes and E is the number of edges in the graph.)
The DFS Traversal takes O(V+E) time.

Space Complexity: O(V)
The color array takes O(V) space and recursion stack space for DFS is O(V) for the worst case.

'''
from collections import deque


class Solution:
    def bfs(self, start, V, adj, color):
        # Queue for BFS traversal
        q = deque()
        q.append(start)
        color[start] = 0
        
        # While queue is not empty
        while q:
            node = q.popleft()
            for it in adj[node]:
                
                # If not already colored
                if color[it] == -1:
                    color[it] = 1 - color[node]
                    q.append(it)
                elif color[it] == color[node]:
                    return False
        return True
    def isBipartite(self, V, adj):
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if not self.bfs(i, V, adj, color):
                    return False
        return True
        