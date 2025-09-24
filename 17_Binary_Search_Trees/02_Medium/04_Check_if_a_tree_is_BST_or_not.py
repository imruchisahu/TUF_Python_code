'''
Given the root node of a binary tree. Return true if the given binary tree is a binary search tree(BST) else false.



A valid BST is defined as follows:



The left subtree of a node contains only nodes with key strictly less than the node's key.


The right subtree of a node contains only nodes with key strictly greater than the node's key.


Both the left and right subtrees must also be binary search trees.

Examples:
Input : root = [5, 3, 6, 2, 4, null, 7]

Output : true

Explanation :

Below is image of the given tree.



Input : root = [5, 3, 6, 4, 2, null, 7]

Output : false

Explanation :

﻿Below is image of the given tree.

The node 4 and node 2 violates the BST rule of smaller to left and larger to right.



Input : root = [2, 1, 3]

Output:
true
false

Submit
Constraints:
1 <= Number of Nodes <= 104
-231 <= Node.val <= 231 - 1

Intuition
To determine if a binary tree is a Binary Search Tree (BST), we need to ensure that for every node, its value falls within a specific range. This range is defined by the values of its parent nodes and their subtrees. For a node to be valid in a BST, all nodes in its left subtree must have values less than the node’s value, and all nodes in its right subtree must have values greater than the node’s value.

A straightforward way to approach this is to perform an inorder traversal of the tree, which will visit nodes in ascending order if the tree is a BST. By collecting node values in this order and then checking if this list is sorted, we can confirm whether the tree is a BST.

Approach
Define a range for each node, every node must satisfy a range of valid values. The root node is initially allowed to have any value within the range from negative infinity to positive infinity.
Start with the root node and ensure its value is within the defined range.
Recursively validate the subtrees. For the left subtree of a node, update the range to be from negative infinity to the node’s value. For the right subtree of a node, update the range to be from the node’s value to positive infinity.
Ensure that each node’s value falls within its updated range. Recursively apply the same checks to the left and right children of each node.
If all nodes satisfy their respective ranges, the tree is a BST and if any node fails the check, the tree is not a BST.
# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
    def isBST(self, root):
        # Helper function to validate the BST
        def validate(node, min_val, max_val):
            # Base case: if the node is None, return True
            if not node:
                return True
            
            # Check if the node's value falls within the valid range
            if node.data <= min_val or node.data >= max_val:
                return False
            
            # Recursively validate the left subtree
            # Update the max value to the current node's value
            left_is_valid = validate(node.left, min_val, node.data)
            
            # Recursively validate the right subtree
            # Update the min value to the current node's value
            right_is_valid = validate(node.right, node.data, max_val)
            
            # Both subtrees must be valid for the tree to be a BST
            return left_is_valid and right_is_valid
        
        # Initial call with the full range of values
        return validate(root, float('-inf'), float('inf'))

# Main method for testing
root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(10)
root.left.left = TreeNode(3)
root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(15)

solution = Solution()
print(solution.isBST(root))  # Output: False


Complexity Analysis
Time Complexity O(N), Each node in the tree is visited once during the inorder traversal.

Space Complexity O(N), The recursive call stack can go up to the depth of the tree and the ans list can also store N elements in the worst case.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.data <= min_val or node.data >= max_val:
                return False
            left_is_valid = validate(node.left, min_val, node.data)
            right_is_valid = validate(node.right, node.data, max_val)
            
            # Both subtrees must be valid for the tree to be a BST
            return left_is_valid and right_is_valid
        return validate(root, float('-inf'), float('inf'))
    
    