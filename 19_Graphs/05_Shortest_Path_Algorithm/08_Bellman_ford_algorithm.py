'''
Given a weighted and directed graph of V vertices and E edges. An edge is represented as [ai, bi, wi], meaning there is a directed edge from ai to bi having weight wi. Find the shortest distance of all the vertices from the source vertex S. If a vertex can't be reached from the S then mark the distance as 109.



If the graph contains a negative cycle then return -1 in a list.


Examples:




Input : V = 6, Edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], S = 0

Output: 0 5 3 3 1 2

Explanation:

For node 1, shortest path is 0->1 (distance=5).

For node 2, shortest path is 0->1->2 (distance=3)

For node 3, shortest path is 0->1->5->3 (distance=3)

For node 4, shortest path is 0->1->5->3->4 (distance=1)

For node 5, shortest path is 0->1->5 (distance=2)

Input : V = 2, Edges = [[0,1,9]], S = 0

Output: 0 9

Explanation: For node 1, the shortest path is 0->1 (distance=9)

Input: V=3, Edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], S = 2

Output:
1 6 0
0 6 1
1 5 0
1 1 0

Submit
Constraints:
1 ≤ V ≤ 500
1 ≤ E ≤ V*(V-1)
-1000 ≤ edges[i][3] ≤ 1000
0 ≤ S < V

Intuition:
The first thing that comes to mind when the requirement is to find shortest distance of all vertices from the source vertex S is Dijkstra's Algorithm. But this problem suggests that graphs can contain negative edges for which the Dijkstra's algorithm will fail.

To solve such issue, the Bellman Ford Algorithm will come in picture. It not only works when the graph contains negative edges, but also helps identify if the graph contains negative cycle (a cycle where sum of all weights is negative). The algorithm finds the minimum distance to reach any node by performing N-1 times Edge Relaxation (where N is the number of nodes in the graph). Though Bellman Ford Algorithm is more versatile, it is slower when compared to Dijkstra's Algorithm.

Edge Relaxation:
Consider an edge between node u and node v having a weight of wt as shown in the figure: 
Consider the distance to reach node u and node v (via paths explored till now) be dist[u] and dist[v] respectively. If the distance taken to reach node v via some node u (dist[u] + wt) is smaller than the known distance to reach node v (dist[v]), then a shorter path to reach node v is found, which passes via node u. Thus, we update the distance to reach node v (dist[v]) to dist[u] + wt. This process of updating the distance is known as Edge Relaxation.

Why exactly N-1 iterations?
Longest Path in a Graph: The longest possible path without cycles in a graph with N nodes consists of (N-1) edges. And during each iteration, the Bellman-Ford algorithm updates the shortest path information for one more edge in the path.
Ensuring All Paths Are Considered: By repeating the relaxation process (N-1) times, the algorithm ensures that all vertices are updated based on paths that could extend up to (N-1) edges.

How to detect a negative cycle in the graph?
It is already known to us that if a graph has negative cycle, the edge relaxation can be done for an infinite number of times. But the algorithm suggests that all the edges will be relaxed after exactly (N-1) iterations.
Thus in order to check the existence of a negative cycle, an extra iteration can be performed to check if the edge relaxation is possible or not.
If in the extra iteration, the edge relaxation was possible, a negative cycle is confirmed in the graph.

Algorithm:
Set the distance to the starting node as 0 and to all other nodes as infinity.
On all the edges, perform Edge Relaxation for (N-1) times updating the distances of all nodes.
To detect if negative cycle exists, try performing edge relaxation on all the edges once more.
If for any edge, relaxation was possible, the graph contains a negative cycle.
Approach:
Initialize a distance array with a very large value (1e9) for all vertices. Set the distance of the source vertex to 0.
Perform edge relaxation on all edges for V-1 times, where V is the number of vertices i.e., check if the known distance to the destination vertex can be minimized by taking the edge. If yes, update the distance.
Perform an additional iteration over all edges to check for negative weight cycles. If any distance can still be minimized, a negative cycle exists in the graph, and the algorithm returns {-1}.
Return the distance array, which contains the shortest distances from the source to all other vertices, or {-1} if a negative cycle is detected.
Dry Run:

Solution:
class Solution:

    # Function to implement 
    # Bellman Ford Algorithm
    def bellman_ford(self, V, edges, S):
        
        # To store the distance
        dist = [int(1e9)] * V
        
        # Distance of source from itself is zero
        dist[S] = 0
        
        # Repeat for V-1 times
        for _ in range(V-1):
            
            # Iterate on all the edges
            for u, v, wt in edges:
                
                # Edge relaxation
                if (dist[u] != int(1e9) and 
                    dist[u] + wt < dist[v]):
                       
                    # Updating the known distance
                    dist[v] = dist[u] + wt
        
        # An extra relaxation to check if the 
        # graph consists of a negative cycle
        for u, v, wt in edges:
            
            # If edge relaxation is possible, 
            # negative cycle exists
            if (dist[u] != int(1e9) and 
                dist[u] + wt < dist[v]):
                   
                # Return [-1]
                return [-1]
        
        # Return the computed result
        return dist


if __name__ == "__main__":
    V, S = 6, 0
    edges = [
        [3, 2, 6], [5, 3, 1], 
        [0, 1, 5], [1, 5, -3], 
        [1, 2, -2], [3, 4, -2], 
        [2, 4, 3]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to implement 
    # Bellman Ford Algorithm
    ans = sol.bellman_ford(V, edges, S)
    
    # Output
    if ans == [-1]:
        print("The graph contains negative cycle.")
    else:
        print("The shortest distance from source is: ", end=" ")
        for d in ans:
            print(d, end=" ")

Complexity Analysis:
Time Complexity: O(V*E)
All the E edges are relaxed for a total of V-1 times. And an extra iteration is performed to detect negative cycle, making the algorithm take O(V*E) time.

Space Complexity: O(V)
The distance array takes O(V) time.


'''
class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [int(1e9)] * V
        dist[S] = 0
        for _ in range(V-1):
            for u, v, wt in edges:
                if (dist[u] != int(1e9) and 
                    dist[u] + wt < dist[v]):
                    dist[v] = dist[u] + wt
        for u, v, wt in edges:
            if (dist[u] != int(1e9) and 
                dist[u] + wt < dist[v]):
                return [-1]
        return dist