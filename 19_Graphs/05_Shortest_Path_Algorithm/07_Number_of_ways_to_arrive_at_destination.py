'''
A city consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that one can reach any intersection from any other intersection and that there is at most one road between any two intersections.



Given an integer n and a 2D integer array ‘roads’ where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. Determine the number of ways to travel from intersection 0 to intersection n - 1 in the shortest amount of time.



Since the answer may be large, return it modulo 109 + 7.


Examples:




Input: n=7, m=10, roads= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

Output: 4

Explanation: 

The four ways to get there in 7 minutes (which is the shortest calculated time) are:

- 0 6

- 0 4 6

- 0 1 2 5 6

- 0 1 3 5 6





Input: n=6, m=8, roads= [[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]

Output: 3

Explanation: 

The three ways to get there in 8 minutes (which is the shortest calculated time) are:

- 0 5

- 0 2 5

- 0 1 3 4 5

Input: n = 4, m = 4, roads = [[0, 1, 10], [1, 2, 7], [2, 3, 4], [0, 3, 3]]

Output:
7
4
0
1

Submit
Constraints:
1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi

Intuition:
Since there can be many paths to reach the destination node from the given source node, the problem requires us to find all those paths that are taking shortest time in order to reach our destination.

Understanding:
Consider the following image:  which represents that there are three shortest paths to reach the destination node from the source node.

Without the loss of generality, it can be said that the number of ways to reach the source node (in shortest time) is equal to sum of number of ways to reach the intermediate nodes (in shortest time) from the destination nodes

Mathematically,
ways[node] = ways[node1] = ways[node2] + ways[node3]
(where ways[node x] represents the number of ways to reach node x from source node with the shortest possible time).

We are already aware of Dijkstra's algorithm which can help us find the shortest path (path taking shortest time) from source to destination node. The only change required to get to the answer will be to add up the number of ways to reach a node (in shortest time).
Approach:
The city is modeled as a graph with intersections as nodes and roads as edges. Each edge has a weight representing the travel time. The graph is stored in an adjacency list for easy traversal.
Arrays are used to track the minimum time to reach each intersection and the number of ways to reach each intersection in that minimum time. A priority queue is initialized to implement Dijkstra's algorithm, starting from the initial intersection.
The priority queue processes intersections based on the shortest accumulated travel time. For each intersection, neighboring intersections are explored. If a shorter path to a neighbor is found, the minimum time and the number of ways to reach the neighbor are updated.
If an equally short path is found, the number of ways from the current intersection is added to the neighbor's count, ensuring large numbers are handled using modulo 109 + 7.
After processing all intersections, return the number of ways to reach the destination in the shortest time, modulo 109 + 7.

import heapq
from collections import defaultdict
from typing import List

class Solution:
    
    # Function to get the number of ways to arrive
    # at destinations in shortest possible time
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        mod = 10**9 + 7 # Mod value
        
        # To store the graph
        adj = defaultdict(list)
        
        # Adding the edges to the graph
        for it in roads:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))
        
        # Array to store the minimum 
        # time to get to nodes
        minTime = [float('inf')] * n
        
        # To store the number of 
        # ways to reach nodes
        ways = [0] * n
        
        # Priority queue to store: {time, node}
        pq = []
        
        # Initial configuration
        minTime[0] = 0
        ways[0] = 1
        heapq.heappush(pq, (0, 0))
        
        # Until the priority queue is empty
        while pq:
            
            # Get the element
            time, node = heapq.heappop(pq)
            
            # Traverse its neighbors
            for adjNode, travelTime in adj[node]:
                
                # If the current time taken is less than
                # earlier known time to reach adjacent node
                if minTime[adjNode] > time + travelTime:
                    
                    # Update the time to reach adjacent node
                    minTime[adjNode] = time + travelTime
                    
                    # Update the number of ways
                    ways[adjNode] = ways[node]
                    
                    # Add the new element in priority queue
                    heapq.heappush(pq, (minTime[adjNode], adjNode))
                
                # Else if the current time taken is same as
                # earlier known time to reach adjacent node 
                elif minTime[adjNode] == time + travelTime:
                    
                    # Update the number of ways 
                    # to reach adjacent nodes
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod
        
        # Return the result
        return ways[n - 1] % mod

# Example usage
if __name__ == "__main__":
    n = 7
    roads = [
        [0, 6, 7], [0, 1, 2], [1, 2, 3],
        [1, 3, 3], [6, 3, 3], [3, 5, 1],
        [6, 5, 1], [2, 5, 1], [0, 4, 5],
        [4, 6, 2]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to get the number of ways to 
    # arrive at destinations in shortest possible time
    ans = sol.countPaths(n, roads)
    
    # Output
    print("The number of ways to arrive at destinations in shortest possible time is:", ans)

Complexity Analysis:
Time Complexity: O(M*logN) A simple Dijkstra's algorithm is used which takes O(E*logV) time (where V and E represents the number of nodes and edges in the graph respectively).

Space Complexity: O(N)

Dijkstra's Algorithm will take extra O(N) space due to priority queue and array to store minimum time to reach nodes.
The array to store the number of ways take O(N) space.

'''
from collections import defaultdict
import heapq


class Solution:
    def countPaths(self, n, roads):
        
        mod = 10**9 + 7 # Mod value
        adj = defaultdict(list)
        for it in roads:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))
        minTime = [float('inf')] * n
        ways = [0] * n
        pq = []
        minTime[0] = 0
        ways[0] = 1
        heapq.heappush(pq, (0, 0))
        while pq:
            time, node = heapq.heappop(pq)
            for adjNode, travelTime in adj[node]:
                if minTime[adjNode] > time + travelTime:
                    minTime[adjNode] = time + travelTime
                    ways[adjNode] = ways[node]
                    heapq.heappush(pq, (minTime[adjNode], adjNode))
                elif minTime[adjNode] == time + travelTime:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod
        return ways[n - 1] % mod