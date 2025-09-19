'''
Return the number of nodes in a binary tree given its root.



Every level in a complete binary tree possibly with the exception of the final one is fully filled, and every node in the final level is as far to the left as it can be. At the last level h, it can have 1 to 2h nodes inclusive.


Examples:
Input : root = [1, 2, 3, 4, 5, 6]

Output : 6

Explanation :



Input : root = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Output : 9

Explanation :



Input : [1, 2, 3]

Output:
3
Constraints:
1 <= Number of Node <= 5*104
-105 <= Node.val <= 105
The tree is guaranteed to be complete.

#Brute 
Intuition
A complete binary tree is one where every level is fully populated, except possibly for the last level, which is filled from left to right. To determine the total number of nodes in such a tree, a straightforward approach is to use a tree traversal method to count each node. For instance, an inorder traversal method visits nodes in the order of left subtree, current node, and right subtree. By keeping a count and incrementing it each time a node is visited, you can accurately tally the total number of nodes in the tree.



Approach
Start by setting up a variable to keep track of the total number of nodes in the tree, initializing it to 0.
**Define a Recursive Inorder Traversal Function:**
**Base Case:** If the current node is null, return immediately as this signifies that there are no more nodes to process in this path.
**Recursive Case:** If the current node is not null, first recursively visit the left subtree. After returning from the left subtree, increment the counter by 1 to account for the current node. Then, proceed to recursively visit the right subtree.
Invoke the recursive inorder traversal function starting from the root of the binary tree. Begin with the counter set to 0.
After completing the traversal, return the final value of the counter, which now holds the total number of nodes in the binary tree.
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to perform inorder
    # traversal and count nodes
    def inorder(self, root, count):
        # Base case: If the current
        # node is NULL, return
        if root is None:
            return

        # Increment count
        # for the current node
        count[0] += 1

        # Recursively call inorder
        # on the left subtree
        self.inorder(root.left, count)

        # Recursively call inorder
        # on the right subtree
        self.inorder(root.right, count)

    # Function to count nodes in the binary tree
    def count_nodes(self, root):
        # Base case: If the root is NULL,
        # the tree is empty, return 0
        if root is None:
            return 0

        # Initialize count variable to
        # store the number of nodes
        count = [0]

        # Call the inorder traversal
        # function to count nodes
        self.inorder(root, count)

        # Return the final count of
        # nodes in the binary tree
        return count[0]

if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    # Call the count_nodes function
    total_nodes = sol.count_nodes(root)

    # Print the result
    print(f"Total number of nodes in the Complete Binary Tree: {total_nodes}")

    
Complexity Analysis
Time Complexity:O(N) where N is the number of nodes in the binary tree. Each node is visited exactly once, ensuring a linear time complexity.

Space Complexity:O(N) where N is the number of nodes in the binary tree. The recursive stack may use space proportional to the number of nodes, especially in a skewed tree. For a balanced tree, the space complexity is roughly O(log N) as the maximum stack depth corresponds to the tree's height.

Intuition
Given the properties of a complete binary tree, where all levels except possibly the last are fully filled and the nodes on the last level are positioned from left to right, an optimized approach can be employed to determine the number of nodes using the tree's height. The maximum number of nodes in a complete binary tree can be calculated with the formula: (2^h - 1), where (h) is the height. For a perfectly filled last level (perfect binary tree), this formula directly applies. To check if the last level is completely filled, the heights of the left and right subtrees can be compared.

If the heights of the left and right subtrees are equal, it indicates that the last level is filled. If they differ, a recursive approach is used to calculate the nodes in the left and right subtrees and sum them up.



Approach
Base Case: If the current node is null, return 0, indicating there are no nodes to count at this point.
Recursive Calls: Compute the heights of the left and right subtrees by making recursive calls.
Check Heights: If the left height is equal to the right height, it indicates that the last level of the tree is completely filled. In this case, you can calculate the total number of nodes using the formula: (1 << lh) - 1, where << denotes the left shift operator.
Handle Incomplete Last Level: If the left height does not match the right height, it suggests that the last level is not fully populated. Here, you should recursively compute the number of nodes in both the left and right subtrees, and return the total count as 1 + countNodes(root->left) + countNodes(root->right).
Calculate Tree Heights: To determine the height of a subtree, initialize a height variable to 0. Traverse down the left or right side of the tree using a while loop, incrementing the height variable until reaching a leaf node. Return the final computed height.
# Definition for a binary tree node.
class TreeNode (object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to count nodes
    # in a binary tree
    def count_nodes(self, root):
        # Base case: If the root
        # is NULL, there are no nodes
        if root is None:
            return 0
        
        # Find the left height and
        # right height of the tree
        lh = self.find_height_left(root)
        rh = self.find_height_right(root)
        
        # Check if the last level
        # is completely filled
        if lh == rh:
            # If so, use the formula for
            # total nodes in a perfect
            # binary tree i.e. 2^h - 1
            return (1 << lh) - 1
        
        # If the last level is not completely
        # filled, recursively count nodes in
        # left and right subtrees
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
    
    # Function to find the left height of a tree
    def find_height_left(self, node):
        height = 0
        # Traverse left child until
        # reaching the leftmost leaf
        while node:
            height += 1
            node = node.left
        return height
    
    # Function to find the right height of a tree
    def find_height_right(self, node):
        height = 0
        # Traverse right child until
        # reaching the rightmost leaf
        while node:
            height += 1
            node = node.right
        return height

if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    # Call the count_nodes function
    total_nodes = sol.count_nodes(root)

    # Print the result
    print(f"Total number of nodes in the Complete Binary Tree: {total_nodes}")

Complexity Analysis
Time Complexity: O(log N * log N) where N is the number of nodes in the binary tree. Calculating leftHeight and rightHeight each takes O(log N) time. In the worst-case scenario, the recursive calls occur at most log N times, leading to a total time complexity of O(log N * log N).

Space Complexity:O(log N) where N is the number of nodes in the binary tree. The maximum depth of the recursion stack is equal to the tree's height, which is log N for a complete binary tree.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def count_nodes(self, root):
        if root is None:
            return 0
        lh = self.find_height_left(root)
        rh = self.find_height_right(root)
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def find_height_left(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def find_height_right(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
