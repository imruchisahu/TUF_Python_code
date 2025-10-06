'''
Given an undirected graph with V vertices and adjacency list adj. Find all the vertices removing which (and edges through it) would increase the number of connected components in the graph. The graph may be initially disconnected.. Return the vertices in ascending order. If there are no such vertices then returns a list containing -1.



Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.


Examples:




Input: V = 7, adj=[[1,2,3], [0], [0,3,4,5], [2,0], [2,6], [2,6], [4,5]] 

Output: [0, 2]

Explanation: If we remove node 0 or node 2, the graph will be divided into 2 or more components.





Input: V = 5, adj=[[1], [0,4], [3,4], [2,4], [1,2,3]] 

Output: [1, 4]

Explanation: If we remove either node 1 or node 4, the graph breaks into multiple components.

Input: V = 3, adj=[[1,2], [0,2], [0,1]]

Output:
[1, 2]
[1]
[2. 3]
[-1]

Submit
Constraints:
E= Number of Edges
1 ≤ V, E ≤ 104

Intuition:
A vertex of a graph is called a Articulation point when the component is divided into 2 or more components if that particular vertex is removed. Removing a vertex means to also remove all the edges that share the vertex.

Example:
Consider the following graph:  For the above graph node 0 and node, 2 are the articulation points. If either of the two nodes is removed, the graph breaks into multiple components like the following: 

Note that node 3 is not an articulation point as its removal does not break the graph into multiple components. To solve this problem, a modified depth-first search (DFS) will use used along with the concept of discovery and low times for nodes.
Understanding:
Before moving to the algorithm, it is important to know about the two arrays that play a crucial role in the algorithm:
Discovery time / Time of insertion Array: During the DFS call, the time when a node is visited first (discovered first), is called its time of insertion or discovery time. This array will store the discovery times of the nodes.
Usage: It helps keep track of when each node was first visited. This value is unique and incremental, meaning it increases as the DFS progresses.
Lowest time of insertion Array: In this case, the current node refers to all its adjacent nodes except the parent and the visited nodes and takes the minimum lowest time of insertion into account. This array stores the lowest time of insertion for all nodes.
Usage: It helps determine whether a node can reach an ancestor via a back edge, which is essential for identifying articulation points.
To find out the bridges in the bridge problem, checks were made inside the DFS, if there exists any alternative path from the adjacent node to the current node. But here the same cannot be done as in this case, we are trying to remove the current node along with all the edges linked to it.

For that reason, here a check will be made if there exists any path from the adjacent node to the previous node of the current node. In addition to that, it must be ensured that the current node that we are trying to remove must not be the starting node.
How the two arrays help in identifying the bridges in a graph?
Consider two nodes, node u and node v, where v is the neighbor of u. Let us assume that tin[u] represents the discovery time of node u and low[v] represents the lowest discovery time reachable from node v.

If low[v] >= tin[u]:
It means that the subtree rooted at it cannot reach any node that was discovered before node (except through node). Therefore, if node is removed, the subtree rooted at it would be disconnected from the rest of the graph.

Thus, when the DFS calls to the descendants are completed, this condition can be checked to identify the articulation points.
Edge Cases:
Consider the following graph: 

In the following graph, the starting node 0 has two adjacent nodes, but it is not an articulation point. To avoid this edge case, the number of children must be incremented only if the adjacent node is not previously visited.

Note: A single node can be found as the articulation point multiple times. Thus, To avoid the storing of duplicate nodes, the nodes will be stored in a hash array instead of directly inserting them in a simple array.

Approach:
Prepare arrays to keep track of visited nodes, discovery times, low values (the lowest discovery time reachable), and articulation point markers. Initialize a timer to record the discovery times.
Perform a DFS traversal for each unvisited node. Mark the current node as visited and set its discovery and low values to the current timer value, then increment the timer.
Traverse all adjacent nodes of the current node. If an adjacent node is not visited, recursively perform DFS for that node. After returning from the DFS call, update the low value of the current node.
Check if the current node is an articulation point based on the conditions involving low and discovery values. If true, mark it as an articulation point.
If the current node is the root of the DFS tree and has more than one child, mark it as an articulation point. After the DFS traversal, compile a list of all marked articulation points.
Return the list of articulation points in ascending order. If no articulation points are found, return -1.

class Solution:
    
    def __init__(self):
        # To store the current time during traversal
        self.timer = 1

    # Helper function to make DFS calls while 
    # identifying articulation points
    def dfs(self, node, parent, vis, tin, low, mark, adj):

        # Mark the node as visited
        vis[node] = True

        # Time of insertion and the lowest time of 
        # insert for node will be the current time 
        tin[node] = low[node] = self.timer

        # Increment the timer
        self.timer += 1

        # To count the number of children of the node
        child = 0

        # Traverse all its neighbor
        for it in adj[node]:

            # Skip the parent
            if it == parent:
                continue

            # If a neighbor is not visited
            if not vis[it]:

                # Make a recursive DFS call
                self.dfs(it, node, vis, tin, low, mark, adj)

                #  Once the recursive DFS call returns, upate
                # the lowest time of insertion for the node 
                low[node] = min(low[node], low[it])

                #  If the lowest time of insertion of the node is 
                # found to be greater than the time of insertion 
                # of the neighbor and it is node the starting node
                if low[it] >= tin[node] and parent != -1:

                    # Mark the node as an articulation point
                    mark[node] = True

                # Increment the child counter
                child += 1

            # Else if the neighbor is already visited
            else:

                # Update the lowest time of insertion of the node
                low[node] = min(low[node], tin[it])

        # If the node is not a starting node 
        # and has more than one child 
        if child > 1 and parent == -1:

            # Mark the node as an articulation point
            mark[node] = True

    # Function to determine the articulation 
    # points in the given graph
    def articulationPoints(self, n, adj):

        # Visited array 
        vis = [False] * n

        # To store the time of insertion(discovery time) of nodes
        tin = [-1] * n

        # To store the lowest time of insert of the nodes
        low = [-1] * n

        # To mark if a node is an articulation point
        mark = [False] * n

        # Start DFS traversal of the graph
        for i in range(n):

            # If a node is not visited
            if not vis[i]:

                # Perform DFS starting from that node
                self.dfs(i, -1, vis, tin, low, mark, adj)

        # To store the nodes that are articulation point
        ans = []

        # Traverse all nodes 
        for i in range(n):

            # If the node is marked as an articulation point
            if mark[i]:
                # Add it to the result
                ans.append(i)

        # If there are no articulation points, return -1
        if len(ans) == 0:
            return [-1]

        # Return the result
        return ans


if __name__ == "__main__":
    V = 7
    # Converting graph in adjacency list
    adj = [
        [1, 2, 3],
        [0],
        [0, 3, 4, 5],
        [2, 0],
        [2, 6],
        [2, 6],
        [4, 5]
    ]

    # Creating an instance of Solution class
    obj = Solution()

    # Function call to get all the 
    # articulation points in the given graph
    nodes = obj.articulationPoints(V, adj)

    # Output
    for node in nodes:
        print(node, end=" ")
    print()

Complexity Analysis:
Time Complexity: O(V+E) (where E represents the number of edges in the graph)
A DFS traversal is performed which takes O(V+E) time.

Space Complexity: O(V) The algorithm uses two arrays to store the discovery time, 
lowest time of insertion taking O(V) space. A visited array is used taking O(V) space 
and an array is used to mark the nodes as articulation points taking O(V) space.
'''
class Solution:
    def __init__(self):
        # To store the current time during traversal
        self.timer = 1

    # Helper function to make DFS calls while 
    # identifying articulation points
    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = True
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for it in adj[node]:
            if it == parent:
                continue
            if not vis[it]:
                self.dfs(it, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[it])
                if low[it] >= tin[node] and parent != -1:
                    mark[node] = True
                child += 1
            else:
                low[node] = min(low[node], tin[it])
        if child > 1 and parent == -1:
            mark[node] = True

    def articulationPoints(self, n, adj):
        vis = [False] * n
        tin = [-1] * n
        low = [-1] * n
        mark = [False] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)
        ans = []
        for i in range(n):
            if mark[i]:
                ans.append(i)
        if len(ans) == 0:
            return [-1]
        return ans
        