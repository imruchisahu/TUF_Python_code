'''
Given root of binary tree, return the preorder traversal of the binary tree.



Morris preorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure.


Examples:
Input : root = [1, 4, null, 4 2]

Output : [1, 4, 4, 2]

Explanation :



Input : root = [1]

Output : [1]

Explanation : Only root node is present.

Constraints:
1 <= Number of Nodes <= 100
-100 Node.val <= 100

Intuition
To address this problem, it is crucial to understand the Morris Inorder Traversal technique for binary trees. Morris Inorder Traversal, known for its space efficiency, can be adapted to perform Preorder Traversal by modifying the traversal method. Specifically, in Preorder Morris Traversal, the value of the current node is printed before proceeding to its left child, but only if the right child of the inorder predecessor is null.

This modification maintains the core structure of Morris Traversal while ensuring that nodes are processed in the sequence required for Preorder Traversal. As a result, the traversal remains efficient, operating in constant space, as it does not require additional data structures.

Approach
Begin by initializing a pointer, current, to traverse the tree, and set it to the root node of the binary tree.
Perform the traversal while current is not null:
If the current node does not have a left child, print the value of the current node and move to its right child.
If the current node has a left child:
Identify the inorder predecessor of the current node, which is the rightmost node in the left subtree.
If the right child of this inorder predecessor is null, establish a temporary link by setting the right child of the inorder predecessor to the current node. Print the value of the current node and move to its left child.
If the right child of the inorder predecessor is not null, this indicates that the temporary link established earlier has been encountered. Therefore, revert the changes by setting the right child of the inorder predecessor back to null and proceed to the current node’s right child.
Continue this process until the traversal reaches the end of the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        # List to store the preorder traversal result
        preorder = []
        
        # Pointer to the current node, starting with the root
        cur = root
        
        # Iterate until the current node becomes None
        while cur:
            # If the current node has no left child
            # Add the value of the current node to the preorder list
            if not cur.left:
                preorder.append(cur.data)
                # Move to the right child
                cur = cur.right
            else:
            # If the current node has a left child
            # Create a pointer to traverse to the rightmost node in the left subtree
                prev = cur.left
                
            # Traverse to the rightmost node in the left subtree
            # or until we find a node whose right child is not yet processed
                while prev.right and prev.right != cur:
                    prev = prev.right
                
            # If the right child of the rightmost node is null
            # Set the right child of the rightmost node to the current node
            # Add the value of the current node to the preorder list and
            # move to the left child

                if not prev.right:
                    prev.right = cur
                    preorder.append(cur.data)
                    cur = cur.left

            # If the right child of the rightmost node is not null
            # Reset the right child to null
                else:
                    prev.right = None
                    cur = cur.right
        
        # Return the resulting preorder traversal list
        return preorder

# Example usage:
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(2)

sol = Solution()
preorder = sol.preorder(root)
print("Binary Tree Morris Preorder Traversal: ", preorder)

Complexity Analysis
Time Complexity: O(2N) where N is the number of nodes in the Binary Tree. The algorithm visits each node at most twice.

Space Complexity: O(1) The algorithm uses constant extra space for auxiliary variables.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        preorder = []
        cur = root
        while cur:
            if not cur.left:
                preorder.append(cur.data)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    preorder.append(cur.data)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return preorder