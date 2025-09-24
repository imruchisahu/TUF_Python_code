'''
Given the root node of a binary search tree (BST) and a value key. Return the root node of the BST after the deletion of the node with the given key value.



Note: As there can be many correct answers, the compiler returns true if the answer is correct, otherwise false.


Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , key = 3

Output : [5, 4, 6, 2, null, null, 7]

Explanation :

Below is image of the original BST





Below is image where the node 3 is deleted



Input : root = [5, 3, 6, 2, 4, null, 7] , key = 0

Output : [5, 3, 6, 2, 4, null, 7]

Explanation :

The tree does not have node with value 0.

Input : root = [5, 3, 6, 2, 4, null, 7] , key = 5

Output:
[4, 3, 6, 2, null, null, 7]
Constraints:
1 <= Number of nodes <= 104
-108 <= Node.val <= 108
All values in tree are unique.
-108 <= key <= 108

Intuition
Deleting a node in a Binary Search Tree (BST) requires addressing various scenarios based on the node's children. If the node has no children, it can be simply removed. If the node has one child, it is replaced by its single child. If the node has two children, the challenge is to maintain the BST properties. The node must be replaced by its in-order successor (the smallest node in the right subtree), which ensures the structure remains valid. The key task is to adjust the pointers of the parent node to reflect these changes, ensuring the integrity of the BST.

Approach
Implement a helper function, connector, to manage the replacement of a node with one or two children.
Within the connector function:
If the node has no left child, return the right child. This effectively removes the node while preserving the right subtree.
If the node has no right child, return the left child. This preserves the left subtree while removing the node.
If the node has both left and right children, locate the leftmost node in the right subtree (the in-order successor). Attach the left subtree of the node to be deleted to this leftmost node.
Return the right child of the node to be deleted as the new root of the subtree.
Within the deleteNode function:
Handle the case where the tree is empty by returning None.
If the root node matches the key to be deleted, invoke the connector function to handle the replacement.
Traverse the tree to locate the node with the specified key while adhering to BST properties. Adjust pointers accordingly to remove the node and preserve the BST structure.
Apply the connector function to the found node to complete its deletion and return the modified tree.

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    # Helper function to connect subtrees after deleting a node
    def connector(self, root):
        # If the node has no left child, return the right subtree.
        # This effectively removes the node by bypassing it with its right child.
        if not root.left:
            return root.right
        
        # If the node has no right child, return the left subtree.
        # This effectively removes the node by bypassing it with its left child.
        elif not root.right:
            return root.left
        
        # If the node has both left and right children, handle the case as follows:
        # 1. Save the left subtree in a temporary variable.
        # 2. Find the leftmost node in the right subtree.
        # 3. Attach the left subtree to the leftmost node in the right subtree.
        leftchild = root.left
        leftmost_child_in_right_subtree = root.right
        
        # Traverse to the leftmost node in the right subtree.
        while leftmost_child_in_right_subtree.left:
            leftmost_child_in_right_subtree = leftmost_child_in_right_subtree.left
        
        # Attach the left subtree to the leftmost node in the right subtree.
        leftmost_child_in_right_subtree.left = leftchild
        
        # Return the right subtree as the new root of the modified tree.
        return root.right

    # Function to delete a node with a specific key from the binary search tree.
    def deleteNode(self, root, key):
        # If the tree is empty, there is nothing to delete.
        if root is None:
            return None

        # If the node to be deleted is the root node, use the connector function.
        if root.data == key:
            return self.connector(root)
        
        # Traverse the tree to find the node to be deleted.
        node = root
        while node:
            # If the key to be deleted is smaller than the current node's data,
            # move to the left subtree.
            if node.data > key:
                # If the left child is the node to be deleted, update the left child.
                if node.left and node.left.data == key:
                    node.left = self.connector(node.left)
                    break
                else:
                    node = node.left 

            # If the key to be deleted is larger than the current node's data,
            # move to the right subtree.
            else:
                # If the right child is the node to be deleted, update the right child.
                if node.right and node.right.data == key:
                    node.right = self.connector(node.right)
                    break
                else:
                    node = node.right  
        
        # Return the modified tree with the node deleted.
        return root


# Example usage
if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    sol = Solution()
    # Delete node with key 3 from the tree
    root = sol.deleteNode(root, 3)


Complexity Analysis
Time Complexity: O(H), explanation is that the time complexity is dependent on the height of the tree.

Space Complexity: O(H), explanation is that the maximum depth of the recursion call stack is equal to the height of the tree.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def connector(self, root):

        if not root.left:
            return root.right

        elif not root.right:
            return root.left
        leftchild = root.left
        leftmost_child_in_right_subtree = root.right

        while leftmost_child_in_right_subtree.left:
            leftmost_child_in_right_subtree = leftmost_child_in_right_subtree.left
        leftmost_child_in_right_subtree.left = leftchild
        return root.right

    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.data == key:
            return self.connector(root)
    
        node = root
        while node:
            if node.data > key:
                if node.left and node.left.data == key:
                    node.left = self.connector(node.left)
                    break
                else:
                    node = node.left 
            else:
                if node.right and node.right.data == key:
                    node.right = self.connector(node.right)
                    break
                else:
                    node = node.right  
        return root