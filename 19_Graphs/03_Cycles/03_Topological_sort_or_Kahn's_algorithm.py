'''
Given a Directed Acyclic Graph (DAG) with V vertices labeled from 0 to V-1.The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Find any Topological Sorting of that Graph.



In topological sorting, node u will always appear before node v if there is a directed edge from node u towards node v(u -> v).



The function should return an array representing the topological order. The output will be validated by our driver code, which checks the correctness of your topological sort. It will print True if the order is valid, otherwise False.


Examples:
Input: V = 6,adj=[ [ ], [ ], [3], [1], [0,1], [0,2] ]







Output: [5, 4, 2, 3, 1, 0]

Explanation: A graph may have multiple topological sortings. 

The result is one of them. The necessary conditions 

for the ordering are:

According to edge 5 -> 0, node 5 must appear before node 0 in the ordering.

According to edge 4 -> 0, node 4 must appear before node 0 in the ordering.

According to edge 5 -> 2, node 5 must appear before node 2 in the ordering.

According to edge 2 -> 3, node 2 must appear before node 3 in the ordering.

According to edge 3 -> 1, node 3 must appear before node 1 in the ordering.

According to edge 4 -> 1, node 4 must appear before node 1 in the ordering.



The above result satisfies all the necessary conditions. 

[4, 5, 2, 3, 1, 0] is also one such topological sorting 

that satisfies all the conditions.

Input: V = 4, adj=[ [ ], [0], [0], [0] ]


Output: [3, 2, 1, 0]

Explanation: The necessary conditions for the ordering are:

For edge 1 -> 0 node 1 must appear before node 0.

For edge 2 -> 0 node 1 must appear before node 0.

For edge 3 -> 0 node 1 must appear before node 0.

Input: V = 3, adj=[[1], [2], []]

Output:
[0, 2, 1]
[2, 1, 0]
[0, 1, 2]
[1. 2. 0]

Submit
Constraints:
 E=number of edges
 1 ≤ V, E ≤ 104

 #DFS Technique

Intuition:
The topological sorting of a directed acyclic graph is nothing but the linear ordering of vertices such that if there is an edge between node u and v(u -> v), node u appears before v in that ordering.
Why does topological sort only exist in DAG?
If the edges are undirected: An undirected edge between node u and v signifies an edge from u to v (u->v) as well as from v to u (v->u) making it practically impossible to write such orderings where u appears before v and v appears before u simultaneously.
If the directed graph contains a cycle: There is no linear ordering possible for nodes in cycles, making it impossible for topological sorting to exist.
Understanding:
Depth-first search (DFS) is a natural fit for this problem because it allows us to explore each path of the graph deeply before backtracking, ensuring that all dependencies of a node are processed before the node itself.
During the DFS traversal, when a node is fully processed (i.e., all nodes it points to are visited), we push it onto a stack.
This stack helps us reverse the order of processing, as nodes deeper in the graph (dependent nodes) are pushed onto the stack first. When we later pop from the stack, we get the nodes in the correct topological order.
Approach:
Prepare a list to store the topological order. Initialize a stack to keep track of the nodes in reverse order of their processing. Create a visited array to track which nodes have been visited.
Define a recursive DFS function that marks the current node as visited. For each neighbor of the current node, if it is not visited, recursively perform DFS on it. After all neighbors are processed, push the current node onto the stack.
Traverse all nodes in the graph. For each unvisited node, initiate a DFS traversal.
Once DFS is complete for all nodes, pop elements from the stack one by one and add them to the topological order list.

class Solution:
    # Function to perform DFS traversal
    def dfs(self, node, adj, vis, st):
        # Mark the node as visited
        vis[node] = 1
        
        # Traverse all the neighbors
        for it in adj[node]:
            
            # If not visited, recursively perform DFS.
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)
        
        # Add the current node to stack 
        # once all the nodes connected to it 
        # have been processed
        st.append(node)
    
    # Function to return list containing 
    # vertices in Topological order
    def topoSort(self, V, adj):
        # To store the result
        ans = []
        
        # Stack to store processed 
        # nodes in reverse order
        st = []
        
        # Visited array
        vis = [0] * V
        
        # Traverse the graph
        for i in range(V):
            
            # Start DFS traversal for unvisited node
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)
        
        # Until the stack is empty
        while st:
            
            # Add the top of stack to result
            ans.append(st.pop())
        
        # Return the result
        return ans

if __name__ == "__main__":
    
    V = 6
    adj = [
        [], 
        [], 
        [3], 
        [1], 
        [0, 1], 
        [0, 2]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to return the 
    # topological sorting of given graph
    ans = sol.topoSort(V, adj)
    
    # Output
    print("The topological sorting of the given graph is:")
    for i in range(V):
        print(ans[i], end=" ")

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represent the number of nodes and edges in the graph)
A simple DFS traversal takes O(V+E) time.

Space Complexity: O(V)
The stack will store at most V nodes taking O(V) space and the array to store the topological sort takes O(V) space.

#BFS (Kahn's Algorithm)

Intuition:
The topological sorting of a directed acyclic graph is nothing but the linear ordering of vertices such that if there is an edge between node u and v(u -> v), node u appears before v in that ordering.
Why does topological sort only exist in DAG?
If the edges are undirected: An undirected edge between node u and v signifies an edge from u to v (u->v) as well as from v to u (v->u) making it practically impossible to write such orderings where u appears before v and v appears before u simultaneously.
If the directed graph contains a cycle: There is no linear ordering possible for nodes in cycles, making it impossible for topological sorting to exist.
To solve the problem using BFS traversal, Kahn's algorithm can be used.
Kahn's Algorithm:
The algorithm suggests that there will always be at least one node having in-degree as zero, which means all such nodes can be put before any other node in the ordering as there is no node pointing to any of these nodes.

After such nodes are added to the ordering, the edges from these nodes can be removed, updating the in-degree of other nodes and exposing more nodes having an in-degree of zero. This process can be repeated till there are nodes left in the graph to get the required linear ordering.
Approach:
Prepare a list to store the topological order. Create an array to track the in-degree (number of incoming edges) of each node. Traverse each node and update the in-degree of its neighbors based on the adjacency list representation of the graph.
Initialize a queue and add all nodes with zero in-degree to it. These nodes have no dependencies and can be processed first.
Use a loop to process nodes from the queue until it is empty:
Remove a node from the front of the queue and add it to the topological order list.
For each neighbor of the removed node, reduce its in-degree by one.
If a neighbor's in-degree becomes zero, all its parent nodes are processed so add it to the queue.
After processing all nodes, the topological order list will contain a valid topological sorting of the graph.

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

if __name__ == "__main__":
    
    V = 6
    adj = [
        [], 
        [], 
        [3], 
        [1], 
        [0,1], 
        [0,2]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to return the 
    # topological sorting of given graph
    ans = sol.topoSort(V, adj)
    
    # Output
    print("The topological sorting of the given graph is:")
    for i in range(V):
        print(ans[i], end=" ")
        
Complexity Analysis:
Time Complexity: O(V+E) (where V and E represent the number of nodes and edges in the graph)
A simple BFS traversal takes O(V+E) time.

Space Complexity: O(V)
Array to store in-degrees require O(V) space and queue space will store O(V) nodes at maximum.


'''
class Solution:
    def dfs(self, node, adj, vis, st):
        vis[node] = 1
        for it in adj[node]:
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)
        st.append(node)
    def topoSort(self, V, adj):
        ans = []
        st = []
        vis = [0] * V
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)
        while st:
            ans.append(st.pop())
        return ans
