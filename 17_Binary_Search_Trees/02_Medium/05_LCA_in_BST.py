'''
Given the root node of a binary search tree (BST) and two node values p,q.



Return the lowest common ancestors(LCA) of the two nodes in BST.


Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , p = 2, q = 4

Output : [3]

Explanation :

Below is image of the BST



Input : root = [5, 3, 6, 2, 4, null, 7] , p = 2, q = 7

Output : [5]

Explanation :

Below is image of the BST



Input : root = [2, 1, 4, null, null, 3, 6] , p = 1, q = 6

Output:
1
2
6
3

Submit
Constraints:
1 <= Number of Nodes <= 104
1 <= Node.val <= 105
All values in BST are unique.
The values p and q are always present in the given BST.

#BRute
Intuition
The Lowest Common Ancestor (LCA) of two elements in a binary tree is the farthest shared ancestor from the root that is common to both elements. Essentially, the LCA of two nodes is the deepest node that serves as an ancestor to both nodes. To determine the LCA, one can trace the paths from the root to each of the two nodes. By comparing these paths, the last common node encountered represents the LCA, as it is the deepest shared ancestor.

To achieve this, the paths from the root to the respective nodes need to be identified. Once these paths are known, comparing them will reveal the deepest shared node, which is the LCA.

Approach
Develop a function that utilizes Depth-First Search (DFS) traversal to trace the path from the root of the binary tree to a specified node.
Utilize this function to obtain arrays that represent the paths from the root node to each of the target nodes.
Compare the two arrays by iterating through them to locate the last shared element in their respective paths from the root.
The last shared element identified in the paths is the Lowest Common Ancestor (LCA) of the given nodes. Return this element as the result.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def getPath(self, root, path, x):
        # Base case: If the current node is null, return False
        if not root:
            return False

        # Add the current node's value to the path
        path.append(root.data)

        # If the current node's value is equal to the target value 'x', return True
        if root.data == x:
            return True

        # Recursively search for the target value 'x' in the left and right subtrees
        if (self.getPath(root.left, path, x) or self.getPath(root.right, path, x)):
            return True

        # If the target value 'x' is not found in the current path, backtrack
        path.pop()
        return False

    def lca(self, root, p, q):
        path1, path2 = [], []

        # Find paths from the root to the given nodes
        if not self.getPath(root, path1, p) or not self.getPath(root, path2, q):
            return None

        # Find the last common element in the paths
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
            i += 1

        # The last common element is the LCA
        return TreeNode(path1[i - 1])

# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    # Find the LCA of nodes with values 5 and 1
    ans = sol.lca(root, 5, 1)
    if ans:
        print("LCA(5, 1) =", ans.data)
    else:
        print("LCA(5, 1) is not present in the tree")

    # Find the LCA of nodes with values 5 and 4
    ans = sol.lca(root, 5, 4)
    if ans:
        print("LCA(5, 4) =", ans.data)
    else:
        print("LCA(5, 4) is not present in the tree")

Complexity Analysis
Time Complexity O(N + log(2N)), where N is the number of nodes. Finding the root-to-node paths using DFS is O(N), and iterating through arrays is O(min(P1, P2)).

Space Complexity O(log2 N) due to storing root-to-node paths and the recursion stack during DFS. The height of the tree (log2(N)) determines the space required for arrays and the maximum depth of the recursion stack.


#Optimal
Intuition:
In a Binary Search Tree (BST), for any given node:

All values in the left subtree are smaller than the node's value.
All values in the right subtree are greater than the node's value.

The LCA of two nodes p and q in the lowest node in the tree that has both p and q as descendants (where a node is also considered its own descendant). There can be three possibilities which are as follows:
If p and q are both on the left of a node, the LCA must be in the left subtree.
If p and q are both on the right of a node, the LCA must be in the right subtree.
If one node is on the left and the other is on the right (or one matches the current node), then the current node is the LCA.
Approach:
Base Case: If root is null, return null (tree is empty).
Store the current node's value for easy comparison.
Check the position of p and q relative to root:
If both p and q are smaller than root->data, this means LCA is in the left subtree → recursively call lca(root->left, p, q).
If both p and q are greater than root->data, this means LCA is in the right subtree → recursively call lca(root->right, p, q).
If p and q are on different sides (one in left, one in right) or one of them is equal to root->data, then current node is the LCA.
Return the current node as LCA if it satisfies the condition in step 3.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    
    # Function to get the LCA in Binary Search Tree
    def lca(self, root, p, q):
        # base case
        if root is None:
            return None

        # Store the current node data
        curr = root.data 

        # If both nodes are smaller than root
        if curr < p and curr < q:
            # LCA lies in the right subtree
            return self.lca(root.right, p, q)
        
        # If both nodes are larger than root 
        if curr > p and curr > q:
            # LCA lies in the left subtree
            return self.lca(root.left, p, q)

        # Else root is the LCA 
        return root

if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)

    sol = Solution()

    # Find the LCA of nodes with values 5 and 8
    ans = sol.lca(root, 5, 8)
    if ans is not None:
        print(f"LCA(5, 8) = {ans.data}")
    else:
        print("LCA(5, 8) is not present in the tree")

Complexity Analysis:
Time Complexity: O(H), where H is the height of the tree.
As we are traversing till the height of the tree. In the best case, the time complexity is O(logN) for a balanced tree. In the worst case, the time complexity is O(N) for a skewed tree.

Space Complexity: O(H) because of the recursive stack space used for the function calls. In the worst case, the space complexity is O(N) for a skewed tree.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, root, p, q):
        if root is None:
            return None
        curr = root.data 

        # If both nodes are smaller than root
        if curr < p and curr < q:
            # LCA lies in the right subtree
            return self.lca(root.right, p, q)
        
        # If both nodes are larger than root 
        if curr > p and curr > q:
            # LCA lies in the left subtree
            return self.lca(root.left, p, q)
        return root
    