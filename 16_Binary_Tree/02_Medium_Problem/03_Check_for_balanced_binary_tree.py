'''
Given a binary tree root, find if it is height-balanced or not.



A tree is height-balanced if the difference between the heights of left and right subtrees is not more than one for all nodes of the tree. 


Examples:
Input : [3, 9, 20, null, null, 15, 7]

Output : Yes

Explanation :



Input : [1, 2, null, null, 3]

Output : No

Explanation :



Input : root = [5, 1, 2, 8, 3, null, 5, null, 4]

Output:
Yes
Constraints:
0 <= Number of Nodes <= 105
1 <= Node.val <= 105

#BRute
Intuition
A naive approach to solve this question would be to calculate for every node, the height of left and right subtree and then finding if the difference between the left and right heights is less than 1. If for every node, the difference comes out of be less than or equal to 1, the tree is balanced.

Algorithm
Calculate the height of a subtree using recursion.
For each node, compute the heights of the left and right subtrees.
If the difference in heights is more than one, the tree is not balanced.
If the difference in heights is more than one, the tree is not balanced.
If all nodes satisfy the balance condition, the tree is balanced.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Helper function to calculate height of a tree
    def height(self, root):
        # Base case: if root is null, height is 0
        if root is None:
            return 0
        # Height = 1 + max height of left and right subtrees
        return 1 + max(self.height(root.left), self.height(root.right))

    # Function to check if the tree is balanced
    def isBalanced(self, root):
        # Base case: an empty tree is balanced
        if root is None:
            return True

        # Find the height of left and right subtrees
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # Check if current node is balanced
        if abs(leftHeight - rightHeight) > 1:
            return False

        # Recursively check if left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Checking if the tree is balanced
    if solution.isBalanced(root):
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")

Complexity Analysis
Time Complexity: O(N2), where N is the number of nodes in the binary tree.
For every N node, the height() function is called twice that takes O(N) time in the worst case. Hence, the overall time complexity becomes O(N x N) = O(N2)

Space Complexity: O(N), because of the recursive stack space used.

#Optimal
Intuition
The O(N*N) time complexity of the previous method can be improved by incorporating the balance check directly within the tree traversal process. Instead of recalculating the heights of the left and right subtrees at each node repeatedly, these heights can be determined in a bottom-up fashion via postorder traversal. This method allows for the efficient validation of balance conditions during traversal, minimizing redundant computations and enabling the early identification of unbalanced nodes.

Algorithm Steps
Perform a postorder traversal of the Binary Tree using recursion: First visit the left subtree, then the right subtree, and finally the root node. During this traversal, compute the heights of the left and right subtrees for each node. Utilize these computed heights to verify the balance condition at the current node.
If, at any node, the absolute difference between the heights of the left and right subtrees exceeds 1, or if any subtree is determined to be unbalanced (returns -1), return -1 immediately, signaling that the tree is unbalanced.
For a balanced tree, return the height of the current node by taking the greater height of its left or right subtree and adding 1 to account for the current node itself.
Continue the traversal process until all nodes have been visited. The final result will either be the height of the entire tree if it is balanced, or -1 if the tree is found to be unbalanced at any point.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        # Function to check if the tree is balanced
        def dfsHeight(root):
            # Base case: if the current node is None,
            # return 0 (height of an empty tree)
            if not root:
                return 0

            # Recursively calculate the height of the left subtree
            leftHeight = dfsHeight(root.left)
            # If the left subtree is unbalanced,
            # propagate the unbalance status
            if leftHeight == -1:
                return -1

            # Recursively calculate the height of the right subtree
            rightHeight = dfsHeight(root.right)
            # If the right subtree is unbalanced,
            # propagate the unbalance status
            if rightHeight == -1:
                return -1

            # Check if the difference in height between left and right subtrees is greater than 1
            # If it's greater, the tree is unbalanced,
            # return -1 to propagate the unbalance status
            if abs(leftHeight - rightHeight) > 1:
                return -1

            # Return the maximum height of left and right subtrees, adding 1 for the current node
            return max(leftHeight, rightHeight) + 1

        # Check if the tree's height difference between subtrees is less than 2
        # If not, return False; otherwise, return True
        return dfsHeight(root) != -1

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Checking if the tree is balanced
    if solution.isBalanced(root):
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")

Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the Binary Tree.

Space Complexity: O(N) because of recursive stack space used.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def dfsHeight(root):
            if not root:
                return 0
            leftHeight = dfsHeight(root.left)
            if leftHeight == -1:
                return -1

            rightHeight = dfsHeight(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1
        return dfsHeight(root) != -1
