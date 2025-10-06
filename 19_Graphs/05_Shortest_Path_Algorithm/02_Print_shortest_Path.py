'''
Given a weighted undirected graph having n vertices numbered from 1 to n and m edges describing there are edges, where edges[i]=[ai,bi,wi], representing an edge from vertex ai to bi with weight wi.



Find the shortest path between the vertex 1 and the vertex n and if path does not exist then return a list consisting of only -1.



If there exists a path, then return a list whose first element is the weight of the path and the remaining elements represent the shortest path from vertex 1 to vertex n.



Note: On IDE only the total sum of weights will be shown as output. As there might be more than one path (The path will be validated through driver code and If wrong then output shown will be -2.).


Examples:






Input: n = 5, m= 6, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]

Output: 5 1 4 3 5

Explanation: The source vertex is 1. Hence, the shortest distance path of node 5 from the source will be 1->4->3->5 as this is the path with a minimum sum of edge weights from source to destination.





Input: n = 4, m = 4, edges = [[1,2,2], [2,3,4], [1,4,1],[4,3,3]]

Output:1 1 4 

Explanation: The source vertex is 1. Hence, the shortest distance path of node 4 from the source will be 1->4 as this is the path with the minimum sum of edge weights from source to destination.

Input: n = 3, m = 1, edges = [[1,2,2]]

Output:
2 1 3
2 1 2 3
-1
1 1 3

Submit
Constraints:
2 <= n <= 104
0 <= m <= 2*104
1 <= a, b <= n
1 <= w <= 105

Intuition:
Since the problem requires the shortest path from source node(node 1) to node n, the first thought that must come to the mind is to use Dijkstra's Algorithm.

Modification:
Since the shortest path needs from source node(node 1) to node n is required, for every node possible, its parent node must be stored via which the node is reachable through minimum distance. Hence, in the Dijkstra's Algorithm, a slight modification can be done where whenever an edge relaxation happens for a particular node, it's parent node is stored in an array.
Approach:
Use a priority queue to process nodes by their shortest known distance.
Initialize two array
One to store shortest distances, with the source node set to 0 and all others to infinity.
Another for parent nodes, setting each node as its own parent initially.
Add the source node to the priority queue with a distance of 0.
Extract the node with the smallest distance from the queue and perfom edge relaxation (update the distances to its neighbors if a shorter path is found). Add the updated neighbors back to the queue and update the parent of node.
The distance array maintains the shortest distances from the source to all nodes, while the parent array tracks the path.
If the destination node is reachable, use the parent array to trace back from the destination to the source, forming the path. If unreachable, return [-1].

import heapq

class Solution:
    # Function to find the shortest 
    # path from node 1 to node n
    def shortestPath(self, n, m, edges):
        
        # Adjacency list to store graph
        adj = [[] for _ in range(n + 1)]
        
        # Adding the edges to the graph
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
        
        # Using priority queue to 
        # implement Dijkstra Algorithm
        pq = []
        
        # Distance array
        dist = [float('inf')] * (n + 1)
        
        # Parent array
        parent = list(range(n + 1))
        
        # Distance of source node 
        # (node 1) to itself is zero
        dist[1] = 0
        
        # Push the source node to the queue.
        heapq.heappush(pq, (0, 1))
        
        # Until the queue is empty
        while pq:
            # Get the pair containing node having 
            # minimum distance from source node
            dis, node = heapq.heappop(pq)
            
            # Iterate through the neighbors
            for adjNode, edWt in adj[node]:
                # If the tentative distance to 
                # reach adjacent node is smaller 
                # than the known distance
                if dis + edWt < dist[adjNode]:
                    
                    # Update the known distance
                    dist[adjNode] = dis + edWt
                    
                    # Push the new pair to priority queue
                    heapq.heappush(pq, (dis + edWt, adjNode))
                    
                    # Update the parent of the adjNode 
                    # to the recent node(where it came from)
                    parent[adjNode] = node
        
        # If distance to the node could not be found, 
        # return an array containing -1.
        if dist[n] == float('inf'):
            return [-1]
        
        # Array to store the path
        path = []
        
        # Start from the destination node
        node = n
        
        # Iterate backwards from destination 
        # to source through the parent array
        while parent[node] != node:
            # Add the node to the path
            path.append(node)
            # Take a step back
            node = parent[node]
        
        # Add the source node to the path
        path.append(1)
        
        # Since the path stored is in a 
        # reverse order, reverse the array 
        # to get the actual path
        path.reverse()
        
        # Add the path weight in the beginning
        path.insert(0, dist[n])
        
        # Return the result
        return path

if __name__ == "__main__":
    n = 5
    m = 6
    edges = [
        [1, 2, 2], [2, 5, 5], [2, 3, 4], 
        [1, 4, 1], [4, 3, 3], [3, 5, 1]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find the shortest distance 
    # of each node from the source node
    ans = sol.shortestPath(n, m, edges)
    
    # Output
    print("The resulting path weight is:", ans[0])
    print("The path is:")
    for i in range(1, len(ans)):
        print(ans[i], end=" ")

Complexity Analysis:
Time Complexity: O((N+M)*logN)
Each node is processed once in the priority queue and deletion and insertion operation takes O(logN) time making it overall O(N*logN) in the worst case.
For each vertex, all its edges are relaxed. This operation involves updating the priority queue, which takes O(logV) making it overall O(M*logN) for E edges in the worst case.
Reconstructing the path involves tracing the parent array, which takes O(N) in the worst case (since we may trace back through all vertices).
Space Complexity: O(N)
The priority queue will store distances to all nodes in worst case leading to O(N) space.
The distance array and parent array takes O(N) space each.
The path array will store O(N) nodes in the worst case.

'''
import heapq
class Solution:
    def shortestPath(self,n, m, edges):
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
        pq = []
        dist = [float('inf')] * (n + 1)
        parent = list(range(n + 1))
        dist[1] = 0
        heapq.heappush(pq, (0, 1))
        while pq:
            dis, node = heapq.heappop(pq)
            for adjNode, edWt in adj[node]:
                if dis + edWt < dist[adjNode]:
                    dist[adjNode] = dis + edWt
                    heapq.heappush(pq, (dis + edWt, adjNode))
                    parent[adjNode] = node
        if dist[n] == float('inf'):
            return [-1]
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        path.insert(0, dist[n])
        return path
    