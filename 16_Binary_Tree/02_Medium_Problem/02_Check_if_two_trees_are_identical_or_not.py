'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.



Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Examples:
Input : p = [1, 2, 3] , q = [1, 2, 3]

Output : true

Explanation : Both trees images are shown below









Input : p = [1, 2, 1] , q = [1, 1, 2]

Output : false

Explanation : Both trees images are shown below









Input : p = [5, 1, 2, 8, null, null, 5, null, 4, null, null, 7 ], q = [5, 1, 2, 8, null, null, 4, null, 5, null, null, 7 ]

Output:
false
Constraints:
0 <= Number of Nodes <= 100
-104 <= Node.val <= 104

Intuition
To determine whether two binary trees are identical, one effective method is to traverse both trees simultaneously, comparing the values and structure of corresponding nodes at each step. The key idea is that two trees are identical if and only if every corresponding pair of nodes in the two trees have the same value and the same left and right subtrees. This requires ensuring that not only the values match, but that the structure of the trees (i.e., the presence or absence of left and right children) is also identical. Essentially, for the trees to be considered identical, the entire hierarchy from the root to the leaves must be the same.

Approach
Start at the root node of both trees (p and q). First, check if both nodes are null. If both are null, the current branches are identical up to this point, so return true. If only one of them is null or if their values differ, return false, as this means the trees are not identical.
Recursively compare the left subtree of p with the left subtree of q and the right subtree of p with the right subtree of q. At each step, ensure that both the structure (presence of children) and the node values match.
If all recursive checks for the left and right subtrees return true, then the trees are identical; otherwise, if any check fails, the trees are not identical. The final result will depend on the outcome of these recursive checks.

class TreeNode: 
# Definition of a binary tree node
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # If both nodes are null, the trees are the same
        if not p and not q:
            return True

        # If one of the nodes is null, the trees are not the same
        if not p or not q:
            return False

        # If the values of the nodes are different, the trees are not the same
        if p.data != q.data:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Creating two sample trees
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    # Checking if the trees are identical
    result = solution.isSameTree(tree1, tree2)
    print("Are the trees identical?", result)  # Output: True

Complexity Analysis
Time Complexity: O(N) Visit each node exactly once during the traversal, where N is the number of nodes in the tree.

Space Complexity: O(h) The space complexity is determined by the recursion stack, which can go as deep as the height of the tree h.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.data != q.data:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
