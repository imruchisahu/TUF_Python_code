'''
Given a root of Binary Tree, where the nodes have integer values. Return the size of the largest subtree of the binary tree which is also a BST.



A binary search tree (BST) is a binary tree data structure which has the following properties.



The left subtree of a node contains only nodes with data less than the node’s data.


The right subtree of a node contains only nodes with data greater than the node’s data.


Both the left and right subtrees must also be binary search trees.

Examples:
Input : root = [2, 1, 3]

Output : 3

Explanation :

The given complete binary tree is a BST consisting of 3 nodes.



Input : root = [10, null, 20, null, 30, null, 40, null, 50]

Output : 5

Explanation :

If we consider the node 10 as root node then it forms the largest BST.



Input : root = [3, 1, 4, null, null, 2]

Output:
1
2
3
4

Submit
Constraints:
1 <= Number of Nodes <= 104
1 <= Node.val <= 105

Hint 1

#Brute
Intuition
To find the largest Binary Search Tree (BST) subtree within a binary tree, a brute force approach involves examining each node and verifying if the subtree rooted at that node adheres to BST rules. This means ensuring that all values in the left subtree are less than the node's value and all values in the right subtree are greater. By recursively validating each node's subtree, the size of any valid BST subtree can be determined and compared to find the largest one. The key is to traverse the tree and check each subtree for BST properties, keeping track of the largest valid subtree found.

Approach
Define a function isValidBST that checks if a given subtree rooted at a node is a valid BST by performing a recursive traversal with range constraints.
Initialize a variable maxSize to 0 to keep track of the maximum size of any valid BST subtree found. Recursively traverse each node of the given binary tree.
At each node, use the isValidBST function to check if the subtree rooted at that node is a valid BST. If it is, calculate the size of this subtree and update maxSize if this size is larger than the current maxSize.
After traversing all nodes, return maxSize, which will hold the size of the largest BST subtree found.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def largestBST(self, root):
        # Helper function to validate BST and get the size of the subtree.
        def isBSTAndSize(node, minValue, maxValue):
            # Base case: if node is None, it is a valid BST of size 0.
            if not node:
                return (0, True, float('inf'), float('-inf'))

            # Recursively check the left and right subtrees.
            leftSize, isLeftBST, leftMin, leftMax = isBSTAndSize(node.left, minValue, node.data)
            rightSize, isRightBST, rightMin, rightMax = isBSTAndSize(node.right, node.data, maxValue)

            # Check if the current node is a valid BST node.
            if isLeftBST and isRightBST and leftMax < node.data < rightMin:
                # Current subtree is a valid BST, calculate its size.
                size = leftSize + rightSize + 1
                # Return size, isBST, min value, and max value for the current subtree.
                return (size, True, min(node.data, leftMin), max(node.data, rightMax))
            else:
                # Current subtree is not a valid BST, return the size of the largest valid BST found so far.
                return (max(leftSize, rightSize), False, float('-inf'), float('inf'))

        # Initialize the function to call
        return isBSTAndSize(root, float('-inf'), float('inf'))[0]

# Main method to demonstrate usage
if __name__ == "__main__":
    # Example binary tree
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.largestBST(root))  # Output: 3

    # Additional test case
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)

    print(sol.largestBST(root))  # Output: 3 (The subtree 5-1-8 is the largest BST)

    
Complexity Analysis
Time Complexity : O(N) , Each node is visited once, and constant-time operations are performed for each node, leading to a time complexity of O(n).

Space Complexity O(H) The space complexity is determined by the recursion stack, which grows with the height of the tree, resulting in O(h) space.


#Optimal
Intuition
A more efficient method to find the largest Binary Search Tree (BST) subtree within a binary tree involves traversing the tree and simultaneously verifying if each subtree is a BST. By adopting a bottom-up recursive approach, it’s possible to traverse the tree efficiently. For each node, the minimum value, maximum value, size of the BST, and whether it is a BST can be determined based on its children’s information. This approach allows for updating and maintaining the size of the largest BST subtree found during the traversal.

Approach
Define a NodeValue class to store the following information about each subtree:
minNode: Minimum value of the subtree.
maxNode: Maximum value of the subtree.
maxSize: Maximum size of the BST encountered so far.
Implement a helper function largestBSTSubtreeHelper that takes the root as input and recursively gathers information (minNode, maxNode, and maxSize) for each subtree.
The NodeValue information for the current node is updated based on the left and right subtree properties. Specifically, the left subtree’s maximum node should be less than the current node and the right subtree’s minimum node should be greater than the current node.
If the current subtree satisfies the BST property, update the size of the node (maxSize) as the sum of maxSize from the left subtree, maxSize from the right subtree, and 1.
If the current subtree is not a BST, carry forward the current maxSize but set minNode to int min and maxNode to int max.
Return the maxSize of the largest BST subtree found.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Helper class to store information about a subtree.
    class NodeValue:
        def __init__(self, minNode, maxNode, maxSize):
            self.minNode = minNode
            self.maxNode = maxNode
            self.maxSize = maxSize

    # Helper function to recursively find the largest BST subtree.
    def largestBSTSubtreeHelper(self, node):
        # Base case: if the node is null, return a default NodeValue.
        if not node:
            return self.NodeValue(float('inf'), float('-inf'), 0)

        # Recursively get values from the left and right subtrees.
        left = self.largestBSTSubtreeHelper(node.left)
        right = self.largestBSTSubtreeHelper(node.right)

        # Check if the current node is a valid BST node.
        if left.maxNode < node.data < right.minNode:
            # Current subtree is a valid BST.
            return self.NodeValue(
                min(node.data, left.minNode),
                max(node.data, right.maxNode),
                left.maxSize + right.maxSize + 1
            )

        # Current subtree is not a valid BST.
        return self.NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

    def largestBST(self, root):
        # Initialize the recursive process and return the size of the largest BST subtree.
        return self.largestBSTSubtreeHelper(root).maxSize

# Main method to demonstrate usage
if __name__ == "__main__":
    # Example binary tree
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.largestBST(root))  # Output: 3

    # Additional test case
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(8)
    root2.right.right = TreeNode(7)

    print(sol.largestBST(root2))  # Output: 3 (The subtree 5-1-8 is the largest BST)

Complexity Analysis
Time Complexity :O(N), where N is the number of nodes in the Binary tree as we traverse through all the nodes in the tree. The information update for each nodes takes constant time hence the overall time complexity is O(N) as the tree is traversed once.

Space Complexity : O(N) , where N is number of nodes in the Binary Tree as for each node we store additional information using a struct class whose new object is initialised.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    class NodeValue:
        def __init__(self, minNode, maxNode, maxSize):
            self.minNode = minNode
            self.maxNode = maxNode
            self.maxSize = maxSize

    def largestBSTSubtreeHelper(self, node):
        if not node:
            return self.NodeValue(float('inf'), float('-inf'), 0)
        
        left = self.largestBSTSubtreeHelper(node.left)
        right = self.largestBSTSubtreeHelper(node.right)
        if left.maxNode < node.data < right.minNode:
            return self.NodeValue(
                min(node.data, left.minNode),
                max(node.data, right.maxNode),
                left.maxSize + right.maxSize + 1
            )
        return self.NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

    def largestBST(self, root):
        return self.largestBSTSubtreeHelper(root).maxSize

