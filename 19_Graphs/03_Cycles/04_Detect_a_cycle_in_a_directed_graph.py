'''
Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any cycles.


Examples:
Input: V = 6, adj= [ [1], [2, 5], [3], [4], [1], [ ] ]







Output: True



Explanation: The graph contains a cycle: 1 -> 2 -> 3 -> 4 -> 1.

Input: V = 4, adj= [[1,2], [2], [], [0,2]]



Output: False



Explanation: The graph does not contain a cycle.

Input: V = 3, adj= [[1], [2], [0]]

Output:
True
False

Submit
Constraints:
  E=number of edges
  1 ≤ V, E ≤ 104

#DFS Techniques
Intuition:
In a Directed Cyclic Graph, during traversal, if we end up at a node, that we have visited previously in the path, that means we came around a circle and ended up at this node, which determines that it has a cycle. However, detecting cycles using DFS in directed graphs requires a different approach than in undirected graphs due to the nature of directed edges.

Understanding:
In undirected graphs, detecting cycles involves checking if a visited node is not the parent of the current node. On the other hand, in directed graphs, simply finding a previously visited node isn't enough because it might have been visited via a different path.
To accurately detect cycles in a directed graph, we need to track nodes within the current path of the DFS traversal. This means maintaining a path array to keep track of nodes in the current DFS path.
If we encounter a node that is already in the current DFS path (recursion stack), it indicates a cycle. If a node is visited but not in the current DFS path, it doesn’t necessarily indicate a cycle.
Approach:
A helper function performs DFS, where during the traversal, the nodes are marked as visited and path visited.
During the traversal, the cycles are checked by detecting if a node is revisited in the current path. Unmarks the node in the path visited array after exploration.
Traverse all the components in the graph to detect the cycle. If any of the components contains a cycle, return true. Otherwise, if no cycle is detected, return false.

class Solution:
    # Function to perform DFS traversal
    def dfs(self, node, adj, visited, pathVisited):
        # Mark the node as path visited
        visited[node] = True
        
        # Mark the node as path visited
        pathVisited[node] = True
        
        # Traverse all the neighbors
        for it in adj[node]:
            
            # If the neighbor is already visited 
            # in the path, a cycle is detected
            if pathVisited[it]:
                return True
            
            # Else if the node is unvisited, 
            # perform DFS recursively from this node
            elif not visited[it]:
                
                # If cycle is detected, return true
                if self.dfs(it, adj, visited, pathVisited):
                    return True
        
        # Remove the node from path 
        pathVisited[node] = False
        
        # Return false if no cycle is detected
        return False

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        
        # Visited array
        visited = [False] * V
        
        # Array to mark nodes that are 
        # visited in a particular path
        pathVisited = [False] * V
        
        # Traverse the graph
        for i in range(V):
            if not visited[i]:
                
                # If a cycle is found, return true
                if self.dfs(i, adj, visited, pathVisited):
                    return True
        
        # Return false if no cycle is 
        # detected in any component
        return False

if __name__ == "__main__":
    
    V = 6
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[1].extend([2, 5])
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(1)
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to determine if cycle 
    # exists in given directed graph
    ans = sol.isCyclic(V, adj)
    
    # Output
    if ans:
        print("The given directed graph contains a cycle.")
    else:
        print("The given directed graph does not contain a cycle.")

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represent the number of nodes and edges in the graph)
A simple DFS traversal takes O(V+E) time.

Space Complexity: O(V)
The visited array and Path Visited array take O(V) space each and the recursion stack space during DFS traversal will be O(V).



#BFS Techniques
Intuition:
To solve this problem using BFS traversal, the previously known algorithm Topological Sort can be used.

Recall that Topological Ordering for a graph having V nodes can be determined if and only the graph is a Directed Acyclic Graph, i.e., there must be no cycle present in the directed graph. In other words, the topological ordering of a DAG consisting of V nodes will always contain V nodes.

But this is not true in the case of a Directed Cyclic Graph. In such a graph where the number of nodes is V, the topological ordering will not contain all nodes (because of the presence of a cycle).

Thus, if the topological sort of the directed graph contains all nodes of the graph, then the graph is acyclic otherwise it is cyclic.

Approach:
A helper function is defined to get the topological sort for the given graph using Kahn's algorithm (BFS based).
The topological ordering for the given directed graph is found using the helper function.
If the ordering contains all nodes, the directed graph is cyclic. Otherwise it is acyclic.

from collections import deque

class Solution:
    # Function to return the topological 
    # sorting of given graph
    def topoSort(self, V, adj):
        # To store the result
        ans = []
        
        # To store the In-degrees of nodes
        inDegree = [0] * V
        
        # Calculating the In-degree of the given graph
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1
        
        # Queue to facilitate BFS
        q = deque()
        
        # Add the nodes with no in-degree to queue
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        
        # Until the queue is empty
        while q:
            # Get the node
            node = q.popleft()
            
            # Add it to the answer
            ans.append(node)
            
            # Traverse the neighbours
            for it in adj[node]:
                # Decrement the in-degree
                inDegree[it] -= 1
                
                # Add the node to queue if 
                # its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)
        
        # Return the result
        return ans

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # To store the topological ordering
        topo = self.topoSort(V, adj)
        
        # If topological sort doesn't include all
        # nodes, the graph is cyclic in nature
        if len(topo) < V:
            return True
        
        # Else the graph is acyclic
        return False

if __name__ == "__main__":
    V = 6
    adj = [[] for _ in range(V)]
    
    adj[0].append(1)
    adj[1].extend([2, 5])
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(1)
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to determine if cycle exists in given directed graph
    ans = sol.isCyclic(V, adj)
    
    # Output
    if ans:
        print("The given directed graph contains a cycle.")
    else:
        print("The given directed graph does not contain a cycle.")

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represent the number of nodes and edges in the graph)
Topological Sort based on BFS (Kahn's Algorithm) takes O(V+E) time.

Space Complexity: O(V)
Array required to store in-degrees takes up O(V) space and queue space will be O(V) in the worst case.

'''
class Solution:
    def dfs(self, node, adj, visited, pathVisited):
        visited[node] = True
        pathVisited[node] = True
        for it in adj[node]:
            if pathVisited[it]:
                return True
            elif not visited[it]:
                if self.dfs(it, adj, visited, pathVisited):
                    return True
        pathVisited[node] = False
        return False

    def isCyclic(self, V, adj):
        visited = [False] * V
        
        # Array to mark nodes that are 
        # visited in a particular path
        pathVisited = [False] * V

        for i in range(V):
            if not visited[i]:
                if self.dfs(i, adj, visited, pathVisited):
                    return True
        return False
    