'''
Given a sorted dictionary of an alien language having N words and K starting alphabets of a standard dictionary. Find the order of characters in the alien language.

There may be multiple valid orders for a particular test case, thus you may return any valid order as a string. The output will be True if the order returned by the function is correct, else False denoting an incorrect order. If the given arrangement of words is inconsistent with any possible letter ordering, return an empty string "".


Examples:
Input: N = 5, K = 4, dict = ["baa","abcd","abca","cab","cad"]

Output: b d a c

Explanation: 

We will analyze every consecutive pair to find out the order of the characters.

The pair “baa” and “abcd” suggests ‘b’ appears before ‘a’ in the alien dictionary.

The pair “abcd” and “abca” suggests ‘d’ appears before ‘a’ in the alien dictionary.

The pair “abca” and “cab” suggests ‘a’ appears before ‘c’ in the alien dictionary.

The pair “cab” and “cad” suggests ‘b’ appears before ‘d’ in the alien dictionary.

So, [‘b’, ‘d’, ‘a’, ‘c’] is a valid ordering.

Input: N = 3, K = 3, dict = ["caa","aaa","aab"]



Output: c a b



Explanation: Similarly, if we analyze the consecutive pair 

for this example, we will figure out [‘c’, ‘a’, ‘b’] is 

a valid ordering.

Input: N = 3, K = 3, dict = ["abc", "bca", "cab"]

Output:
b c a
c b a
a b c
a c b

Submit
Constraints:
1 ≤ N, M ≤ 300
1 ≤ K ≤ 26
1 ≤ dict[i].length ≤ 50

Intuition:
How this problem can be identified as a Graph problem?
The problem suggests that there exists the ordering of different words based on the alien dictionary. Also, it is asked to find out the ordering of letters based on the dictionary. The concept of ordering of nodes can be solved using Topological sort which comes under the topic of Graphs.
How to form the graph?
Here, the letters can be represented as nodes of the graph.

To understand the edges, consider example 1 where
N=5, K=4, dict = {"baa", "abcd", "abca", "cab", "cad"}

Considering the first two words "baa" and "abcd", it is clear that they are differentiated by the first letter i.e. 'b' and 'a'. Thus, a directed edge can be inserted in the graph from node 'b' to node 'a' representing that letter 'b' must appear before the letter 'a' in the ordering as shown in the figure:


By comparing pairs of words in the dictionary, edges can be added to the graph.
Note:
It is not required to check every pair of words possible to add the edges to the graph. Instead just checking the differentiating letter in consecutive pairs will work as well as shown in the image:

Edge Case:
The problem arises when the value of K becomes 5 and there is no word in the dictionary containing the letter 'e'. In this case, a separate node with the value 'e' can be added in the graph and it will be considered a component of the directed graph like the following, and the same algorithm will work fine for multiple components.


Approach:
Initialise a graph with nodes equal to the number of required letters. The letters from 'a' to 'z' can be represented as numbers from 0 to 26 for easier understanding.
Compare the consecutive pair of words, and find the differentiating letter. Compare the letters to add an edge to the graph.
Once the graph is prepared, get the topological ordering of the graph formed.
The ordering of letters obtained from the topological sorting, will be the ordering of letters based on the alien dictionary.

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

    # Function to determine order of 
    # letters based on alien dictionary
    def findOrder(self, dict, N, K):
        
        # Initialise a graph of K nodes
        adj = [[] for _ in range(K)]
        
        # Compare the consecutive words
        for i in range(N - 1):
            
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))
            
            # Compare the pair of strings letter by 
            # letter to identify the differentiating letter
            for ptr in range(length):
                
                # If the differentiating letter is found
                if s1[ptr] != s2[ptr]:
                    
                    # Add the edge to the graph
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                    break
        
        # Get the topological sort 
        # of the graph formed
        topo = self.topoSort(K, adj)
        
        # To store the answer
        ans = ""
        
        for i in range(K):
            # Add the letter to the result
            ans += chr(ord('a') + topo[i])
            ans += ' '
        
        # Return the answer
        return ans

# Example usage
N = 5
K = 4
dict = [
    "baa", "abcd", "abca", "cab", "cad"
]

sol = Solution()
ans = sol.findOrder(dict, N, K)

# Output
print("The order to characters as per alien dictionary is:", ans)

Complexity Analysis:
Time Complexity: O(K+N) (where K and N represents the number of nodes and edges in the given graph)
Forming the graph takes O(N*len) time, where len is the average length of a word in the dictionary.
Finding topological sort takes O(K+N) time.
Space Complexity: O(K+N)
Storing the graph takes O(N) space.
Topological sorting algorithm uses extra O(K) computational space.
Follow-up question for interview:
When is the ordering of letters not possible:
If every character matches and the largest word appears before the shortest word: For example, if “abcd” appears before “abc”, we can say the ordering is not possible.
If there exists a cyclic dependency between the characters: For example, in the dictionary: dict: {“abc”, “bat”, “ade”} there exists a cyclic dependency between 'a' and 'b' because the dictionary states 'a' < 'b' < 'a', which is not possible.

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

    # Function to determine order of 
    # letters based on alien dictionary
    def findOrder(self, dict, N, K):
        
        # Initialise a graph of K nodes
        adj = [[] for _ in range(K)]
        
        # Compare the consecutive words
        for i in range(N - 1):
            
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))
            
            # Compare the pair of strings letter by 
            # letter to identify the differentiating letter
            for ptr in range(length):
                
                # If the differentiating letter is found
                if s1[ptr] != s2[ptr]:
                    
                    # Add the edge to the graph
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                    break
        
        # Get the topological sort 
        # of the graph formed
        topo = self.topoSort(K, adj)
        
        # To store the answer
        ans = ""
        
        for i in range(K):
            # Add the letter to the result
            ans += chr(ord('a') + topo[i])
            ans += ' '
        
        # Return the answer
        return ans

       
