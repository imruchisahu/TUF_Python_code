'''

Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes adjacent to node i, meaning there is an edge from node i to each node in adj[i]. A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node. Return an array containing all the safe nodes of the graph in ascending order.


Examples:
Input: V = 7, adj= [[1,2], [2,3], [5], [0], [5], [], []]

Output: [2, 4, 5, 6]

Explanation: 

From node 0: two paths are there 0->2->5 and 0->1->3->0. 

The second path does not end at a terminal node. So it is not 

a safe node.

From node 1: two paths exist: 1->3->0->1 and 1->2->5.

But the first one does not end at a terminal node. So it is not a safe node.

From node 2: only one path: 2->5 and 5 is a terminal node.

So it is a safe node.

From node 3: two paths: 3->0->1->3 and 3->0->2->5 

but the first path does not end at a terminal node. 

So it is not a safe node.

From node 4: Only one path: 4->5 and 5 is a terminal node. 

So it is also a safe node.

From node 5: It is a terminal node. 

So it is a safe node as well.

From node 6: It is a terminal node. 

So it is a safe node as well.

Input: V = 4, adj= [[1], [2], [0,3], []]

Output: [3]

Explanation: Node 3 itself is a terminal node and it is a safe node as well. But all the paths from other nodes do not lead to a terminal node.So they are excluded from the answer.

Input: V = 4, adj= [[1], [2], [0], []]

Output:
[]
[1, 2]
[0]
[3]

Submit
Constraints:
  V == adj.length
  1 <= V <= 104
  0 <= adj[i].length <= n
  0 <= adj[i][j] <= n - 1
  adj[i] is sorted in a strictly increasing order.
  The graph may contain self-loops.
  The number of edges in the graph will be in the range [1, 4 * 104].

  #DFS Techniques
  Intuition:
It can be observed that all possible paths starting from a node are going to end at some terminal node unless there exists a cycle and the paths return back to themselves.

Understanding:
Consider the below graph:



It is clear that these types of nodes will never be considered safe:
One is which are occuring in a cycle. Example: Nodes 0, 1 and 3.
Second is which are leading to a cycle. Example: Node 7.

Except these types of nodes, all other nodes will be considered eventually safe.
Hence in order to find the safe nodes, the unsafe nodes can be detected by checking if they exist or point to a cycle. Now, a cycle detection technique is already known to us as discussed in detect cycles in a Directed graph (Using DFS).

Approach:
Initialize three arrays to keep track of visited nodes, nodes in the current traversal path, and nodes identified as safe. Each node starts as unvisited and is considered potentially unsafe until proven otherwise.
Perform a DFS from each node that has not been visited yet. During the DFS traversal, mark the current node as visited and add it to the current path. Assume the current node is unsafe initially.
For each adjacent node of the current node:
If the adjacent node is unvisited, recursively perform DFS on it.
If the adjacent node is in the current path, a cycle is detected, making the node unsafe.
If any adjacent node leads to a cycle, the current node remains marked as unsafe.
If no cycles are detected from the current node and its paths, mark the current node as safe. Remove the current node from the path, as the DFS for this node is complete.
After the entire graph is traversed, gather all nodes marked as safe and return the result.
Solution:
from typing import List

class Solution:
    
    # Function to perform DFS traversal 
    # while checking for safe nodes
    def dfsCheck(self, node: int, adj: List[List[int]], 
                 vis: List[bool], 
                 pathVis: List[bool], 
                 check: List[bool]) -> bool:
                      
        # Mark the node as visited
        vis[node] = True
        
        # Add the node to current path
        pathVis[node] = True
        
        # Mark the node as potentially unsafe
        check[node] = False
        
        # Traverse for adjacent nodes
        for it in adj[node]:
            
            # When the node is not visited
            if not vis[it]:
                
                # Perform DFS recursively and if 
                # a cycle is found, return false
                if self.dfsCheck(it, adj, vis, pathVis, check):
                    
                    # Return true since a 
                    # cycle was detected
                    return True

            # Else if the node has been previously 
            # visited in the same path
            elif pathVis[it]:
                
                # Return true since a 
                # cycle was detected
                return True
        
        # If the current node neither exist 
        # in a cycle nor points to a cycle, 
        # it can be marked as a safe node
        check[node] = True
        
        # Remove the node from the current path
        pathVis[node] = False
        
        # Return false since no cycle was found
        return False

    # Function to get the eventually safe nodes
    def eventualSafeNodes(self, V, adj):
        
        # Visited array
        vis = [False] * V
        
        # Path Visited array
        pathVis = [False] * V
        
        # To keep a check of safe nodes
        check = [False] * V
        
        # Traverse the graph and 
        # check for safe nodes
        for i in range(V):
            if not vis[i]:
                
                # Start DFS traversal
                self.dfsCheck(i, adj, vis, pathVis, check)
        
        # To store the result
        ans = []
        
        # Add the safe nodes to the result
        for i in range(V):
            if check[i]:
                ans.append(i)
        
        # Return the result
        return ans

# Main function
if __name__ == "__main__":
    
    V = 7
    adj = [
         [1,2],
         [2,3],
         [5],
         [0],
         [5],
         [],
         []
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution() 
    
    # Function call to get the eventually 
    # safe nodes in the given graph
    ans = sol.eventualSafeNodes(V, adj)
    
    # Output
    print("The eventually safe nodes in the graph are:")
    for node in ans:
        print(node, end=" ")

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represents the number of nodes and edges in the given graph)
DFS traversal takes O(V+E) time and adding the safe nodes to the result takes O(V) time.

Space Complexity: O(V)
The visited, path visited, and check array take O(V) space each and the recursion stack space will be O(V) in the worst case.



#BFS Technique
Intuition:
It can be observed that all possible paths starting from a node are going to end at some terminal node unless there exists a cycle and the paths return back to themselves.

Understanding:
Consider the below graph:



It is clear that these types of nodes will never be considered safe:
One is which is occurring in a cycle. Example: Nodes 0, 1, and 3.
Second is which is leading to a cycle. Example: Node 7.

Except these types of nodes, all other nodes will be considered eventually safe.
Hence in order to find the safe nodes, the unsafe nodes can be detected by checking if they exist or point to a cycle. Now, to solve this using BFS traversal technique, the topological sorting (Kahn's Algorithm) can be used. The topological sort algorithm will automatically exclude the nodes which are either forming a cycle or connected to a cycle.

Transforming the graph:
The node with outdegree 0 is considered as terminal node but the topological sort algorithm deals with the indegrees of the nodes. So, to use the topological sort algorithm, we will reverse every edge of the graph.


Approach:
Reverse the edges of the graph reversing the graph.
Find the topological sort of the reversed graph which will exclude automatically the unsafe nodes.
Sort the ordering returned by topological sort to obtain the eventually safe nodes in a sorted fashion.
Solution:
from collections import deque

class Solution:

    # Function to return the topological
    # sorting of given graph
    def topoSort(self, V, adj):
        
        # To store the In-degrees of nodes
        inDegree = [0] * V
        
        # Update the in-degrees of nodes
        for i in range(V):
            
            for it in adj[i]:
                # Update the in-degree
                inDegree[it] += 1

        # To store the result
        ans = []
        
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

    # Function to get the
    # eventually safe nodes
    def eventualSafeNodes(self, V, adj):
        
        # To store the reverse graph
        adjRev = [[] for _ in range(V)]
        
        # Reversing the edges
        for i in range(V):
            
            # i -> it, it-> i
            for it in adj[i]:
                
                # Add the edge to reversed graph
                adjRev[it].append(i)
        
        # Return the topological 
        # sort of the given graph
        result = self.topoSort(V, adjRev)
        
        # Sort the result
        result.sort()
        
        # Return the result
        return result

# Example usage
V = 7
adj = [
    [1, 2],
    [2, 3],
    [5],
    [0],
    [5],
    [],
    []
]

sol = Solution()
ans = sol.eventualSafeNodes(V, adj)

# Output
print("The eventually safe nodes in the graph are:")
print(" ".join(map(str, ans)))

Complexity Analysis:
Time Complexity: O(V+E) + O(V*logV) (where V and E represents the number of nodes and edges in the given graph)
Reversing the graph takes O(E) time.
Finding topological sort using Kahn's algorithm takes O(V+E) time.
Sorting the nodes takes O(N*logN) time (where N is the number of safe nodes, which can go up to V in worst-case).
Space Complexity: O(V+E)
Storing the reversed graph takes O(E) space.
Topological sorting algorithm uses extra O(V) space because of in-degrees array and queue data structure.

'''
from typing import List


class Solution:
    def dfsCheck(self, node: int, adj: List[List[int]], 
                 vis: List[bool], 
                 pathVis: List[bool], 
                 check: List[bool]) -> bool:
        vis[node] = True
        pathVis[node] = True
        check[node] = False
        for it in adj[node]:
            if not vis[it]:
                if self.dfsCheck(it, adj, vis, pathVis, check):
                    return True
            elif pathVis[it]:
                return True
        check[node] = True
        pathVis[node] = False
        return False
    def eventualSafeNodes(self, V, adj):
        vis = [False] * V
        pathVis = [False] * V
        check = [False] * V
    
        for i in range(V):
            if not vis[i]:
                self.dfsCheck(i, adj, vis, pathVis, check)
        ans = []
        for i in range(V):
            if check[i]:
                ans.append(i)
        return ans