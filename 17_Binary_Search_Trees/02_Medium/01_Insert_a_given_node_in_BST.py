'''
Given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion.



It is guaranteed that the new value does not exist in the original BST. Note that the compiler output shows true if the node is added correctly, else false.


Examples:
Input : root = [4, 2, 7, 1, 3] , val = 5

Output : [4, 2, 7, 1, 3, 5]

Explanation :

Below is image where the node 5 is inserted





There is another way to insert the given val as shown below.



Input : root = [40, 20, 60, 10, 30, 50, 70] , val = 25

Output : [40, 20, 60, 10, 25, 50, 70, null, null, null, 30]

Explanation :

Below is image where the node 25 is inserted



Input : root = [4, 2, 7, 1, null, 6] , val = 3

Output:
[4, 2, 7, 1, 3, 6]
Constraints:
1 <= Number of nodes <= 104
-108 <= Node.val <= 108
All values in tree are unique.
-108 <= val <= 108
It is guaranteed that the val does not exists in original BST.

Intuition
The goal is to insert a new value into a Binary Search Tree (BST) while ensuring that the fundamental properties of the BST are preserved. A BST is organized in such a way that for any given node, all values in its left subtree are smaller than the node's value, and all values in the right subtree are larger. The insertion process requires identifying the correct location for the new value, ensuring that the tree remains correctly ordered. This involves traversing the tree, making comparisons at each node, and ultimately finding an appropriate null child position where the new node can be inserted, thereby maintaining the structure and properties of the BST.

Approach
Initiate a traversal of the tree to locate the correct insertion point by comparing the value to be inserted with the value of the current node.
If the value to be inserted is less than the value of the current node, proceed to explore the left subtree.
If the value to be inserted is greater than the value of the current node, proceed to explore the right subtree.
Continue this comparison and traversal process until a potential leaf position (a null child) is identified in the relevant subtree.
To insert the new value, create a new node containing the given value, and attach this new node as a child of the parent node at the empty position found in the previous step. If the value is less than the parent's node value, the new node should be attached as the left child; otherwise, it should be attached as the right child.
Return the updated Binary Search Tree, now including the newly inserted value while maintaining its properties.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Recursive function to insert a value into the BST
    def solve(self, node, val):
        # If the current node is None, create a new TreeNode with the given value
        if node is None:
            return TreeNode(val)
        
        # Traverse the tree to find the correct insertion point
        if val < node.data:
            # Move to the left subtree
            node.left = self.solve(node.left, val)
        elif val > node.data:
            # Move to the right subtree
            node.right = self.solve(node.right, val)
        
        # Return the (potentially modified) node
        return node
    
    # Public method to start the insertion process
    def insertIntoBST(self, root, val):
        return self.solve(root, val)

# Helper function to print the tree in-order
def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)

# Main function for testing
if __name__ == "__main__":
    solution = Solution()
    
    # Create a sample BST: [4, 2, 7, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    val = 5
    # Insert the value into the BST
    newRoot = solution.insertIntoBST(root, val)
    
    # Print the BST in-order to verify the insertion
    printInOrder(newRoot)

Complexity Analysis
Time Complexity: O(H), where H is the height of the tree, which in the worst case can be N (for a skewed tree), but for a balanced BST, it will be log(N).
Space Complexity: O(1) Only a constant amount of space is used to store the current node and the new node, regardless of the size of the input tree.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:

    def solve(self, node, val):
        if node is None:
            return TreeNode(val)
        
        if val < node.data:
            node.left = self.solve(node.left, val)
        elif val > node.data:
            node.right = self.solve(node.right, val)
        return node

    def insertIntoBST(self, root, val):
        return self.solve(root, val)
    