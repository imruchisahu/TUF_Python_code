'''
Given an undirected graph with V vertices. Two vertices u and v belong to a single province if there is a path from u to v or v to u. Find the number of provinces. The graph is given as an n x n matrix adj where adj[i][j] = 1 if the ith city and the jth city are directly connected, and adj[i][j] = 0 otherwise.



A province is a group of directly or indirectly connected cities and no other cities outside of the group.


Examples:


Input: adj=[ [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1] ]

Output: 2

Explanation:In this graph, there are two provinces: [1, 4] and [2, 3]. City 1 and city 4 have a path between them, and city 2 and city 3 also have a path between them. There is no path between any city in province 1 and any city in province 2.

Input: adj= [ [1, 0, 1], [0, 1, 0], [1, 0, 1] ]

Output: 2

Explanation: The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.

Input: adj= [ [1, 1], [1, 1] ]

Output:
2
1
3
4

Submit
Constraints:
  1 <= V <= 300
  V == adj.length
  V == adj[i].length
  adj[i][j] is 1 or 0.
  adj[i][i] == 1
  a[i][j] == adj[j][i]
  
  Intuition:
A province is like a group of directly or indirectly connected cities and no other cities outside of the group. Every city in a province can be visited from every other city in the same province.
To solve this problem, all the cities and their connections can be explored to identify these groups. For this, the traversal techniques BFS and DFS can be used and every time, we had to start from a new city, a new group of cities is explored.

Approach:
Convert the given adjacency matrix to adjacency list for easy traversal.
Initialise a visited array to mark the nodes that as visited and a counter to count the number of provinces found.
Every time a new node is visited, a new province is founds so increment the counter and traverse all the nodes connected to current node.
By the end of the exploration, the counter will get us the total number of provinces.

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
    
    # Function to find the number of
    # provinces in the given graph
    def numProvinces(self, adj):
        
        # Variable to store number of nodes
        V = len(adj)
        
        # To store adjacency list
        adjLs = [[] for _ in range(V)]
        
        # Convert adjacency matrix to adjacency list
        for i in range(V):
            for j in range(V):
                # self nodes are not considered
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        
        # Visited array
        vis = [0] * V
        
        # Variable to store number of provinces
        cnt = 0
        
        # Start Traversal
        for i in range(V):
            # If the node is not visited
            if not vis[i]:
                # Increment counter
                cnt += 1
                
                # Start traversal from current node
                self.bfs(i, adjLs, vis)
                #self.dfs(i, adjLs, vis)
        
        # Return the count
        return cnt

# Main function to test the solution
if __name__ == "__main__":
    adj = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the provinces in the given graph
    ans = sol.numProvinces(adj)
    
    print("The number of provinces in the given graph is:", ans)

Complexity Analysis:
Time Complexity: O(V + E) (where V denotes the number of nodes, E denotes the number of edges)
Converting adjacency matrix to list takes O(V2) time (equivalent to O(E)).
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
        while q:
            i = q.popleft()
            for adjNodes in adjLs[i]:
                
                if vis[adjNodes] != 1:
                    vis[adjNodes] = 1
                    q.append(adjNodes)

  
    def dfs(self, node, adjLs, vis):
        vis[node] = 1 
        for it in adjLs[node]:
            if not vis[it]:
                self.dfs(it, adjLs, vis)
    
    def numProvinces(self, adj):
        V = len(adj)
        adjLs = [[] for _ in range(V)]
        
        # Convert adjacency matrix to adjacency list
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        vis = [0] * V
        cnt = 0
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.bfs(i, adjLs, vis)
                #self.dfs(i, adjLs, vis)
        return cnt
        