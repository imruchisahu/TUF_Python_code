'''
Given an undirected connected graph with V vertices numbered from 0 to V-1, the task is to implement both Depth First Search (DFS) and Breadth First Search (BFS) traversals starting from the 0th vertex. The graph is represented using an adjacency list where adj[i] contains a list of vertices connected to vertex i. Visit nodes in the order they appear in the adjacency list.


Examples:




Input: V = 5, adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output:[0, 2, 4, 3, 1], [0, 2, 3, 1, 4]

Explanation:

DFS: Start from vertex 0. Visit vertex 2, then vertex 4, backtrack to vertex 0, then visit vertex 3, and finally vertex 1. The traversal is 0 → 2 → 4 → 3 → 1.

BFS: Start from vertex 0. Visit vertices 2, 3, and 1 (in the order they appear in the adjacency list). Then, visit vertex 4 from vertex 2. The traversal is 0 → 2 → 3 → 1 → 4.

Input: V = 4, adj = [[1, 3], [2, 0], [1], [0]]

Output: [0, 1, 2, 3], [0, 1, 3, 2]

Explanation:

DFS: Start from vertex 0. Visit vertex 1, then vertex 2, backtrack to vertex 0, then visit vertex 3. The traversal is 0 → 1 → 2 → 3.

BFS: Start from vertex 0. Visit vertices 1 and 3, then visit vertex 2 from vertex 1. The traversal is 0 → 1 → 3 → 2.

Input: V = 3, adj = [[1, 2], [0], [0]]

Output:
[0, 1, 2], [0, 1, 2]
[0, 2, 1], [0, 1, 2]
[0, 1, 2], [0, 2, 1]
[0, 2, 1], [0, 2, 1]

Submit
Constraints:
E= Number of Edges
1 ≤ V, E ≤ 104

# BFS Technique
Intuition:
The traversal techniques form the basics of any graph problem. One of the two traversal techniques is Breadth First Search(BFS), also known as Level Order Traversal. Breadth-First Search (BFS) is a traversal technique that explores all the neighbors of a node before moving to the next level of neighbors. It uses a queue data structure.

Approach:
Mark all nodes as unvisited. Create an empty queue.
Enqueue the source node. Mark the source node as visited.
While the queue is not empty:
Dequeue the front node. Process the node.
For each adjacent unvisited node, enqueue the adjacent node and mark it as visited.
Repeat the process until all nodes are visited.
Solution:
from collections import deque

class Solution:

    # Helper function to perform BFS
    # traversal from the node
    def bfs(self, node, adj, vis, ans):
        # Queue data structure
        q = deque()

        # Push the starting node
        q.append(node)

        # Until the queue is empty
        while q:
            # Get the node
            node = q.popleft()

            # Add the node to answer
            ans.append(node)

            # Traverse for all its neighbours
            for it in adj[node]:
                # If the neighbour has previously not been
                # visited, store in Q and mark as visited
                if not vis[it]:
                    vis[it] = 1
                    q.append(it)

    # Helper function to recursively
    # perform DFS from the node
    def dfs(self, node, adj, vis, ans):
        # Mark the node as visited
        vis[node] = 1

        # Add the node to the result
        ans.append(node)

        # Traverse all its neighbours
        for it in adj[node]:
            # If the neighbour is not visited
            if not vis[it]:
                # Perform DFS recursively
                self.dfs(it, adj, vis, ans)

    # Function to return a list containing
    # the DFS traversal of the graph
    def dfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # Create a list to store DFS
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Call DFS from that node
                self.dfs(i, adj, vis, ans)

        # Return the result
        return ans

    # Function to return a list containing
    # the BFS traversal of the graph
    def bfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # To store the result
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Mark the node as visited
                vis[i] = 1

                # Call BFS from that node
                self.bfs(i, adj, vis, ans)

        return ans


if __name__ == "__main__":
    V = 5
    adj = [
        [2, 3, 1],
        [0],
        [0, 4],
        [0],
        [2]
    ]

    # Creating instance of Solution class
    sol = Solution()

    # Function call to get the BFS traversal of graph
    bfs = sol.bfsOfGraph(V, adj)

    # Function call to get the DFS traversal of graph
    dfs = sol.dfsOfGraph(V, adj)

    # Output
    print("The BFS traversal of the given graph is: ", bfs)
    print("The DFS traversal of the given graph is: ", dfs)


Complexity Analysis:
Time Complexity: O(V+E) (where E represents the number of edges in the graph)
All the V nodes are traversed during the traversal and all the E edges are processed once taking an overall time complexity of O(V+E).

Space Complexity: O(V)
The BFS traversal uses a queue data structure to process the nodes in a level-order fashion. In the worst case, all the nodes will be present in the queue leading to space requirement of O(V).



#DFS Technique
Intuition:
The traversal techniques form the basics of any graph problem. One of the two traversal techniques is Depth First Search(DFS). Depth-First Search (DFS) is a traversal technique that explores as far as possible along each branch before backtracking. It uses a stack data structure, either explicitly or implicitly through recursion.

Approach:
Mark all nodes as unvisited. Create an empty stack or use recursion.
Push the source node onto the stack (or call the recursive function with the source node). Mark the source node as visited.
While the stack is not empty:
Pop the top node from the stack. For each adjacent unvisited node, push the adjacent node onto the stack (or call the recursive function with the adjacent node).
Mark the adjacent node as visited.
Repeat the process until all nodes are visited.
Dry Run:
 
Solution:
from collections import deque

class Solution:

    # Helper function to perform BFS
    # traversal from the node
    def bfs(self, node, adj, vis, ans):
        # Queue data structure
        q = deque()

        # Push the starting node
        q.append(node)

        # Until the queue is empty
        while q:
            # Get the node
            node = q.popleft()

            # Add the node to answer
            ans.append(node)

            # Traverse for all its neighbours
            for it in adj[node]:
                # If the neighbour has previously not been
                # visited, store in Q and mark as visited
                if not vis[it]:
                    vis[it] = 1
                    q.append(it)

    # Helper function to recursively
    # perform DFS from the node
    def dfs(self, node, adj, vis, ans):
        # Mark the node as visited
        vis[node] = 1

        # Add the node to the result
        ans.append(node)

        # Traverse all its neighbours
        for it in adj[node]:
            # If the neighbour is not visited
            if not vis[it]:
                # Perform DFS recursively
                self.dfs(it, adj, vis, ans)

    # Function to return a list containing
    # the DFS traversal of the graph
    def dfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # Create a list to store DFS
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Call DFS from that node
                self.dfs(i, adj, vis, ans)

        # Return the result
        return ans

    # Function to return a list containing
    # the BFS traversal of the graph
    def bfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # To store the result
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Mark the node as visited
                vis[i] = 1

                # Call BFS from that node
                self.bfs(i, adj, vis, ans)

        return ans


if __name__ == "__main__":
    V = 5
    adj = [
        [2, 3, 1],
        [0],
        [0, 4],
        [0],
        [2]
    ]

    # Creating instance of Solution class
    sol = Solution()

    # Function call to get the BFS traversal of graph
    bfs = sol.bfsOfGraph(V, adj)

    # Function call to get the DFS traversal of graph
    dfs = sol.dfsOfGraph(V, adj)

    # Output
    print("The BFS traversal of the given graph is: ", bfs)
    print("The DFS traversal of the given graph is: ", dfs)

Complexity Analysis:
Time Complexity: O(V+E) (where E represents the number of edges in the graph)
All the V nodes are traversed during the traversal and all the E edges are processed once taking an overall time complexity of O(V+E).

Space Complexity: O(V)
The DFS traversal uses a stack data structure or recursive stack space to process the nodes in a depth-first fashion. In the worst case, all the nodes will be present in the stack leading to space requirement of O(V).

'''
from collections import deque


