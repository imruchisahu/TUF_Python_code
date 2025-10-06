'''Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say two vertices u and v belong to a same component if there is a path from u to v or v to u. Find the number of connected components in the graph.



A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.


Examples:


Input: V=4, edges=[[0,1],[1,2]]

Output: 2

Explanation: Vertices {0,1,2} forms the first component and vertex 3 forms the second component.

Input: V = 7, edges = [[0, 1], [1, 2], [2, 3], [4, 5]]

Output: 3

Explanation:

The edges [0, 1], [1, 2], [2, 3] form a connected component with vertices {0, 1, 2, 3}.

The edge [4, 5] forms another connected component with vertices {4, 5}.

Therefore, the graph has 3 connected components: {0, 1, 2, 3}, {4, 5}, and the isolated vertices {6} (vertices 6 and any other unconnected vertices).

Input: V = 5, edges = [[0, 1], [1, 2], [3, 4]]

Output:
1
2
4
3

Submit
Constraints:
1 ≤ V, edges.length ≤ 104
0 <= edges[i][0], edges[i][1] <= V-1
All edges are unique

Intuition:
A component is like a group of directly or indirectly connected nodes and no other nodes outside of the group. Every node in a component can be visited from every other node in the same province.
To solve this problem, all the nodes and their connections can be explored to identify these groups. For this, the traversal techniques BFS and DFS can be used and every time, we had to start from a new node, a new group of nodes(component) is explored.

Approach:
Convert the given adjacency matrix to adjacency list for easy traversal.
Initialise a visited array to mark the nodes that as visited and a counter to count the number of components found.
Every time a new node is visited, a new component is founds so increment the counter and traverse all the nodes connected to current node.
By the end of the exploration, the counter will get us the total number of components.
Dry Run:

Solution:
from collections import deque

class Solution:
    
    # Function for BFS traversal
    def bfs(self, node, adjLs, vis):
        
        # Mark the node as visited
        vis[node] = 1
        
        # Queue required for BFS traversal
        q = deque()
        
        # To start traversal from node
        q.append(node)
        
        # Keep on traversing till 
        # the queue is not empty
        while q:
            # Get the node
            i = q.popleft()
            
            # Traverse its unvisited neighbours
            for adjNodes in adjLs[i]:
                
                if vis[adjNodes] != 1:
                    
                    # Mark the node as visited
                    vis[adjNodes] = 1
                    
                    # Add the node to queue
                    q.append(adjNodes)
    
    # Function for DFS traversal
    def dfs(self, node, adjLs, vis):
        
        # Mark the node as visited
        vis[node] = 1
        
        # Traverse its unvisited neighbours
        for it in adjLs[node]:
            
            if not vis[it]:
                # Recursively perform DFS
                self.dfs(it, adjLs, vis)
    
    # Function call to find the number of 
    # connected components in the given graph
    def findNumberOfComponent(self, V, edges):
        E = len(edges)
        
        # To store adjacency list
        adjLs = [[] for _ in range(V)]
        
        # Add edges to adjacency list
        for i in range(E):
            adjLs[edges[i][0]].append(edges[i][1])
            adjLs[edges[i][1]].append(edges[i][0])
        
        # Visited array
        vis = [0] * V
        
        # Variable to store number of components
        cnt = 0
        
        # Start Traversal
        for i in range(V):
            # If the node is not visited
            if not vis[i]:
                # Increment counter
                cnt += 1
                
                # Start traversal from current 
                # node using any traversal
                self.bfs(i, adjLs, vis)
                # self.dfs(i, adjLs, vis)
        
        # Return the count
        return cnt

if __name__ == "__main__":
    V = 4
    edges = [
        [0, 1],
        [1, 2]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find the number of 
    # connected components in the given graph
    ans = sol.findNumberOfComponent(V, edges)
    
    print("The number of components in the given graph is:", ans)

Complexity Analysis:
Time Complexity: O(V + E) (where V denotes the number of nodes, E denotes the number of edges)
Converting the edges to adjacency list takes O(E) time.
Considering overall, all the nodes are visited through traversal techniques which takes O(V+ E) time.
Space Complexity: O(V + E)
Storing the adjacency list takes O(E) space.
Any traversal technique takes O(V) extra space.


'''
from collections import deque 
class Solution:
    def bfs(self, node, adjLs, vis):
        vis[node] = 1
        q = deque()
        q.append(node)
        
        # Keep on traversing till 
        # the queue is not empty
        while q:
            i = q.popleft()
            for adjNodes in adjLs[i]:
                if vis[adjNodes] != 1:
                    vis[adjNodes] = 1
                    q.append(adjNodes)
    
    # Function for DFS traversal
    def dfs(self, node, adjLs, vis):
        vis[node] = 1
        for it in adjLs[node]:
            if not vis[it]:
                self.dfs(it, adjLs, vis)

    def findNumberOfComponent(self, V, edges):
        E = len(edges)
        adjLs = [[] for _ in range(V)]
        
        # Add edges to adjacency list
        for i in range(E):
            adjLs[edges[i][0]].append(edges[i][1])
            adjLs[edges[i][1]].append(edges[i][0])
        vis = [0] * V
        cnt = 0
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.bfs(i, adjLs, vis)
                # self.dfs(i, adjLs, vis)
        return cnt

       