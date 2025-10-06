'''
There are a total of N tasks, labeled from 0 to N-1. Given an array arr where arr[i] = [a, b] indicates that you must take course b first if you want to take course a. Find if it is possible to finish all tasks.


Examples:
Input: N = 4, arr = [[1,0],[2,1],[3,2]]



Output: True



Explanation: It is possible to finish all the tasks in the order : 0 1 2 3.

First, we will finish task 0. Then we will finish task 1, task 2, and task 3.

Input: N = 4, arr = [[0,1],[3,2],[1,3],[3,0]]



Output: False



Explanation: It is impossible to finish all the tasks. Let’s analyze the pairs:

For pair {0, 1} -> we need to finish task 1 first and then task 0. (order : 1 0).

For pair{3, 2} -> we need to finish task 2 first and then task 3. (order: 2 3).

For pair {1, 3} -> we need to finish task 3 first and then task 1. (order: 3 1).

But for pair {3, 0} -> we need to finish task 0 first and then task 3 but task 0 requires task 1 and task 1 requires task 3. So, it is not possible to finish all the tasks.

Input: N = 2, arr = [[1,0]]

Output:
True
Constraints:
  1 <= N <= 2000
  0 <= arr.length <= 5000
  arr[i].length == 2
  0 <= arr[i][0], arr[i][1] < N
  All the pairs arr[i] are unique.
  
  Intuition:
How this problem can be identified as a Graph problem?
The problem suggests that some courses must be completed before other courses. This is analogous to Topological Sort Algorithm in graph which helps to find a ordering where a node must come come before other nodes in the ordering.
Hence, the courses can be represented as nodes of graphs and dependencies of courses can be shown as edges.

Now, For the graph formed, if the Topological sort can be found containing all the nodes (courses), all the courses can be completed in the order returned by topological sort. Else it is not possible to complete all the courses.
How to form the graph?
The pair [a,b] represents that the Course b must be completed before Course a.
Hence in the graph, two nodes representing Course a and b can be created with a directed edge from Node b to Node a. This way the topological sort will return Node b before Node a.
Approach:
Using the dependencies of courses, prepare a directed graph.
Get the topological ordering of the graph formed.
If the topological ordering contains all nodes, all the courses can be completed in that order.
Otherwise, it is not possible to completed all the courses.

from collections import deque

class Solution:

    # Function to return the topological
    # sorting of given graph
    def topoSort(self, V, adj):
        
        # To store the In-degrees of nodes
        inDegree = [0] * V
        
        # Update the in-degrees of nodes
        for i in range(V):
            
            for it in adj[i]:
                # Update the in-degree
                inDegree[it] += 1

        # To store the result
        ans = []
        
        # Queue to facilitate BFS
        q = deque()
        
        # Add the nodes with no in-degree to queue
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        
        # Until the queue is empty
        while q:
            
            # Get the node
            node = q.popleft()
            
            # Add it to the answer
            ans.append(node)
            
            # Traverse the neighbours
            for it in adj[node]:
                
                # Decrement the in-degree
                inDegree[it] -= 1
                
                # Add the node to queue if 
                # its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)
        
        # Return the result
        return ans

    # Function to determine if all 
    # the tasks can be finished
    def canFinish(self, N, arr):
        
        # To store the graph
        adj = [[] for _ in range(N)]
        
        # Form the graph
        for it in arr:
            u = it[0]
            v = it[1]
            
            # Add the edge v-> u
            adj[v].append(u)
        
        # Get the topological ordering of graph
        topo = self.topoSort(N, adj)
        
        # If it doesn't contain
        # all nodes, return false
        if len(topo) < N:
            return False
        
        # Return true otherwise
        return True

# Example usage
N = 4
arr = [
    [1, 0],
    [2, 1],
    [3, 2]
]

sol = Solution()
ans = sol.canFinish(N, arr)

# Output
if ans:
    print("All the tasks can be finished.")
else:
    print("All the tasks can not be finished.")

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represents the number of nodes and edges in the given graph)
Forming the graph takes O(E) time.
Finding topological sort takes O(V+E) time.
Space Complexity: O(V+E)
Storing the graph takes O(E) space.
Topological sorting algorithm uses extra O(V) computational space.

  '''
from collections import deque


class Solution:
    def topoSort(self, V, adj):
        
        # To store the In-degrees of nodes
        inDegree = [0] * V
        
        # Update the in-degrees of nodes
        for i in range(V):
            
            for it in adj[i]:
                # Update the in-degree
                inDegree[it] += 1
        ans = []
        q = deque()
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for it in adj[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)
        return ans

    def canFinish(self, N, arr):
        adj = [[] for _ in range(N)]
        
        # Form the graph
        for it in arr:
            u = it[0]
            v = it[1]
            
            # Add the edge v-> u
            adj[v].append(u)
        topo = self.topoSort(N, adj)
        if len(topo) < N:
            return False
        return True