class Solution:
    def bfs(self, node, adj, vis, ans):
        # Queue data structure
        q = deque()

        # Push the starting node
        q.append(node)

        # Until the queue is empty
        while q:
            # Get the node
            node = q.popleft()

            # Add the node to answer
            ans.append(node)

            # Traverse for all its neighbours
            for it in adj[node]:
                # If the neighbour has previously not been
                # visited, store in Q and mark as visited
                if not vis[it]:
                    vis[it] = 1
                    q.append(it)

    # Helper function to recursively
    # perform DFS from the node
    def dfs(self, node, adj, vis, ans):
        # Mark the node as visited
        vis[node] = 1

        # Add the node to the result
        ans.append(node)

        # Traverse all its neighbours
        for it in adj[node]:
            # If the neighbour is not visited
            if not vis[it]:
                # Perform DFS recursively
                self.dfs(it, adj, vis, ans)

    def dfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # Create a list to store DFS
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Call DFS from that node
                self.dfs(i, adj, vis, ans)

        # Return the result
        return ans
    
    def bfsOfGraph(self, V, adj):
        # Visited array
        vis = [0] * V

        # To store the result
        ans = []

        # Traverse all the nodes
        for i in range(V):
            # If the node is unvisited
            if vis[i] == 0:
                # Mark the node as visited
                vis[i] = 1

                # Call BFS from that node
                self.bfs(i, adj, vis, ans)

        return ans