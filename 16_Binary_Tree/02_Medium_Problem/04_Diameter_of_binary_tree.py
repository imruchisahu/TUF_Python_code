'''
Given the root of a binary tree, return the length of the diameter of the tree.



The diameter of a binary tree is the length of the longest path between any two nodes in the tree. It may or may not pass through the root.


Examples:
Input : root = [1, 2, 3, 4, 5]

Output : 3

Explanation : The path length between node 4 and 3 is of length 3.

There are other ways to reach the solution.





Input : root = [1, 2, 3, null, 4, null, 5]

Output : 4

Explanation : The path length between node 4 and 5 is of length 4.





Input : root = [5, 1, 2, 8, 3, null, 5, null, 4]

Output:
5
Constraints:
1 <= Number of Nodes <= 104
-100 <= Node.val <= 100


#Brute
Intuition
To determine the diameter of a binary tree, consider each node as a potential Curving Point in the path that forms the diameter. This Curving Point represents the node at the maximum height along the diameter path, where the path transitions between ascending and descending. The diameter at a particular Curving Point is calculated by adding the height of the left subtree to the height of the right subtree. This can be expressed as:

Diameter = Left Subtree Height + Right Subtree Height
Approach
Start by initializing a global variable diameter to keep track of the maximum diameter encountered during the traversal. This variable will be updated at each node as the tree is traversed.
Create a recursive function called calculateHeight that calculates the height of each node. For each node, compute the height of its left and right subtrees, and use these values to determine the current diameter by summing the heights. Continuously update the diameter variable with the maximum value encountered during this process.
Begin traversing the tree from the root node, utilizing the calculateHeight function to compute and update the maximum diameter at each node. Once the traversal is complete, return the value stored in diameter as the final result.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to compute the height of a subtree
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Function to find the diameter of a binary tree (Brute Force)
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        # Get the height of left and right subtrees
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        # Calculate diameter through the current node
        currentDiameter = leftHeight + rightHeight

        # Recursively calculate the diameter of left and right subtrees
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        # Return the maximum of the three values
        return max(currentDiameter, max(leftDiameter, rightDiameter))

# Creating a test tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print("Diameter of the binary tree is:", sol.diameterOfBinaryTree(root))

Complexity Analysis
Time Complexity: O(N2) In this approach, for each node, we calculate the height of its left and right subtrees, which takes O(N) time. Since this calculation is done for each of the N nodes in the tree, the total time complexity is O(N * N) = O(N2)

Space Complexity: O(H) The space complexity is determined by the maximum depth of the recursion stack, which corresponds to the height of the tree, H. Thus, the space complexity is O(H).

#Optimal
Intuition
The previous method for calculating the diameter of a binary tree can be refined by eliminating the repetitive calculations of subtree heights. In the earlier approach, the heights of the left and right subtrees are computed multiple times for each node, leading to inefficient and redundant computations. A more efficient strategy is to calculate these heights in a bottom-up fashion using a Postorder traversal. This technique enables the validation of balance conditions and the computation of the diameter simultaneously during the traversal.

Approach
Start by initializing a variable diameter to keep track of the maximum diameter of the tree. Then, create a helper function named height that accepts a node and a reference to the diameter variable.
For the base case, if the node is null, return 0. In the recursive function, compute the heights of the left and right subtrees for each node. Determine the current diameter by adding these subtree heights together and then adding 1 to account for the node itself. Update the global diameter variable with the maximum value encountered so far.
Once the entire tree has been traversed, return the maximum diameter recorded during the traversal as the final result.
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Function to find the diameter of a binary tree
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Initialize the variable to store the diameter of the tree
        diameter = [0]

        # Call the height function to traverse the tree and calculate diameter
        self.height(root, diameter)

        # Return the calculated diameter
        return diameter[0]

    # Function to calculate the height of the tree and update the diameter
    def height(self, node: TreeNode, diameter: List[int]) -> int:
        # Base case: If the node is None, return 0 indicating an empty tree height
        if not node:
            return 0

        # Recursively calculate the height of left and right subtrees
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)

        # Update the diameter with the maximum of current diameter 
        diameter[0] = max(diameter[0], lh + rh)

        # Return the height of the current node's subtree
        return 1 + max(lh, rh)

# Main method to test the function
if __name__ == "__main__":
    # Example usage: Create a tree and find its diameter
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    result = solution.diameterOfBinaryTree(root)
    print(f"Diameter of the binary tree is: {result}")
    
Complexity Analysis
Time Complexity: O(N) In the optimized approach, each node is visited once, and its height is calculated during the postorder traversal.

Space Complexity: O(H) The space complexity is determined by the maximum depth of the recursion stack, which corresponds to the height of the tree, H.

'''
from typing import List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]
    def height(self, node: TreeNode, diameter: List[int]) -> int:
        if not node:
            return 0
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)
        diameter[0] = max(diameter[0], lh + rh)
        return 1 + max(lh, rh)
    