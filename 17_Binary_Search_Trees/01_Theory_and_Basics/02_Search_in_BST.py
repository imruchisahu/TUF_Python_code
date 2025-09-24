'''
Given the root of a binary search tree (BST) and an integer val.



Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


Examples:
Input : root = [4, 2, 7, 1, 3] , val = 2

Output : [2, 1, 3]

Explanation :



Input : root = [4, 2, 7, 1, 3] , val = 5

Output : []

Explanation :



Input : root = [10, 2, 12, 1, 4, null, null, null, null, 3] , val = 2

Output:
[2, 1, 4, null, null, 3]
Constraints:
1 <= Number of Nodes <= 5000
1 <= Node.val <= 107
1 <= val <= 107
All nodes values in BST are unique.

Intuition
In a Binary Search Tree (BST), the key property is that for any given node N, all nodes in its left subtree contain values smaller than N, while all nodes in its right subtree hold values greater than N. This structure facilitates an efficient search for a value X, which can be understood through three distinct scenarios:

1. If the value at node N matches X, then N is the target node.

2. If the value at node N is less than X, the search must proceed to the right subtree, as X cannot exist in the left subtree.

3. If the value at node N is greater than X, the search must continue in the left subtree, since X cannot be found in the right subtree.

Approach
Initiate a traversal of the tree using a while loop, conditioned on the root being non-NULL and the root's data not matching X.
If the root's data is less than X, shift the focus to the right child of the root.
If the root's data exceeds X, redirect the search to the left child of the root.
Upon exiting the loop, if the root is NULL, it indicates that X is not present in the tree, and the function should return NULL. Otherwise, return the node containing the value X.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
    def searchBST(self, root, val):
        # Traverse the tree until we find the node 
        # with the given value or reach the end
        while root is not None and root.data != val:
            # Move to the left or right child 
           # depending on the value comparison
            root = root.left if root.data > val else root.right
        # Return the found node or None if not found
        return root  

# Example usage
def main():
    # Creating a simple BST for demonstration
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    sol = Solution()
    result = sol.searchBST(root, 2)
    if result:
        print(f"Node found with value: {result.data}")
    else:
        print("Node not found")

if __name__ == "__main__":
    main()

Complexity Analysis
Time Complexity: O(log2(N)) : The time complexity is O(log2(N)) in a balanced BST since the search space is halved at each step. However, in the worst case (skewed tree), it can be O(N).

Space Complexity: O(1): The space complexity is O(1) as the search is performed iteratively without using additional space.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val):
        while root is not None and root.data != val:
            root = root.left if root.data > val else root.right
        return root
    