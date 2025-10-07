'''
Given an array nums consisting of non-negative integers and a queries array, where queries[i] = [xi, mi].



The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.



Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.


Examples:
Input : nums = [4, 9, 2, 5, 0, 1] , queries = [ [3, 0], [3, 10], [7, 5], [7,9] ]



Output : [3, 10, 7, 14]



Explanation :

1st query : x = 3, m = 0. There are only one numbers less than equal to m i.e 0. 0 XOR 3 = 3. The answer is 3.

2nd query : x = 3, m = 10. The maximum XOR is 3 XOR 9 = 10.

3rd query : x = 7, m = 5. The maximum XOR is 7 XOR 0 = 7.

4th query : x = 7, m = 9. The maximum XOR is 7 XOR 9 = 14.

Input : nums = [0, 1, 2, 3, 4] , queries = [ [3, 1], [1, 3], [5, 6] ]



Output : [3, 3, 7]



Explanation :

1st query : x = 3, m = 1. There are only two numbers less than equal to m i.e 0 , 1. 0 XOR 3 = 3, 1 XOR 3 = 2. The larger value is 3.

2nd query : x = 1, m = 3. The maximum XOR is 1 XOR 2 = 3

3rd query : x = 5, m = 6. The maximum XOR is 5 XOR 2 = 7.

Input : nums = [5, 2, 4, 6, 6, 3] , queries = [ [12, 4], [8, 1], [6, 3] ]

Output:
[15, -1, 5]

Constraints:
1 <= nums.length , queries.length <= 105
queries[i].length == 2
0 <= nums[i] , xi , mi <= 109

Intuition
We can efficiently solve this problem by using a Trie data structure, where each node represents a bit and paths from the root to the leaves represent binary numbers. The aim is to maximize the XOR value between a given number and any number in the array that is less than or equal to a specified limit.
By incrementally inserting numbers into the Trie up to the required value for each query, unnecessary operations are minimized. This approach allows for efficiently finding the maximum XOR for each query by traversing the Trie and selecting opposite bits whenever possible, ensuring the highest possible XOR result. If no numbers are less than or equal to the specified limit, the result is -1.
Approach
Build a Trie Node to hold binary bits (0 and 1), and add methods to insert numbers and find the maximum XOR value.
Set up a list to store query results, and sort the numbers and queries by their limits. This way, we only insert necessary numbers into the Trie.
Go through the sorted numbers and queries. For each query, add numbers to the Trie up to the query's limit and use the Trie to find the highest XOR value for the query.
After all queries are processed, return the results. This method ensures we handle each query efficiently.

# Node Structure for Trie
class Node:
    def __init__(self):
        # Initialize child links (0 and 1)
        self.links = [None, None]

    # Check if a child node exists at a given index (0 or 1)
    def contains_key(self, ind):
        return self.links[ind] is not None

    # Get the child node at a given index (0 or 1)
    def get(self, ind):
        return self.links[ind]

    # Set the child node at a given index (0 or 1)
    def put(self, ind, node):
        self.links[ind] = node

# Definition for Trie data structure
class Trie:
    def __init__(self):
        # Initialize root node
        self.root = Node()

    # Function to insert a number into the trie
    def insert(self, num):
        # Start traversal
        node = self.root

        # Traverse each bit of the number
        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            # If the current node doesn't have a child node at the current bit, create one
            if not node.contains_key(bit):
                node.put(bit, Node())

            # Move to the child node corresponding to the current bit
            node = node.get(bit)

    # Function to find the maximum XOR value achievable with a given number
    def find_max(self, num):
        node = self.root
        max_num = 0

        # Traverse each bit of the number
        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            # If there exists a different bit in the trie at the current position, choose it to maximize XOR
            if node.contains_key(1 - bit):
                max_num = max_num | (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)

        # Return the maximum XOR value
        return max_num

# Solution class to handle queries
class Solution:
    # Function to handle the maximize XOR queries
    def maximizeXor(self, nums, queries):
        # Initialize list to store results of queries
        ans = [0] * len(queries)

        # List to store offline queries
        offline_queries = []

        # Sort the array of numbers
        nums.sort()

        # Convert queries to offline queries and store them in a list
        for index, query in enumerate(queries):
            offline_queries.append((query[1], query[0], index))

        # Sort queries based on their end points
        offline_queries.sort()

        i = 0
        trie = Trie()

        # Process each query
        for m, x, query_index in offline_queries:
            # Insert numbers into the trie until the current query's end point
            while i < len(nums) and nums[i] <= m:
                trie.insert(nums[i])
                i += 1

            # If there are numbers inserted into the trie, find the maximum XOR value for the query range
            if i != 0:
                ans[query_index] = trie.find_max(x)
            else:
                ans[query_index] = -1

        # Return results
        return ans

# Main function to test the Solution class
if __name__ == "__main__":
    # Create instance of Solution class
    sol = Solution()

    # Input array of numbers
    nums = [0, 1, 2, 3, 4]

    # Queries in the form of [x, m]
    queries = [[3, 1], [1, 3], [5, 6]]

    # Get the results of the maximize XOR queries
    result = sol.maximizeXor(nums, queries)

    # Output the results
    print("Result of Max XOR Queries:")
    for i in range(len(result)):
        print(f"Query {i + 1}: {result[i]}")

Complexity Analysis
Time Complexity: O(32N + Q(logQ) + 32Q) where N is the size of the input array and Q is the number of queries. The time complexity includes inserting N numbers into the Trie, each taking O(32) operations due to the 32-bit integer representation, resulting in O(32N). Sorting the Q queries takes O(Q(logQ)) time. Processing each query involves traversing the 32-bit Trie, resulting in O(32Q).

Space Complexity: O(32N + Q) where N is the size of the input array and Q is the number of queries. The space complexity accounts for storing N numbers in the Trie (32N) and the storage needed for the Q queries.

'''
class Node:
    def __init__(self):
        self.links = [None, None]
    def contains_key(self, ind):
        return self.links[ind] is not None

    def get(self, ind):
        return self.links[ind]

    def put(self, ind, node):
        self.links[ind] = node

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if not node.contains_key(bit):
                node.put(bit, Node())
            node = node.get(bit)

    def find_max(self, num):
        node = self.root
        max_num = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.contains_key(1 - bit):
                max_num = max_num | (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return max_num

class Solution:
    def maximizeXor(self, nums, queries):
        ans = [0] * len(queries)
        offline_queries = []
        nums.sort()
        for index, query in enumerate(queries):
            offline_queries.append((query[1], query[0], index))
        offline_queries.sort()

        i = 0
        trie = Trie()
        for m, x, query_index in offline_queries:
            while i < len(nums) and nums[i] <= m:
                trie.insert(nums[i])
                i += 1
            if i != 0:
                ans[query_index] = trie.find_max(x)
            else:
                ans[query_index] = -1
        return ans