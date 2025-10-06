'''
There are a total of N tasks, labeled from 0 to N-1. Given an array arr where arr[i] = [a, b] indicates that you must take course b first if you want to take course a. Find the order of tasks you should pick to finish all tasks.

If no such ordering exists, return an empty array.

Since multiple valid answers are possible, the final output will be 1 if your solution is correct, otherwise 0.


Examples:
Input: N = 4, arr = [[1,0],[2,1],[3,2]]

Output: [0, 1, 2, 3]

Explanation: First,finish task 0, as it has no prerequisites. Then,finish task 1, since it depends only on task 0. After that,finish task 2, since it depends only on task 1. Finally,finish task 3, since it depends only on task 2

Input: N = 4, arr = [[0,1],[3,2],[1,3],[3,0]]

Output: []

Explanation: It is impossible to finish all the tasks. Let’s analyze the pairs:

For pair {0, 1} → we need to finish task 1 first and then task 0 (order: 1 → 0).

For pair {3, 2} → we need to finish task 2 first and then task 3 (order: 2 → 3).

For pair {1, 3} → we need to finish task 3 first and then task 1 (order: 2 → 3 → 1 → 0).

But for pair {3, 0} → we need to finish task 0 first and then task 3, which contradicts the previous order. So, it is not possible to finish all the tasks.

Input: N = 2, arr = [[1,0]]

Output:
[0, 1]
Constraints:
  1 <= N <= 2000
  0 <= arr.length <= 5000
  arr[i].length == 2
  0 <= arr[i][0], arr[i][1] < N
  All the pairs arr[i] are unique.

  Intuition:
This problem is a continuation of the problem Course Schedule-I. Just the only difference here is that instead of determining whether the tasks can be finished or not, the problem requires us to find out the ordering of tasks so that all the tasks can be finished. If no such ordering is possible, an empty list can be returned.

Approach:
Using the dependencies of courses, prepare a directed graph.
Get the topological ordering of the graph formed.
If the topological ordering contains all nodes, all the courses can be completed in that order, which can be returned as an answer.
Otherwise, it is not possible to complete all the courses, so an empty list can be returned.

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
                
                # Add the node to queue if its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)
        
        # Return the result
        return ans

    # Function to determine order
    # of tasks to finish all tasks
    def findOrder(self, N, arr):
        
        # To store the graph
        adj = [[] for _ in range(N)]
        
        # Form the graph
        for u, v in arr:
            # Add the edge v-> u
            adj[v].append(u)
        
        # Get the topological ordering of graph
        topo = self.topoSort(N, adj)
        
        # If it doesn't contain all nodes,
        # it is impossible to finish all tasks
        if len(topo) < N:
            return []
        
        # Return the ordering otherwise
        return topo

# Example usage
N = 4
arr = [
    [1, 0],
    [2, 1],
    [3, 2]
]

sol = Solution()

# Function call to determine order
# of tasks to finish all tasks
ans = sol.findOrder(N, arr)

# Output
print("The order to perform tasks is:")
print(" ".join(map(str, ans)))

Complexity Analysis:
Time Complexity: O(V+E) (where V and E represent the number of nodes and edges in the given graph)
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
    def findOrder(self, N, arr):
        adj = [[] for _ in range(N)]
        for u, v in arr:
            # Add the edge v-> u
            adj[v].append(u)
        
        # Get the topological ordering of graph
        topo = self.topoSort(N, adj)
        if len(topo) < N:
            return []
        return topo

        