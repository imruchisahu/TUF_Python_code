'''
Given a weighted, undirected graph of V vertices, numbered from 0 to V-1, and an adjacency list adj where adj[i] represents all edges from vertex i.



Each entry in adj[i] is of the form [to, weight], where:

to → the neighboring vertex connected to i,
weight → the weight of the edge between i and to.


Given a source node S. Find the shortest distance of all the vertex from the source vertex S. Return a list of integers denoting shortest distance between each node and source vertex S. If a vertex is not reachable from source then its distance will be 109.


Examples:




Input: V = 2, adj [] = [[[1, 9]], [[0, 9]]], S=0

Output: [0, 9]

Explanation:

The shortest distance from node 0(source) to node 0 is 0 and the shortest distance from node 0 to node 1 is 9.





Input: V = 3,adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S=2

Output: [4, 3, 0]

Explanation: 

For node 0, the shortest path is 2->1->0 (distance=4)

For node 1, the shortest path is 2->1 (distance=3)

Input: V=4, adj = [[[1, 1], [3, 2]],[[0, 1], [2, 4]],[[1, 4], [3, 3]], [[0, 2], [2, 3]]], S=0

Output:
[1, 5, 2, 0]
[0, 5, 1, 2]
[0, 1, 5, 2]
[0, 1, 1, 5]

Submit
Constraints:
1 ≤ V ≤ 10000
0 ≤ adj[i][j] ≤ 10000
1 ≤ adj.size() ≤ [ (V*(V - 1)) / 2 ]
0 ≤ S < V

#USing Min-Heap
Dijkstra's Algorithm:
Dijkstra's Algorithm is used in connected graphs (undirected as well as directed) whenever it is required to find out the shortest distance from the source node to every other node.

Conditions for Dijkstra's Algorithm to work?
The graph must only have non-negative edge weights.
Algorithm:
Set the distance to the starting node as 0 and to all other nodes as infinity. Add all nodes to an unvisited set. Begin with the starting node.
Perform Edge Relaxation, i.e., for each unvisited neighbor of the current node, calculate the tentative distance from the start node. If this tentative distance is less than the known distance, update it.
Mark the current node as visited once all its neighbors have been evaluated. It won't be checked again. Choose the unvisited node with the smallest tentative distance as the new current node.
Repeat steps 2-3 untill all the nodes are visited. Once all nodes are visited, the shortest path to all the nodes is now known.
Implementation: Using Min-Heap
To implement the Dijkstra's Algorithm, a minimum heap data structure (Priority Queue) can be used. The priority queue will store the pair {dist, node} storing the tentative distance required to reach the node from the source node. If this distance is found to be smaller than the known distance, we update the distance to reach node and push to newly found pair of {dist, node} in the priority queue.

Significance of using a Min-Heap data structure:
Storing the pair {dist, node} in min-heap ensures that out of all the pairs, the node with the minimum distance (from source node) is taken into consideration first. This helps the algorithm to explore the shortest path first improving efficiency.
Approach:
Use a priority queue to process nodes by their shortest known distance.
Initialize an array to store shortest distances, with the source node set to 0 and all others to infinity.
Add the source node to the priority queue with a distance of 0.
Extract the node with the smallest distance from the queue and perfom edge relaxation (update the distances to its neighbors if a shorter path is found). Add the updated neighbors back to the queue.
The distance array contains the shortest distances from the source to all node.
Solution:
import heapq

class Solution:
    # Function to find the shortest distance of all
    # the vertices from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        # Priority queue
        pq = []
        
        # Distance array
        dist = [int(1e9)] * V
        
        # Distance of source node from itself is 0
        dist[S] = 0
        
        # Add the source node to the priority queue
        heapq.heappush(pq, (0, S))
        
        # Until the priority queue is empty
        while pq:
            
            # Get the tentative distance
            dis, node = heapq.heappop(pq)
            
            # Traverse all its neighbors
            for adjNode, edgeWt in adj[node]:
                
                # If the tentative distance to reach adjacent node
                # is smaller than the known distance
                if dis + edgeWt < dist[adjNode]:
                    
                    # Update the known distance
                    dist[adjNode] = dis + edgeWt
                    
                    # Push the new pair in priority queue
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        
        # Return the result
        return dist


# Main method
if __name__ == "__main__":
    V, S = 2, 0
    
    # Create adjacency list
    adj = [
        [(1, 9)], 
        [(0, 9)]
    ]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the shortest distance
    # of each node from the source node
    ans = sol.dijkstra(V, adj, S)
    
    # Output
    print("The shortest distance of nodes from the source node is:", end=" ")
    for i in ans:
        print(i, end=" ")
    print()
Complexity Analysis:
Time Complexity: O((V+E)*logV) (where V and E represent the number of nodes and edges of the graph)
Each node is processed once in the priority queue and deletion and insertion operation takes O(logV) time making it overall O(V*logV) in the worst case.
For each vertex, all its edges are relaxed. This operation involves updating the priority queue, which takes O(logV) making it overall O(E*logV) for E edges in the worst case.
Space Complexity: O(V)
The priority queue will store distances to all nodes in worst case leading to O(V) space.
The distance array takes O(V) space.


#Using_sort
Dijkstra's Algorithm:
Dijkstra's Algorithm is used in connected graphs (undirected as well as directed) whenever it is required to find out the shortest distance from the source node to every other node.

Conditions for Dijkstra's Algorithm to work?
The graph must only have non-negative edge weights.
Algorithm:
Set the distance to the starting node as 0 and to all other nodes as infinity. Add all nodes to an unvisited set. Begin with the starting node.
Perform Edge Relaxation i.e., for each unvisited neighbor of the current node, calculate the tentative distance from the start node. If this tentative distance is less than the known distance, update it.
Mark the current node as visited once all its neighbors have been evaluated. It won't be checked again. Choose the unvisited node with the smallest tentative distance as the new current node.
Repeat steps 2-3 untill all the nodes are visited. Once all nodes are visited, the shortest path to all the nodes is now known.
Implementation: Using Set
To implement the Dijkstra's Algorithm, a set data structure can be used. The set will store the pair {dist, node} storing the tentative distance required to reach the node from the source node. If this distance is found to be smaller than the known distance, we update the distance to reach node and insert the newly found pair of {dist, node} in the set.

Significance of using a Set data structure:
Storing the pair {dist, node} in set ensures that out of all the pairs, the node with the minimum distance (from source node) is taken into consideration first. This helps the algorithm to explore the shortest path first improving efficiency.
Another added advantage in the set is that it can perform deletion operations on pairs that are found to be unfruitful saving some iterations.
Approach:
Create a distance array initialized to infinity (1e9), except for the source vertex which is set to 0.
Use a set to store pairs of (distance, node), starting with the source node with a distance of 0.
Continuously extract the node with the smallest distance from the set until the set is empty.
For the current node, iterate through all its adjacent nodes. Calculate the tentative distance to each neighbor. If this distance is smaller than the known distance, update the distance and adjust the set.
After processing all nodes, return the distance array containing the shortest distances from the source to all nodes.

import heapq

class Solution:
    
    # Function to find the shortest distance of all 
    # the vertices from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        # Min-heap to store {dist, node}
        st = []
        
        # Distance array 
        dist = [int(1e9)] * V
        
        # Distance of source node from itself is 0
        dist[S] = 0
        
        # Adding the source node to heap
        heapq.heappush(st, (0, S))
        
        # Until the heap is empty
        while st:
            # Get the distance
            dis, node = heapq.heappop(st)
            
            # Traverse all its neighbors
            for it in adj[node]:
                adjNode, edgeWt = it # node, edge weight
                
                # If the tentative distance to 
                # reach adjacent node is smaller 
                # than the known distance
                if dis + edgeWt < dist[adjNode]:
                    # Update the known distance
                    dist[adjNode] = dis + edgeWt
                    
                    # Add the new pair to the heap
                    heapq.heappush(st, (dist[adjNode], adjNode))
        
        # Return the result
        return dist

# Main function
if __name__ == "__main__":
    V = 2
    S = 0
    adj = [
        [(1, 9)], 
        [(0, 9)]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to find the shortest distance 
    # of each node from the source node
    ans = sol.dijkstra(V, adj, S)
    
    # Output
    print("The shortest distance of nodes from the source node is: ", end="")
    for i in range(V):
        print(ans[i], end=" ")

Complexity Analysis:
Time Complexity: O((V+E)*logV) (where V and E represent the number of nodes and edges of the graph)
Each node is processed once in the set and deletion and insertion operation takes O(logV) time making it overall O(V*logV) in the worst case.
For each node, all its edges are relaxed. This operation involves updating the set, which takes O(logV) making it overall O(E*logV) for E edges in the worst case.
Space Complexity: O(V)
The set will store distances to all nodes in worst case leading to O(V) space.
The distance array takes O(V) space.


#Time-Complexity_and_Depth_theory
Why Min Heap is used instead of Queue data structure?
Even if a Queue data structure is used, the shortest path can be found, but it will act like a brute force solution as all paths are explored, and out of them the shortest one is picked.

On the other hand, using the Minimum Heap data structure ensures that the shortest path among all the paths is always explored first so that unnecessary iterations can be saved.

'''
import heapq


class Solution:
    def dijkstra(self, V, adj, S):
        pq = []
        dist = [int(1e9)] * V
        dist[S] = 0
        heapq.heappush(pq, (0, S))
        
        # Until the priority queue is empty
        while pq:
            dis, node = heapq.heappop(pq)
            for adjNode, edgeWt in adj[node]:
                if dis + edgeWt < dist[adjNode]:
                    dist[adjNode] = dis + edgeWt
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        return dist