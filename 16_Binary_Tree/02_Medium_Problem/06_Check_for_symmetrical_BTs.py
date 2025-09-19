'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Examples:
Input : root = [1, 2, 2, 3, 4, 4, 3]

Output : true

Explanation :



Input : root = [1, 2, 2, null, 3, null, 3]

Output : false

Explanation : When a straight line is drawn through the root node and the tree is folded around it, the rightmost node 3 is overlapped with null node and the node 3 present at left of root node is overlapped with null nodes.

So both node 3 in tree does not show symmetric behaviour.



Input: root = [1, 2, 3]



Output:
true
false

Submit
Constraints:
1<= Number of Nodes <= 104
-100 <= Node.val <= 100
Intuition
A tree is considered symmetric if its structure exhibits a mirroring pattern, where the left and right subtrees of each node are either identical or mirror images of each other. To verify the symmetry of a tree recursively, begin by comparing the root node's left and right subtrees. Then, for each pair of subtrees, ensure that the left child of the left subtree is a mirror image of the right child of the right subtree, and similarly, the right child of the left subtree mirrors the left child of the right subtree. This mirroring must be consistent throughout the entire tree to confirm its symmetry.

Algorithm Steps
First, check if the tree is empty by verifying if the root node is null. If the tree is empty, return true because an empty tree is symmetric by default.
If the tree is not empty, invoke a utility function, passing the left and right subtrees of the root node. This function will handle the recursive checks necessary to determine symmetry.
The base case in the recursive function occurs when both the left and right subtrees are null, in which case the function should return true. However, if only one subtree is null while the other is not, return false, as this indicates asymmetry.
For each node, compare the values of the current nodes from the left and right subtrees. Recursively check whether the left subtree of the left node mirrors the right subtree of the right node and vice versa. Continue these recursive comparisons until all corresponding nodes have been evaluated. If every comparison holds true, the tree is symmetric, and the function should return true. If any comparison fails, the function will return false, indicating that the tree is not symmetric.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self, root):
        if not root:
            return True # An empty tree is symmetric
        return self.symmetry(root.left, root.right)

    def symmetry(self, left, right):
        if not left and not right:
            return True # Both nodes are null, so symmetric

        if not left or not right:
            return False # One of the nodes is null, so not symmetric

        if left.data != right.data:
            return False # The values of the nodes do not match, so not symmetric

        # Recursively check the children of the nodes
        return self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Create a sample tree: 1, 2, 2, 3, 4, 4, 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # Test the symmetric tree
    print(solution.is_symmetric(root)) # Output: True

Complexity Analysis
Time complexity: O(N) This is because there are N number of nodes in the binary tree each node is traversed once to check for symmetry.

Space complexity : O(h) This is because the maximum depth of the recursion stack is equal to the height of the tree.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def is_symmetric(self, root):
        if not root:
            return True # An empty tree is symmetric
        return self.symmetry(root.left, root.right)

    def symmetry(self, left, right):
        if not left and not right:
            return True # Both nodes are null, so symmetric

        if not left or not right:
            return False # One of the nodes is null, so not symmetric

        if left.data != right.data:
            return False # The values of the nodes do not match, so not symmetric

        # Recursively check the children of the nodes
        return self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)

  