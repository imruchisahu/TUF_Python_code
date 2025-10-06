'''
You are given a directed graph with V vertices, numbered from 0 to V − 1, and its adjacency list Adj, where Adj[i] contains all vertices j such that there is a directed edge from vertex i to vertex j.

Your task is to find the number of strongly connected components (SCCs) in the graph.


Examples:
Input: V=5, Adj=[[2,3],[0],[1],[4],[]]





Output: 3

Explanation: Three strongly connected components are marked below:





Input: V=8, Adj=[[1],[2],[0,3],[4],[5,7],[6],[4,7],[]]



Output: 4

Explanation: Four strongly connected components are marked below:





Input: V=3, Adj=[[1], [2],[]]

Output:
2
3
1
4

Submit
Constraints:
1 ≤ V ≤ 5000

0 ≤ E ≤ (V*(V-1))

0 ≤ ai, bi ≤ V-1

What is meant by Strongly Connected Component (SCC)?
A component is called a Strongly Connected Component(SCC) only if for every possible pair of vertices (u, v) inside that component, u is reachable from v and v is reachable from u.
Note: Strongly connected components(SCC) are only valid for directed graphs.

Consider the following example: 
There are 4 strongly connected components in the above graph which are (0,1,2), (3), (4,5,6), and (7). Note that a component containing a single vertex is always a strongly connected component.

Intuition:
Example:
Consider starting a DFS traversal from node 0 for the following graph, it will end up visiting all nodes making it impossible to differentiate between different SCCs: 
Another way to represent the graph is in the following way:

By definition, within each SCC, every node is reachable. So, DFS traversal is started from a node of SCC1, all the nodes in SCC1 can be visited and via edge e1 the SCC2 can be reached. Similarly, traversal can be done from SCC2 to SCC3 via edge e2 and from SCC3 to SCC4 via edge e3. Thus all the nodes of the graph become reachable.

But, if the edges e1, e2, e3 and e4 are reversed, the graph will be: 
Now, in this graph, if a DFS is started from node 0, it will only visit nodes in SSC1. It is true for all other nodes in Strongly Connected Components. Hence, it is clear that in one DFS call, all the nodes in one SCC will be visited. Thus, the number of DFS calls will represent the number of strongly connected components.

How to identify the edges that must be reversed?
To find the edges that must be reversed, the strongly connected components must be known prior. To solve this problem, all the edges in the graph can be reversed, this will not affect the strongly connected components as already all nodes are reachable to each other. Thus, the graph will look like this: 
How to identify the starting node for DFS traversal?
Consider if instead of node 0, node 7 is used as the starting node for DFS traversal. In such a case, even after reversing the edges, all the nodes will be visited. Thus, it is important to identify the node from where the DFS can be started so that the SCCs can be identified.

This can be solved by identifying the order of visiting the nodes when a DFS traversal is made on the original graph. The node that will be visited later will have a greater finishing time, and the node that will be visited before will have a smaller finishing time.

Using this, the order in which the nodes must be visited to determine the number of SCCs can be determined based on their finishing time. The DFS calls for the node that was visited first(having the smallest finishing time) must be made first and for the node that was visited last(having the greatest finishing time) must be made last.

Note: Since the node visited last in the original DFS call must be visited first in the later DFS call, a Stack data structure can be used to store the nodes based on their finishing times.
Kosaraju's Algorithm:
Sort all the nodes according to their finishing time: Perform a DFS call to sort the nodes based on their finishing time and store them in a stack.
Reverse all the edges of the entire graph: Create a new graph where all the edges of the original graph will be reversed.
Perform the DFS and count the number of different DFS calls to get the number of SCC: Start DFS traversal on the reversed graph from the node which is on the top of the stack and continue until the stack becomes empty. For each DFS call, the counter representing the number of SCCs can be incremented by 1.
Approach:
Create a visited array to keep track of visited nodes and a stack to store nodes based on their finishing times during DFS traversal.
Perform a DFS on the original graph to determine the finishing times of nodes. Each node is pushed onto the stack after all its descendants are processed.
Reverse the edges of the original graph to create a transposed graph. Perform DFS on the transposed graph, starting from the nodes in the order defined by the stack (based on their finishing times from the first DFS).
Count the number of DFS trees formed in this step, which corresponds to the number of strongly connected components.
The count of DFS trees from the second pass is the number of strongly connected components in the original graph.

class Solution:
    def dfs(self, node, vis, adj, st):
        # Mark the node as visited
        vis[node] = 1

        # Traverse all its neighbors
        for it in adj[node]:
            if not vis[it]:
                # Recursively perform DFS if not visited already
                self.dfs(it, vis, adj, st)
        
        # Push the node in stack
        st.append(node)
    
    def helperDFS(self, node, vis, adjT):
        # Mark the node as visited
        vis[node] = 1
        
        # Traverse all its neighbors
        for it in adjT[node]:
            if not vis[it]:
                # Recursively perform DFS if not already visited
                self.helperDFS(it, vis, adjT)
    
    def kosaraju(self, V, adj):
        # Visited array
        vis = [0] * V
        
        # Stack data structure 
        st = []
        
    #Perform initial DFS to store the nodes in stack based on their finishing time 
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj, st)
        
        # To store the reversed graph
        adjT = [[] for _ in range(V)]
        
        #Reverse all the edges of original graph to the reversed graph 
        for i in range(V):
            # Mark the node as unvisited
            vis[i] = 0
            
            # Add the reversed edge
            for it in adj[i]:
                adjT[it].append(i)
        
        #To store the count of strongly connected components 
        count = 0
        
        #Start DFS call from every unvisited node based on their finishing time 
        while st:
            # Get the node
            node = st.pop()
            
            # If not visited already
            if not vis[node]:
                count += 1
                self.helperDFS(node, vis, adjT)
        
        # Return the result
        return count

# Main function
if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    adj[0].extend([2, 3])
    adj[1].append(0)
    adj[2].append(1)
    adj[3].append(4)
    
    sol = Solution()
    count = sol.kosaraju(V, adj)
    print("Number of strongly connected components:", count)

Complexity Analysis:
Time Complexity: O(V+E) (where E represent the number of edges)
Two DFS traversals are made each taking an O(V+E) time. Reversing all the edges in the graph takes O(E) time.

Space Complexity: O(V+E)
Storing the transposed graph takes O(V+E) space and the space due to the stack and visited array will be O(V) each.

'''
class Solution:
    def dfs(self, node, vis, adj, st):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, vis, adj, st)
        st.append(node)
    
    def helperDFS(self, node, vis, adjT):
        vis[node] = 1
        for it in adjT[node]:
            if not vis[it]:
                self.helperDFS(it, vis, adjT)
    def kosaraju(self, V, adj):
        vis = [0] * V
        st =[]
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj, st)
        adjT = [[] for _ in range(V)]
        for i in range(V):
            vis[i] = 0
            for it in adj[i]:
                adjT[it].append(i)
        count = 0
        while st:
            node = st.pop()
            if not vis[node]:
                count += 1
                self.helperDFS(node, vis, adjT)
        return count
      