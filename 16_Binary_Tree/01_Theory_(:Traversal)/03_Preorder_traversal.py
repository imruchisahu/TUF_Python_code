'''
Given root of binary tree, return the preorder traversal of the binary tree.


Examples:
Input : root = [1, 4, null, 4 2]

Output : [1, 4, 4, 2]

Explanation :



Input : root = [1]

Output : [1]

Explanation : Only root node is present.

Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[5, 1, 8, 6, 2, 4, 5]
Constraints:
1 <= Number of Nodes <= 100
-100 <= Node.val <= 100

#Recursive Approach
Intuition
Preorder traversal is one of the depth-first traversal methods used to explore nodes in a binary tree. The algorithm first visits the root node, then in the preorder traversal, we visit (i.e., add to the array) the current node by accessing its value, then we recursively traverse the left subtree in the same manner. We repeat these steps for the left subtree, then when we return to the current node, we recursively travel to the right subtree in a preorder manner as well. The sequence of steps in preorder traversal follows: Root, Left, Right.

Approach
Base Case: If the current node is null, it means we have reached the end of a subtree and there are no further nodes to explore. Hence the recursive function stops and we return from that particular recursive call.
Recursive Function:
Process Current Node: The recursive function begins by processing i.e., adding to the array or printing the current node.
Traverse Left Subtree: Recursively traverse the left subtree by invoking the preorder function on the left child of the current node. This step continues the exploration of nodes in a depth-first manner.
Traverse Right Subtree: After traversing the entire left subtree, we traverse the right subtree recursively. We once again invoke the preorder function, but this time on the right child of the current node.
Dry Run
Algorithm:

Step 1: Check for the base case that if the current node is null, exit the void function.
Step 2: Push the value of the current node into the preorder traversal array.
Step 3: Invoke the preorder function on the left child then right child to traverse the left and right subtrees in the preorder manner respectively.


This recursive approach implicitly uses the call stack to handle backtracking while exploring the tree nodes.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Helper function to perform preorder traversal
    def func(self, node, ans):
        # If the current node is None, return (base case for recursion)
        if node is None:
            return
        
        # Append the current node's value to the list
        ans.append(node.val)
        # Recursively traverse the left subtree
        self.func(node.left, ans)
        # Recursively traverse the right subtree
        self.func(node.right, ans)
    
    # Function to initiate preorder traversal and return the resulting list
    def preorder(self, root):
        # Create an empty list to store preorder traversal values
        ans = []
        # Call the helper function with the root node and the list
        self.func(root, ans)
        # Return the resulting list containing preorder traversal values
        return ans

# Main function to test the preorder traversal
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()
    # Getting preorder traversal
    result = solution.preorder(root)

    # Displaying the preorder traversal result
    print("Preorder Traversal:", end=" ")
    # Output each value in the preorder traversal result
    for val in result:
        print(val, end=" ")
    print()

Complexity Analysis :
Time Complexity: O(N) where N is the number of nodes in the binary tree, as each node of the binary tree is visited exactly once.

Space Complexity: O(N) where N is the number of nodes in the binary tree, as an additional space for the array is allocated to store the values of all ‘N’ nodes of the binary tree.

#Iterative Approach
Intuition
As a prerequisite to this approach, please understand Preorder Traversal in detail. The preorder traversal of a Binary Tree follows the order: Root, Left then Right. An iterative approach maintains a stack structure to simulate the recursive nature of the traversal without using actual recursion. The stack follows a last-in-first-out methodology and stores the nodes yet to be processed mimicking the depth-first search characteristic of preorder traversal.

Approach
Initially, the root node is pushed into the stack. While the stack is not empty, we continuously pop nodes from the stack and for each popped node, we add its value to the resultant traversal vector, push its right child onto the stack followed by its left child.
This sequence ensures that the left child, which should be processed first in the preorder traversal, is visited before the right child due to the Last In, First Out behaviour of the stack. This process continues until all nodes are processed.
Dry Run
Algorithm:

Step 1: Initialise an empty vector ‘preorder’ to store the preorder traversal result. Create a stack to store the nodes during traversal and push the root node onto the stack. Check if the root is null, return an empty traversal result if true.
Step 2: Push the root of the binary tree into the stack.

Step 3: While the stack is not empty:
Get the current node from the top of the stack.
Remove the node from the stack.
Add the node’s value to the preorder traversal result.
First, push the right child onto the stack if it exists.
Secondly, push the left child onto the stack if it exists.
Step 4: Return the ‘preorder’ traversal result.

from typing import List

# Define the TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to perform preorder traversal
    # of a binary tree iteratively
    def preorder(self, root: TreeNode) -> List[int]:
        # Initialize list to store
        # the preorder traversal result
        preorder = []
        
        # If the root is None, return
        # an empty traversal result
        if root is None:
            return preorder
        
        # Create a stack to store
        # nodes during traversal
        st = []
        # Push the root node
        # onto the stack
        st.append(root)
        
        # Perform iterative preorder traversal
        while st:
            # Get the current node
            # from the top of the stack
            root = st.pop()
            
            # Add the node's value to
            # the preorder traversal result
            preorder.append(root.val)
            
            # Push the right child
            # onto the stack if exists
            if root.right:
                st.append(root.right)
            
            # Push the left child onto
            # the stack if exists
            if root.left:
                st.append(root.left)
        
        # Return the preorder
        # traversal result
        return preorder

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the preorder traversal
result = sol.preorder(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()

Complexity Analysis :
Time Complexity: O(N) where N is the number of nodes in the binary tree. Every node of the binary tree is visited exactly once, and for each node, the operations performed (pushing and popping from the stack, accessing node values, etc.) are constant time operations.

Space Complexity: O(N) where N is the number of nodes in the binary tree. This is because the stack can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes. In the average case or for a balanced tree, the maximum number of nodes that could be in the stack at any given time would be roughly the height of the tree, hence O(log2N).


'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def func(self, node, ans):
        if node is None:
            return
        ans.append(node.val)
        self.func(node.left, ans)
        self.func(node.right, ans)
    
    def preorder(self, root):
        ans=[]
        self.func(root, ans)
        return ans
    