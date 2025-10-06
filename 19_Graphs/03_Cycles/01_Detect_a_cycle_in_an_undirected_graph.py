'''

Given an undirected graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any cycles.

Note: The graph does not contain any self-edges (edges where a vertex is connected to itself).

Examples:

Input: V = 6, adj= [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

Output: True

Explanation: The graph contains a cycle: 0 ->1 -> 2 -> 5 -> 4 -> 1.

Input: V = 4, adj= [[1, 2], [0], [0, 3], [2]]

Output: False

Explanation: The graph does not contain any cycles.

Input: V = 4, adj= [[1, 2], [0, 2], [0, 1, 3], [2]]

Output:
True
False

Submit
Constraints:
E=number of edges
1 ≤ V, E ≤ 104

#BFS Techniques
Intuition:
In an undirected graph, a cycle is formed when a path exists that returns to the starting vertex without reusing an edge. The key idea is that during traversal (e.g., using Breadth-First Search (BFS) for this approach), if we encounter a vertex that has already been visited and is not the immediate parent of the current vertex, a cycle exists.

Approach:
A helper function performs BFS to detect cycles, using a queue to track nodes and their parents. For each unvisited node, initialize the queue with the node and mark it as visited.
While the queue is not empty, process each node's neighbors:
If a neighbor is unvisited, mark it visited and enqueue it.
If a neighbor is visited and not the parent, a cycle is detected.
Return true if any cycle is found during traversal.

from collections import deque

class Solution:
    
    # Function to perform BFS traversal
    def bfs(self, i, adj, visited):
        # Queue to store (node, parent)
        q = deque()
        
        # Push initial node in queue 
        # with no one as parent
        q.append((i, -1))
        
        # Mark the node as visited
        visited[i] = True
        
        # Until the queue is empty
        while q:
            # Get the node and its parent
            node, parent = q.popleft()
            
            # Traverse all the neighbors
            for it in adj[node]:
                # If not visited
                if not visited[it]:
                    # Mark the node as visited
                    visited[it] = True
                    
                    # Push the new node in queue 
                    # with curr node as parent
                    q.append((it, node))
                    
                # Else if it is visited with some 
                # different parent a cycle is detected
                elif it != parent:
                    return True
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        visited = [False] * V
        ans = False
        
        # Start Traversal from every unvisited node
        for i in range(V):
            if not visited[i]:
                # Start BFS traversal and update result
                ans = self.bfs(i, adj, visited)
                
                # Break if a cycle is detected
                if ans:
                    break
        return ans

if __name__ == "__main__":
    V = 6
    adj = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to detect cycle in given graph.
    ans = sol.isCycle(V, adj)
    
    # Output
    if ans:
        print("The given graph contains a cycle.")
    else:
        print("The given graph does not contain a cycle.")

Complexity Analysis:
Time Complexity: O(V + E)
(where V is the number of nodes and E is the number of edges in the graph)
Traversing the complete graph overall which taken O(V+E) time.

Space Complexity: O(V)
Visited array takes O(V) space and in the worst case queue will store all nodes taking O(V) space.

#DFS Techniques
Intuition:
In an undirected graph, a cycle is formed when a path exists that returns to the starting vertex without reusing an edge. The key idea is that during traversal (e.g., using Depth-First Search (DFS) for this approach), if we encounter a vertex that has already been visited and is not the immediate parent of the current vertex, a cycle exists.

Approach:
A helper function performs DFS to detect cycles, keeping track of nodes and their parents. For each unvisited node, initialize the mark the node as visited.
Traverse the neighbors of the node:
If a neighbor is unvisited, mark it visited and recursively perform DFS from it.
If a neighbor is visited and not the parent, a cycle is detected.
Return true if any cycle is found during traversal.

class Solution:
    
    # Function to perform DFS traversal
    def dfs(self, i, adj, visited, prev):
        # Mark the node as visited
        visited[i] = True
        
        # Traverse all the neighbors
        for node in adj[i]:
            
            # If not visited
            if not visited[node]:
                
                # Recursively perform DFS, and 
                # return true if cycle is found
                if self.dfs(node, adj, visited, i):
                    return True
                    
            # Else if it is visited with some 
            # different parent a cycle is detected
            elif node != prev:
                return True
        
        # Return false if no cycle is detected
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Visited array
        visited = [False] * V
        
        # Start Traversal from every unvisited node
        for i in range(V):
            if not visited[i]:
                
                # Start DFS traversal, and 
                # return true if cycle is found
                if self.dfs(i, adj, visited, -1):
                    return True
        
        # Return false if no cycle is detected
        return False

if __name__ == "__main__":
    V = 6
    adj = [
        [1, 3], 
        [0, 2, 4], 
        [1, 5], 
        [0, 4], 
        [1, 3, 5], 
        [2, 4]
    ]
    
    #Creating an instance of Solution class 
    sol = Solution()
    
    #Function call to detect cycle in given graph. 
    ans = sol.isCycle(V, adj)
    
    # Output
    if ans: 
        print("The given graph contains a cycle.")
    else: 
        print("The given graph does not contain a cycle.")

Complexity Analysis:
Time Complexity: O(V + E)
(where V is the number of nodes and E is the number of edges in the graph)
Traversing the complete graph overall which taken O(V+E) time.

Space Complexity: O(V)
Visited array takes O(V) space and in the worst case recursion stack will store O(V) calls taking O(V) space.

'''
from collections import deque
class Solution:
    def bfs(self, i, adj, visited):
        q = deque()
        q.append((i, -1))
        visited[i] = True
        while q:
            node, parent = q.popleft()
            for it in adj[node]:
                if not visited[it]:
                    visited[it] = True
                    q.append((it, node))
                elif it != parent:
                    return True
        return False
    def isCycle(self, V, adj):
        visited = [False] * V
        ans = False
        
        # Start Traversal from every unvisited node
        for i in range(V):
            if not visited[i]:
                ans = self.bfs(i, adj, visited)
                if ans:
                    break
        return ans