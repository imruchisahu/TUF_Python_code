'''
There are n cities and m edges connected by some number of flights. Given an array of flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. Given three integers src, dst, and k, and return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


Examples:




Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

Output: 700

Explanation: The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.

Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.





Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1

Output: 200

Explanation:The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0 

Output:
600
700
200
500

Submit
Constraints:
  1 <= n <= 100
  0 <= flights.length <= (n * (n - 1) / 2)
   flights[i].length == 3
  0 <= fromi, toi < n
  fromi != toi
  1 <= pricei <= 104
  There will not be any multiple flights between the two cities.
  0 <= src, dst, k < n

Intuition:
Since the problem includes finding the cheapest flight to reach from source to destination, the first thought that must come to the mind is to use Dijkstra's Algorithm. But there is a restriction mentioned on the number of stops taken to reach the destination, due to which some modifications need to be done in Dijkstra's algorithm to obtain the result.
It is known that Dijkstra's algorithm is implemented using Min-heap (priority queue) data structure. For current problem, there are two things related to a node that must be stored in priority queue:

Distance to reach the node.
Stops taken to reach the node.

Now the question arises which one must be given priority in the priority queue.
Understanding how to store elements in priority queue:
While storing the elements, if priority is given to minimum distance first then after a few iterations, it can be seen that the algorithm will halt when number of stops could not exceed.
It may result in a wrong answer as it will prevent the algorithm to explore those paths which have more cost but fewer stops that the current answer.
To prevent this issue, the elements can be stored in terms of the minimum number of stops in the priority queue so that when the algorithm halts, it gives the minimum cost within limits.
Choosing better data structure to improve complexity:
It was clear till now that everything will be stored/ordered in terms of number of stops. But the stops will always increase monotonically (increasing by 1). So the actual significance of using a Min-heap data strucute here in Dijkstra's algorithm fades away. Hence, a simple Queue data structure can be used to avoid the additional logarithmic factor in the complexity (caused by the insertion/deletion operation in Min-Heap data structure).
Approach:
The cities and flights are represented as a graph using an adjacency list. Each city is a node, and each flight is an edge with an associated cost.
A vector is initialized to store the minimum cost to reach each city, initially set to a very large value (infinity). A queue is used to manage the states during traversal. Each state consists of the current city, the cost to reach that city, and the number of stops made so far.
The traversal begins from the source city, with an initial cost of 0 and 0 stops. For each city dequeued, all its neighboring cities are explored.
If a cheaper cost to reach a neighboring city is found and the number of stops does not exceed k, the neighboring city is enqueued with the updated cost and incremented stop count.
The minimum cost to reach each neighboring city is updated whenever a cheaper route is found during the traversal.
After exploring all possible routes within the stop constraint, the minimum cost to reach the destination city is returned. If unreachable within k stops, the function returns -1.

from collections import deque
from typing import List

class Solution:
    
    # Function to find cheapest price from 
    # src to dst with at most k stops 
    def CheapestFlight(self, n: int, flights: List[List[int]], 
                       src: int, dst: int, k: int) -> int:
        
        # To store the graph
        adj = [[] for _ in range(n)]
        
        # Adding edges to the graph
        for it in flights:
            adj[it[0]].append((it[1], it[2]))
        
        # To store minimum distance
        minDist = [float('inf')] * n
        minDist[src] = 0
        # Queue storing the elements of 
        # the form {stops, {node, dist}}
        q = deque([(0, src, 0)])
        
        # Until the queue is empty
        while q:
            
            # Get the element from queue
            stops, node, dist = q.popleft()
            
            # If the number of stops taken exceed k, 
            # skip and move to the next element
            if stops > k:
                continue
            
            # Traverse all the neighbors
            for adjNode, edgeWt in adj[node]:
                
                # If the tentative distance to reach adjacent
                # node is smaller than the known distance
                # and number of stops doesn't exceed k
                if (dist + edgeWt < minDist[adjNode] and 
                    stops <= k):
                    
                    # Update the known distance
                    minDist[adjNode] = dist + edgeWt
                    
                    # Add the new element to queue
                    q.append((stops + 1, adjNode, dist + edgeWt))
        
        # If the destination is unreachable, return -1
        if minDist[dst] == float('inf'):
            return -1
        
        # Otherwise return the result
        return minDist[dst]

if __name__ == "__main__":
    n = 4
    flights = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200]
    ]
    
    src, dst, k = 0, 3, 1
    
    # Creating an instance of Solution class
    sol = Solution() 
    
    # Function call to determine cheapest flight from source to destination within K stops
    ans = sol.CheapestFLight(n, flights, src, dst, k)
    
    # Output
    print("The cheapest flight from source to destination within K stops is:", ans)

Complexity Analysis:
Time Complexity: O((N+M*K)) (where N is the number of cities, M is the number of flight (edges), and K is the max. number of stops allowed)
Creating the graph takes O(M) time.
Each node can be inserted into the queue up to k+1 times (0 stops, 1 stop, ..., up to k stops) making it take O(N*k).
For each node processed in the queue, we iterate over all its adjacent nodes (edges). If there are E edges in total and each edge can be considered at most k+1 times, the total number of edge considerations takes O(M*k) time.
Space Complexity: O(M+N*K)
Storing the graph takes O(M) space.
Array to store minimum distance takes O(N) space.
Queue will store N*K elements in the worst case taking O(N*K) space.

'''
from collections import deque
from typing import List


class Solution:
    def CheapestFlight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[] for _ in range(n)]
        for it in flights:
            adj[it[0]].append((it[1], it[2]))
        
        # To store minimum distance
        minDist = [float('inf')] * n
        minDist[src] = 0
        # Queue storing the elements of 
        # the form {stops, {node, dist}}
        q = deque([(0, src, 0)])
        while q:
            stops, node, dist = q.popleft()
            if stops > K:
                continue
            for adjNode, edgeWt in adj[node]:
                if (dist + edgeWt < minDist[adjNode] and 
                    stops <= K):
                    minDist[adjNode] = dist + edgeWt
                    q.append((stops + 1, adjNode, dist + edgeWt))
        if minDist[dst] == float('inf'):
            return -1
        return minDist[dst]