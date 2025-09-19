'''
Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.



The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).


Examples:
Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 1

Output : 3

Explanation :



Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 4

Output : 5

Explanation :



Input : root = [7, 1, 2, 8, 10, 4, 5, null, 6], p = 6, q = 10

Output:
1
Constraints:
2 <= Number of Nodes <= 105
-106 <= node.val <= 106
All values in tree are unique.

Intuition
Finding the Lowest Common Ancestor (LCA) of two nodes in a binary tree requires determining the closest node that is an ancestor to both given nodes. The LCA can be identified as one of the following: it may be located within the left subtree, the right subtree, or it might be the root node itself if the two nodes are distributed across both subtrees. The fundamental idea is that the LCA is the deepest node that serves as an ancestor to both target nodes, representing the point where their paths to the root diverge.

Approach
Start by checking if the current root node is null or matches one of the target nodes (x or y). If the root is null or matches either target node, then return the root, as it could potentially be the LCA or simply indicate the end of the search path.
Perform a recursive search in the left subtree to find the nodes x and y. This involves calling the LCA function on the left child of the current root.
Similarly, perform a recursive search in the right subtree. This entails calling the LCA function on the right child of the current root.
After completing the recursive searches, analyze the results of both subtree searches. If both recursive calls return non-null values, it implies that one target node was found in each subtree. Consequently, the current root node must be the LCA, as it is the common ancestor of both nodes.
If only one of the subtree searches returns a non-null result, it indicates that both target nodes are located within the same subtree. In this case, return the non-null result, which represents the LCA found in that subtree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if root is None or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Result
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root

if __name__ == "__main__":
    # Construct a simple binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    solution = Solution()
    p = root.left  # Node with value 5
    q = root.right  # Node with value 1

    lca = solution.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.data)

    
Complexity Analysis
Time complexity: O(N) where n is the number of nodes.

Space complexity: O(N), auxiliary space.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else: 
            return root