'''
Given root of the binary tree, return its maximum depth.



A binary tree's maximum depth is number of nodes along the longest path from root node down to the farthest node.


Examples:
Input : root = [1, 2, 3, null, null, null , 6]

Output : 3

Explanation : The path from root node 1 to node with value 6 has maximum depth with 3 nodes along path.



Input : root = [3, 9, 20, null, null, 15 , 7]

Output : 3

Explanation : The path from root node 3 to node with value 15 has maximum depth with 3 nodes along path.

There exists other paths to reach the solution.



Input : root = [5, 1, 2, 8, null, null, 5, null, 4, null, null, 7]

Output:
5
Constraints:
1 <= Number of Nodes <= 104
0 <= Node.val <= 104

#REcursive Approach
ntuition
To find the maximum height of a binary tree a possible solution is using a recursive approach to divide the tree into smaller sub-trees. By finding the depth of these sub-trees and combining them, determine the depth of the entire tree. For each node in the tree, find the maximum depth of the left and right subtree, take the larger of these two depths, and add one (for the current node).

Approach
If the current node is null (meaning there is no node), return 0. This is the base case of our recursion.
Recursively find the maximum depth of the left sub-tree and the maximum depth of the right sub-tree.
The depth of the current node is 1 (for the current node itself) plus the maximum of the depths of the left and right sub-trees.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # Base case: if the node is null, return 0
        if root is None:
            return 0
        # Recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # The depth of the tree is 1 current node + the maximum depth of the subtrees
        return 1 + max(left, right)

# Main method to test the function
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Maximum Depth:", solution.maxDepth(root))

        if root is None:
            return 0
        # Recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # The depth of the tree is 1 current node + the maximum depth of the subtrees
        return 1 + max(left, right)

# Main method to test the function
if __name__ == "__main__":

Complexity Analysis:
Time Complexity: O(N), the recursive solution visits each node once, leading to O(N) time complexity.

Space Complexity: O(h), it uses O(h) space due to the recursive function calls on the stack, where h is the height of the tree.

#Iterative Approach
Intuition
To determine the maximum depth of a binary tree using level order traversal, envision the process as a breadth-first exploration. Begin by initializing a queue and placing the root node into it. As each level of the tree is traversed, keep track of the depth by counting the number of levels visited. At each level, remove nodes from the queue and add their left and right children. Increment the depth counter as the level progresses. This exploration continues until there are no more levels to visit, at which point the depth counter will indicate the maximum depth of the tree.

Strategy
Begin by setting up a queue for level order traversal and a variable called depth to keep track of the tree's depth. If the root is null, return 0, indicating that the tree is empty. Otherwise, add the root node to the queue and initialize depth to 0.
Continue processing as long as the queue is not empty: Increment depth by 1 to advance to the next level. For each node at the current level (based on the number of elements in the queue), remove the node from the front of the queue and enqueue its left and right children if they are present.
Once the loop completes, return depth, which indicates the maximum depth of the tree.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # If the tree is empty, return 0
        if root is None:
            return 0

        # Create a queue to hold nodes to be processed
        q = deque([root])
        # Initialize level to 0
        level = 0

        # While there are nodes in the queue
        while q:
            # Get the number of nodes at the current level
            size = len(q)

            # Process all nodes at the current level
            for _ in range(size):
                # Get the front node in the queue
                front = q.popleft()

                # Enqueue left child if it exists
                if front.left is not None:
                    q.append(front.left)

                # Enqueue right child if it exists
                if front.right is not None:
                    q.append(front.right)
            # Increment level to move to the next level
            level += 1

        # Return the maximum depth
        return level

# Main method to test the function
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Maximum Depth:", solution.maxDepth(root))

Complexity Analysis:
Time Complexity: O(N), the iterative solution processes each node once, resulting in O(n) time complexity.

Space Complexity: O(w), where w is the maximum width of the tree


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)