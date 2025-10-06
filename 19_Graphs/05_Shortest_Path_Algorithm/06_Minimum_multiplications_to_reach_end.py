'''
Given start, end, and an array arr of n numbers. At each step, the start is multiplied by any number in the array and then a mod operation with 100000 is done to get the new start.



Find the minimum steps in which the end can be achieved starting from the start. If it is not possible to reach the end, then return -1.


Examples:
Input: arr = [2, 5, 7], start = 3, end = 30

Output: 2

Explanation: 

Step 1: 3*2 = 6 % 100000 = 6 

Step 2: 6*5 = 30 % 100000 = 30

Therefore, in minimum 2 multiplications, we reach the end number which is treated as a destination node of a graph here.

Input: arr = [3, 4, 65], start = 7, end = 66175

Output: 4

Explanation: 

Step 1: 7*3 = 21 % 100000 = 21 

Step 2: 21*3 = 6 % 100000 = 63 

Step 3: 63*65 = 4095 % 100000 = 4095 

Step 4: 4095*65 = 266175 % 100000 = 66175

Therefore, in minimum 4 multiplications we reach the end number which is treated as a destination node of a graph here.

Input: arr = [3, 4, 65], start = 7, end = 21

Output:
0
1
3
2

Submit
Constraints:
  1 <= n <= 104
  1 <= arr[i] <= 104
  1 <= start, end < 105

Intuition:
How to identify this as a problem on Graphs?
When dealing with problems that involve transforming one value to another through a series of operations, it's helpful to think of the problem as a graph because:
Node Representation: Each possible value of start can be considered a node (or start) in a graph.
Transitions as Edges: The operations (multiplying by any number in the array and taking modulo 100000) represent transitions (or edges) between these states.
Path Finding: The goal is to find the shortest sequence of operations (steps) that transform start into end. This is analogous to finding the shortest path between two nodes in a graph.
Once it is clear, this problem boils down to finding Shortest path in undirected graph with unit weights.

How to identify the neighbors for a node?
For any current node(value), its neighbors are the nodes(values) obtained by multiplying it by each number in the array arr and then taking modulo 100000.
Edge Cases:
If the start and end are identical, there is no transition(steps) required. Hence, 0 can be returned.
If it is not possible to transform start to end, return -1.
Approach:
Create a array to store minimum steps to reach a node initialized to infinity for all possible values. Set the distance of the starting value (start) to 0. Use a queue to perform BFS.
Perform BFS traversal starting from the source node (start value).
For each node(value), update the distance of its adjacent nodes(values) if a shorter path is found and push the node in the queue. Return the steps taken if end value is reached.
If reaching end value is not posssible, return -1.
Dry Run:

Solution:
from collections import deque

class Solution:
    
    # Function to determine minimum 
    # multiplications to reach end 
    def minimumMultiplications(self, arr, start, end):
        
        # Base case
        if start == end:
            return 0
        
        # Size of array
        n = len(arr)
        mod = 100000 # mod
        
        # Array to store minimum 
        # steps (distance array)
        minSteps = [float('inf')] * 100000
        
        # Queue to implement 
        # Dijkstra's algorithm
        q = deque()
        
        # Mark initial position as 0
        minSteps[start] = 0
        
        # Add the initial node to queue
        q.append((0, start))
        
        # Until the queue is empty
        while q:
            
            # Get the element
            steps, val = q.popleft()
            
            # Check for adjacent neighbors
            for i in range(n):
                
                # Value of neighboring node
                num = (val * arr[i]) % mod
                
                # If end is reached, return steps taken
                if num == end:
                    return steps + 1
                
                # Check if the current steps taken is 
                # less than earlier known steps
                if steps + 1 < minSteps[num]:
                    
                    # Update the known steps
                    minSteps[num] = steps + 1
                    
                    # Insert the pair in queue
                    q.append((steps + 1, num))
        
        # Return -1 if reaching 
        # end is not possible
        return -1

if __name__ == "__main__":
    start = 3
    end = 30
    arr = [2, 5, 7]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to determine minimum 
    # multiplications to reach end
    ans = sol.minimumMultiplications(arr, start, end)
    
    # Output
    print("The minimum multiplications to reach end is:", ans)

Complexity Analysis:
Time Complexity: O(100000*N) (where N is the length of given array)
A simple BFS traversal is performed taking O(V+E) time, where V represents nodes (which can be 100000 in the worst case) and E represents the number of edges (transitions) (which can be 100000*N, since for every value, N edges are formed). This makes the overall time complexity as O(100000*N).

Space Complexity: O(100000*N)

Queue space will store all the transitions possible in worst-case resulting in O(100000*N) space.
The array to store minimum steps takes O(100000) space.

'''
from collections import deque


class Solution:
    def minimumMultiplications(self, arr, start, end):
        if start == end:
            return 0
        n = len(arr)
        mod = 100000 # mod
        minSteps = [float('inf')] * 100000
        q = deque()
        minSteps[start] = 0
        q.append((0, start))
        while q:
            steps, val = q.popleft()
            for i in range(n):
                num = (val * arr[i]) % mod
                if num == end:
                    return steps + 1
                if steps + 1 < minSteps[num]:
                    minSteps[num] = steps + 1
                    q.append((steps + 1, num))
        return -1
