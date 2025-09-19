'''
In a binary tree, a path is a list of nodes where there is an edge between every pair of neighbouring nodes. A node may only make a single appearance in the sequence.



The total of each node's values along a path is its path sum. Return the largest path sum of all non-empty paths given the root of a binary tree.



Note: The path does not have to go via the root.


Examples:
Input : root = [20, 9, -10, null, null, 15, 7]

Output : 34

Explanation : The path from node 15 to node 9 has maximum path sum.

The path is 15 -> -10 -> 20 -> 9.



Input : root = [-10, 9, 20, null, null, 15, 7]

Output : 42

Explanation : The path from node 15 to node 7 has maximum path sum.

The path is 15 -> 20 -> 7.



Input : root = [1, 2, 3, null, 4]



Output:
10
Constraints:
1 <= Number of Nodes <= 3*104
-103 <= Node.val <= 103


Intuition
To determine the maximum path sum in a binary tree, it is essential to consider all possible paths between any two nodes. Since paths can start and end at any node, a comprehensive exploration of every potential path is required, making the problem complex. The primary objective is to identify the path that yields the highest sum. To achieve this, the problem can be decomposed into smaller, more manageable components.

Visualize each node as a potential turning point in the path. For every node, calculate the maximum path sum that includes the node itself and extends through its children. Throughout the traversal, continuously track the highest path sum encountered.

Approach
Begin by defining a recursive function designed to calculate the maximum path sum for each subtree rooted at a given node. If the current node is null, return 0, as there is no valid path through a null node.
Proceed by calculating the maximum path sum for both the left and right subtrees. If the path sum for either subtree is negative, it should be disregarded, as including it would decrease the overall sum. This can be achieved by taking the maximum of 0 and the calculated path sum for each subtree.
For each node, compute the potential maximum path sum that passes through the node and its children. This sum includes the node itself and the maximum path sums from both subtrees. If this value exceeds the current global maximum sum, update the global maximum to reflect this new higher value.
Finally, return the maximum path sum for the current node, considering only one of its subtrees. This step ensures that when the function backtracks up the tree, only the highest path sum from either the left or right subtree is propagated upward, maintaining the integrity of the overall maximum path sum calculation.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMaxPathSum(self, root, maxi):
        # Base case: If the current node is null, return 0
        if not root:
            return 0

        # Calculate the maximum path sum
        # for the left and right subtrees
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))

        # Update the overall maximum
        # path sum including the current node
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)

        # Return the maximum sum considering
        # only one branch (either left or right)
        # along with the current node
        return max(leftMaxPath, rightMaxPath) + root.val

    def maxPathSum(self, root):
        # Initialize maxi to the
        # minimum possible integer value
        maxi = [float('-inf')]

        # Call the recursive function to
        # find the maximum path sum
        self.findMaxPathSum(root, maxi)

        # Return the final maximum path sum
        return maxi[0]

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

# Finding and printing the maximum path sum
maxPathSum = solution.maxPathSum(root)
print("Maximum Path Sum:", maxPathSum)

Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the recursive traversal.

Space Complexity: O(1) as no additional space or data structures are created that are proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMaxPathSum(self, root, maxi):
        if not root:
            return 0
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)
        return max(leftMaxPath, rightMaxPath) + root.val

    def maxPathSum(self, root):
        maxi = [float('-inf')]
        self.findMaxPathSum(root, maxi)
        return maxi[0]
    