'''
Assuming standing on the right side of a binary tree and given its root, return the values of the nodes visible, arranged from top to bottom.


Examples:
Input : root = [1, 2, 3, null, 5, null, 4]

Output : [1, 3, 4]

Explanation :



Input : root = [1, 2, 3, 6, 5, 8, 4]

Output : [1, 3, 4]

Explanation :



Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[5, 2, 5, 6]
Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103

Intuition
The goal is to traverse a binary tree in a way that captures the nodes visible from the left and right perspectives. By utilizing a level-order traversal, each level of the tree is processed independently, ensuring that the structure and relationships between nodes are preserved. This traversal is facilitated using a queue to keep track of nodes at each level, allowing for a systematic exploration from the root to the deepest leaves. By maintaining a 2D array to record the nodes at each level, the left and right views can be easily extracted by focusing on the first and last nodes at each level, respectively.

Approach
Initialize an empty queue for storing nodes during traversal and a 2D array (or vector of vectors) for the level order traversal.
If the tree is empty, return the empty 2D array and enqueue the root node into the queue.
While the queue is not empty:
Determine the current size of the queue, representing the number of nodes at the current level.
Create a vector to store the nodes at the current level.
For each node at the current level, dequeue the front node from the queue. Add the node’s value to the level vector. Enqueue the left and right children of the current node, if they exist.
After processing all nodes at the current level, add the level vector to the 2D array.
To obtain the left view, extract the first element from each level's vector and store it in a separate array. This array represents the left view of the binary tree.
To obtain the right view, extract the last element from each level's vector and store it in a separate array. This array represents the right view of the binary tree.
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to return the Right view of the binary tree
    def rightSideView(self, root):
        res = []

        # Get the level order traversal of the tree
        levelTraversal = self.levelOrder(root)

        # Iterate through each level and add the last element to the result
        for level in levelTraversal:
            res.append(level[-1])

        return res

    # Function to return the Left view of the binary tree
    def leftSideView(self, root):
        res = []

        # Get the level order traversal of the tree
        levelTraversal = self.levelOrder(root)

        # Iterate through each level and add the first element to the result
        for level in levelTraversal:
            res.append(level[0])

        return res

    # Function that returns the level order traversal of a Binary tree 
    def levelOrder(self, root):
        ans = []

        # Return an empty list if the tree is empty
        if not root:
            return ans

        # Use a queue to perform level order traversal
        q = deque([root])

        while q:
            size = len(q)
            level = []

            # Process each node in the current level
            for i in range(size):
                top = q.popleft()
                level.append(top.data)

                # Enqueue the left child if it exists
                if top.left:
                    q.append(top.left)

                # Enqueue the right child if it exists
                if top.right:
                    q.append(top.right)

            # Add the current level to the result
            ans.append(level)

        return ans

# Main method to test the functionality
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    solution = Solution()

    # Get the Right View traversal
    rightView = solution.rightSideView(root)

    # Print the result for Right View
    print("Right View Traversal:", end=" ")
    for node in rightView:
        print(node, end=" ")
    print()

    # Get the Left View traversal
    leftView = solution.leftSideView(root)

    # Print the result for Left View
    print("Left View Traversal:", end=" ")
    for node in leftView:
        print(node, end=" ")
    print()

Complexity Analysis
Time Complexity: O(N): Each node in the binary tree is processed exactly once, either enqueued or dequeued, resulting in a linear time complexity relative to the number of nodes, N.

Space Complexity: O(N): The space complexity is determined by the maximum number of nodes stored in the queue at any point during the traversal. In the worst case, this could be all nodes of the last level of the binary tree, which could amount to N/2 nodes.

#Optimal Approach
Intuition
To obtain the left and right views of a binary tree, a depth-first traversal is employed. This approach tracks the level of each node, ensuring that only the first node encountered at each level is included in the result. For both views, the traversal starts from the root and progresses through each level, capturing the required nodes based on the traversal order. The left view prioritizes left children first, while the right view prioritizes right children first.

Approach
Algorithm for Left View
Begin by initializing an empty vector named res to hold the nodes visible from the left view of the binary tree.
Implement a recursive depth-first search (DFS) approach to traverse the tree:
Base Case: If the current node is null, terminate the recursion as this indicates the end of a vertical level.
Recursive Function: Define the function to accept the current node, its vertical level, and the result vector res as parameters.
Within the recursive function, check if the size of res is equal to the current level. If true, add the value of the current node to res, as this is the first node encountered at this vertical level.
Proceed by making a recursive call to the function for the left child of the current node, followed by the right child, incrementing the level by 1 for each call. This ensures nodes are processed from top to bottom, left to right.
Continue the recursion process until all nodes are traversed and the base case is encountered. Return the vector res, which will now contain the nodes visible from the left view of the tree.

Left View of Binary Tree
Algorithm for Right View
Start by initializing an empty vector named res to store the nodes visible from the right view of the binary tree.
Implement a recursive depth-first search (DFS) approach for traversal:
Base Case: If the current node is null, return from the recursion, indicating the end of the current vertical level.
Recursive Function: The function should accept the current node, its vertical level, and the result vector res as arguments.
Within the recursive function, check if the size of res matches the current level. If so, add the current node's value to res, as this node is the first encountered at this vertical level from the right side.
Make a recursive call for the right child of the current node first, followed by the left child, incrementing the level by 1 for each recursive call. This ensures that nodes on the right side are prioritized, providing the right view.
Continue the recursive process until all nodes have been visited and the base case is reached. Finally, return the vector res, which now includes the nodes visible from the right view of the binary tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to return the Right view of the binary tree
    def rightSideView(self, root):
        res = []
        
        # Call the recursive function to populate the right-side view
        self.recursionRight(root, 0, res)
        
        return res

    # Function to return the Left view of the binary tree
    def leftSideView(self, root):
        res = []
        
        # Call the recursive function to populate the left-side view
        self.recursionLeft(root, 0, res)
        
        return res

    # Recursive function to traverse the binary tree and populate the left-side view
    def recursionLeft(self, root, level, res):
        # Check if the current node is NULL
        if root is None:
            return
        
        # Check if the size of the result list is equal to the current level
        if len(res) == level:
            # If equal, add the value of the current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the left child with an increased level
        self.recursionLeft(root.left, level + 1, res)
        
        # Recursively call the function for the right child with an increased level
        self.recursionLeft(root.right, level + 1, res)

    # Recursive function to traverse the binary tree and populate the right-side view
    def recursionRight(self, root, level, res):
        # Check if the current node is NULL
        if root is None:
            return
        
        # Check if the size of the result list is equal to the current level
        if len(res) == level:
            # If equal, add the value of the current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the right child with an increased level
        self.recursionRight(root.right, level + 1, res)
        
        # Recursively call the function for the left child with an increased level
        self.recursionRight(root.left, level + 1, res)

# Main method to test the functionality
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    solution = Solution()

    # Get the Right View traversal
    rightView = solution.rightSideView(root)

    # Print the result for Right View
    print("Right View Traversal:", end=" ")
    for node in rightView:
        print(node, end=" ")
    print()

    # Get the Left View traversal
    leftView = solution.leftSideView(root)

    # Print the result for Left View
    print("Left View Traversal:", end=" ")
    for node in leftView:
        print(node, end=" ")
    print()

Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree.
As each node is visited once and for each node, we perform a constant amount of work (checking conditions and making at most two recursive calls). Thus, the time complexity is O(N).

Space Complexity: O(H), where H is the height of the binary tree.
Because of the recursive stack space which depends on the height of the tree.

Note:
In a balanced tree, height H is nearly equal to logN. Hence, the best-case space complexity is O(logN).
In a skewed tree, height H is almost equal to N. Hence, the worst-case space complexity turns out to be O(N).

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        res=[]
        self.recursionRight(root, 0, res)
        return res
    def leftSideView(self, root):
        res =[]
        self.recursionLeft(root, 0, res)
        return res

    def recursionLeft(self, root, level, res):
        if root is None:
            return
        if len(res) == level:
            res.append(root.data)
        self.recursionLeft(root.left, level + 1, res)
        self.recursionLeft(root.right, level + 1, res)

    def recursionRight(self, root, level, res):
        if root is None:
            return
        if len(res) == level:
            res.append(root.data)
        self.recursionRight(root.right, level + 1, res)
        self.recursionRight(root.left, level + 1, res)

