'''
Given a root of Binary Tree, perform the boundary traversal of the tree. 



The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.



The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:



The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.


If a node in the left boundary and has a left child, then the left child is in the left boundary.


If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.


The leftmost leaf is not in the left boundary.


The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.


Examples:
Input : root = [1, 2, 3, 4, 5, 6, 7, null, null, 8, 9]

Output : [1, 2, 4, 8, 9, 6, 7, 3]

Explanation :



Input : root = [1, 2, null, 4, 9, 6, 5, 3, null, null, null, null, null, 7, 8]

Output : [1, 2, 4, 6, 5, 7, 8]

Explanation :



Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[5, 1, 8, 6, 4, 5, 2]
Constraints:
0 <= Number of Nodes <= 104
-103 <= Node.val <= 103

Intuition
The boundary traversal algorithm aims to traverse the boundary of a binary tree in an anti-clockwise direction. The traversal is divided into three main parts: the left boundary, the bottom boundary (leaf nodes), and the right boundary. The left boundary traversal starts from the root and moves to the leftmost child, switching to the right child if the left is unavailable, until reaching a leaf node. The bottom boundary includes all leaf nodes using a simple preorder traversal. The right boundary traversal is similar to the left boundary but in the reverse direction, moving from the root to the rightmost child, and reversing the order of nodes in the result.

Approach
Boundary Traversal Diagram 1
Begin by initializing an empty array to collect the nodes encountered during the boundary traversal. Additionally, create a helper function designed to determine whether a node is a leaf, which helps to prevent the inclusion of duplicate nodes in the traversal.
Define a recursive function called addLeftBoundary and use a vector to keep track of nodes on the left boundary. Start this function at the root of the tree and proceed down the leftmost path until you reach a leaf node. For every non-leaf node encountered, append its value to the result list. Continue by traversing to the left child, and if the left child is not available, call the function on the right child.

Boundary Traversal Diagram 2
Next, create a recursive function named addLeafNodes and use a vector to store the nodes found at the bottom of the tree. When this function encounters a leaf node, add its value to the result list. Recursively visit the left and right subtrees of the current node following a preorder traversal pattern.

Boundary Traversal Diagram 3
Define another recursive function, addRightBoundary, and use a vector to capture nodes on the right boundary. Begin at the root and traverse the rightmost path of the tree until reaching a leaf node. For each non-leaf node, first attempt to traverse to its right child; if that child is unavailable, move to the left child. As the recursion returns, add the current node's value to the result list.

Boundary Traversal Diagram 4
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    # Function to check if a node is a leaf
    def isLeaf(self, root):
        return not root.left and not root.right

    # Function to add the left boundary of the tree
    def addLeftBoundary(self, root, res):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    # Function to add the right boundary of the tree
    def addRightBoundary(self, root, res):
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])

    # Function to add the leaves of the tree
    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    # Main function to perform the boundary traversal of the binary tree
    def boundary(self, root):
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.data)

        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res

# Helper function to print the result
def printResult(result):
    for val in result:
        print(val, end=" ")
    print()

# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()

# Get the boundary traversal
result = solution.boundary(root)

# Print the result
print("Boundary Traversal: ", end="")
printResult(result)

Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This is due to traversing the left boundary, bottom nodes, and right boundary sequentially, each operation being at most O(N).

Space Complexity: O(N) for storing boundary nodes and auxiliary recursion stack space in the worst-case scenario of a skewed tree.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    # Function to add the left boundary of the tree
    def addLeftBoundary(self, root, res):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    # Function to add the right boundary of the tree
    def addRightBoundary(self, root, res):
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])

    # Function to add the leaves of the tree
    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    def boundary(self, root):
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.data)

        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res
    