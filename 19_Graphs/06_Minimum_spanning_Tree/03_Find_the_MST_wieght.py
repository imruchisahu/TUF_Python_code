'''
You are given a weighted, undirected, and connected graph with V vertices numbered from 0 to V-1.



The graph is provided in the form of an adjacency list, where each entry adj[u] contains a list of pairs [v, w], representing an edge between vertex u and vertex v with weight w.



Find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. 



A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.



Note : The input to the function in code editor is giving in form of adjacency list.


Examples:




Input: V = 4, adj = [[[1, 1], [3, 4]], [[0, 1], [2, 2]], [[1, 2], [3, 3]], [[0, 4], [2, 3]]]

Output: 6

Explanation: 

Edges included in the MST:

From node 0 → [1, 1] (weight 1)
From node 1 → [2, 2] (weight 2)
From node 2 → [3, 3] (weight 3)
The total MST weight is 1 + 2 + 3 = 6.

These edges connect all vertices (0, 1, 2, 3) with minimum cost.





Input: V = 3, adj = [[[1, 5], [2, 15]], [[0, 5], [2, 10]], [[0, 15], [1, 10]]]

Output: 15

Explanation: 

Edges included in the MST:

From node 0 → [1, 5] (weight 5)
From node 1 → [2, 10] (weight 10)
The total weight of the MST is 5+10 = 15

Input: V = 4, adj = [[[1, 1], [3, 4]], [[0, 1], [2, 2]], [[1, 2], [3, 3]], [[0, 4], [2, 3]]]

Output:
7
6
8
5

Submit
Constraints:
2 ≤ V ≤ 103
V-1 ≤ E ≤ 104
1 ≤ w ≤ 105

#Prim's Alogrithm
Intuition:
The minimum spanning tree consists of edges having minimum possible edge weight that are connecting all the nodes. So, a greedy approach can be followed where all the edges are considered from a node and the minimum edge is considered connecting that node. This way, it ensures that once all the nodes are visited, the edges that are taken into the consideration form a minimum spanning tree.
This is the principle behind the Prim's Algorithm to find the minimum spanning tree for a given graph.

Algorithm:
Start with any node as the initial node in the MST. Set its key value to 0 and all other nodes' key values to infinity.
Select the node with the minimum key value that is not yet included in the MST. Add this node to the MST.
Update the key values of its adjacent nodes to the edge weights if the edge weight is smaller than the current key value.
Repeat the process until all nodes are included in the MST.
Once all the nodes are included, the MST is complete

Understanding:
Since, from every node, the minimum edge will be considered for the MST every time, the best data structure to use here will be the Minimum heap data structure, which will store a pair: {edge, node}.
Approach:
A minimum priority queue (min-heap) is used to keep track of the edges based on their weights. A visited array is used to mark nodes that have been included in the MST.
An arbitrary initial node is pushed into the priority queue with an edge weight of 0. While the priority queue is not empty, extract the edge with the minimum weight.
If the node connected by this edge is already visited, skip it. Otherwise, mark the node as visited and add the edge weight to the MST sum.
Traverse all adjacent edges of the current node. For each adjacent node that is not visited, push the edge into the priority queue.
The process continues until all nodes are included in the MST. The final sum of the weights of the edges in the MST is returned.

import heapq

class Solution:
    
    # Function to get the sum of weights of edges in MST
    def spanningTree(self, V, adj):
        
        # Min-Heap to store pair of {edgeWt, node}
        pq = []
        
        # Visited array
        visited = [0] * V
        
        # Push any arbitrary initial node
        heapq.heappush(pq, (0, 0))
        
        # To store the weight of MST
        sum = 0
        
        # Until the priority queue is not empty
        while pq:
            
            # Get the pair with minimum edge
            wt, node = heapq.heappop(pq)
            
            # If the node is already visited, 
            # skip the iteration
            if visited[node] == 1:
                continue
            
            # Otherwise, mark the node as visited
            visited[node] = 1
            
            # Update the weight of MST
            sum += wt
            
            # Traverse all the edges of the node
            for it in adj[node]:
                
                # Get the adjacent node
                adjNode = it[0]
                
                # Get the edge weight
                edgeWt = it[1]
                
                # Add the pair to min-heap if 
                # the node is not visited already
                if visited[adjNode] == 0:
                    heapq.heappush(pq, (edgeWt, adjNode))
        
        # Return the weight of MST
        return sum

if __name__ == "__main__":
    V = 4
    edges = [
        [0, 1, 1],
        [1, 2, 2],
        [2, 3, 3],
        [0, 3, 4]
    ]
    
    # Forming the adjacency list from edges
    adj = [[] for _ in range(V)]
    for it in edges:
        u, v, wt = it
        adj[u].append([v, wt])
        adj[v].append([u, wt])
    
    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to get the sum of weights of edges in MST
    ans = sol.spanningTree(V, adj)
    
    print("The sum of weights of edges in MST is:", ans)

Complexity Analysis:
Time Complexity: O(ElogE) (where E is the number of edges in the graph)
In the worst case, the min-heap will store all the E edges, and insertion operation on the min-heap takes O(logE) time taking overall O(ElogE) time.

Space Complexity: O(E + V) (where V is the number of nodes in the graph)
The min-heap will store all edges in worst-case taking O(E) space and the visited array takes O(V) space.

#Kruskal's Algorithm
class DisjointSet:
    # To store the ranks, parents and sizes 
    # of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

# Solution class
class Solution:
    # Function to get the sum of weights of edges in MST
    def spanningTree(self, V, adj):
        
        # To store the edges
        edges = []
        
        # Getting all edges from adjacency list
        for i in range(V):
            for it in adj[i]:
                v = it[0] # Node v
                wt = it[1] # edge weight
                u = i # Node u
                edges.append((wt, u, v))
        
        # Creating a disjoint set of V vertices
        ds = DisjointSet(V)
        
        # Sorting the edges based on their weights
        edges.sort()
        
        # To store the sum of edges in MST
        sum = 0
        
        # Iterate on the edges
        for wt, u, v in edges:
            # Join the nodes if not in the same set 
            if ds.findUPar(u) != ds.findUPar(v):
                
                # Update the sum of edges in MST
                sum += wt
                
                # Unite the nodes 
                ds.unionBySize(u, v)
        
        # Return the computed sum
        return sum

if __name__ == "__main__":
    V = 4
    edges = [
        [0, 1, 1],
        [1, 2, 2],
        [2, 3, 3],
        [0, 3, 4]
    ]
    
    # Forming the adjacency list from edges
    adj = [[] for _ in range(V)]
    for it in edges:
        u = it[0]
        v = it[1]
        wt = it[2]
        
        adj[u].append([v, wt])
        adj[v].append([u, wt])
    
    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to get the sum of weights of edges in MST
    ans = sol.spanningTree(V, adj)
    
    print("The sum of weights of edges in MST is:", ans)

'''
import heapq


class Solution:
    def spanningTree(self, V, adj):
        pq = []
        visited = [0] * V
        heapq.heappush(pq, (0, 0))
        sum = 0
        while pq:
            wt, node = heapq.heappop(pq)
            if visited[node] == 1:
                continue
            visited[node] = 1
            sum += wt
            for it in adj[node]:
                adjNode = it[0]
                edgeWt = it[1]
                if visited[adjNode] == 0:
                    heapq.heappush(pq, (edgeWt, adjNode))
        return sum