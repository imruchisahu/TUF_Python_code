'''
Given a graph of V vertices numbered from 0 to V-1. Find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n x n. Matrix[i][j] denotes the weight of the edge from i to j. If matrix[i][j]=-1, it means there is no edge from i to j.


Examples:
Input: matrix = [[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, 1],[3, 5, 4, 0]]

Output: [[0, 2, 5, 6], [1, 0, 3, 4], [4, 6, 0, 1], [3, 5, 4, 0]] 

Explanation: matrix[0][0] is storing the distance from vertex 0 to vertex 0, the distance from vertex 0 to vertex 1 is 2 and so on.

Input: matrix = [[0,25],[-1,0]]

Output: [[0, 25],[-1, 0]]

Explanation: The matrix already contains the shortest distance.

Input: matrix = [[0,1,43],[1,0,6],[-1,-1,0]]

Output:
[[0, 1, 43], [1, 0, 6], [-1, -1, 0]]
[[0, 1, 43], [1, 0, 6], [13, -1, 0]]
[[0, 1, 7], [1, 0, 6], [-1, -1, 0]]
[[0, 1, 13], [1, 0, 6], [-1, -1, 0]]

Submit
Constraints:
1 <= n <= 100
-1 <= matrix[ i ][ j ] <= 1000

Intuition:
In the problem, it is required to find the shortest distance between every pair of vertices which can be seen as finding the shortest distance of every node from all nodes (multiple sources). There are already algorithms namely Dijkstra's Algorithm and Bellman Ford Algorithm but they are single-source shortest path algorithms. But here since multiple sources are considered, the FLoyd Warshall algorithm will come into picture.

The Floyd Warshall algorithm is a multi-source shortest path algorithm and it helps to detect negative cycles (a cycle where sum of all weights is negative) as well. The shortest path between node u and v means the path(from u to v) for which the sum of the edge weights is minimum.

The Floyd Warshall algorithm is nothing but the brute force approach of checking every possible path from node u to node v (via some node k) to figure out the shortest path from node u to node v.
Understanding:
Consider the following graph:  where we aim to find the shortest distance from source node to destination node. The algorithm suggests to check every path (via other nodes) from source to destination node to find the required shortest distance.
There are 5 paths to reach from source to destination node (where dist[i][j] represents the shortest distance from node i to node j):
Via node 1: Total distance = dist[s][1] + dist[1][d] , i.e., 7+2 = 9.
Via node 2: Total distance = dist[s][2] + dist[2][d] , i.e., 1+3 = 4.
Via node 3: Total distance = dist[s][3] + dist[3][d] , i.e., 10+4 = 14.
Via node 4: Total distance = dist[s][4] + dist[4][d] , i.e., 5+3 = 8.
Direct edge: Distance = 6.

Hence the shortest distance to reach from source to destination node is minimum of all the paths, i.e.,
dist[s][d] = min(all the paths from source to destination)
dist[s][d] = min(9, 4, 14, 8, 6)
dist[s][d] = 4. (Via node 2).

The Flord Warshall Algorithm is applicable to both directed as well as undirected graphs as the undirected edge can be represented as two directed edges between the nodes having same weight as that of the undirected edege.
Note:
Until now, to store a graph we have used the adjacency list. But in this algorithm, we are going to use the adjacency matrix method to represent the graph (for simplicity).
Cost of reaching a node from itself must always be 0, i.e., dist[i][i] = 0 always.

How to detect negative cycles:
Consider the following example:  Here, the distance to reach node 0 is coming out to be -3, where it should have been 0. Hence, if it is found that the distance to reach any node from itself is negative, the graph contains negative cycle.
Approach:
Initialize a distance matrix to store the minimum distance between each pair of nodes with the adjacency matrix of the graph.
Start updating the distance matrix considering each node as an intermediate node for all possible pairs of nodes.
Consider (i, j) as a pair of nodes representing source and destination nodes respectively and an intermediate node k, there can be three possible scenarios:
If k is not an intermediate node in path from i to j: Skip the iteration.
If there is no direct edge from i to j: Update the dist[i][j] to dist[i][k] + dist[k][j].
If there is a direct edge from i to j: Update the dist[i][j] to the minimum of dist[i][j] and (dist[i][k] + dist[k][j]).
Once all the pairs of nodes are checked for every intermediate nodes, the distance matrix will store the shortest distance betweeen any two nodes. Distance for nodes that are unreachable will be marked as -1.

Solution:
class Solution:
    # Function to find the shortest distance 
    # between every pair of vertices.
    def shortest_distance(self, matrix):
        
        # Getting the number of nodes
        n = len(matrix)
        
        # For each intermediate node k
        for k in range(n):
            
            # Check for every (i, j) pair of nodes
            for i in range(n):
                for j in range(n):
                    
                    # If k is not an intermediate 
                    # node, skip the iteration
                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue
                    
                    # If no direct edge from 
                    # i to v is present
                    if matrix[i][j] == -1:
                        
                        # Update the distance
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                    
                    # Else update the distance to 
                    # minimum of both paths
                    else:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

# Example usage
matrix = [
    [0, 2, -1, -1],
    [1, 0, 3, -1],
    [-1, -1, 0, -1],
    [3, 5, 4, 0]
]

# Creating an instance of 
# Solution class
sol = Solution()

# Function to find the shortest distance 
# between every pair of vertices.
sol.shortest_distance(matrix)

# Output
print("The shortest distance matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))

Complexity Analysis:
Time Complexity: O(N3) (where N repesents the number of nodes in graph) Because of three nested loops.

Space Complexity: O(N2) The algorithm uses a space of O(N2) to store shortest distance between every pair of nodes possible.

'''
class Solution:
    def shortestDistance(self, matrix):
        n = len(matrix)
        for k in range(n):
            
            # Check for every (i, j) pair of nodes
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue
                    if matrix[i][j] == -1:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                    else:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
