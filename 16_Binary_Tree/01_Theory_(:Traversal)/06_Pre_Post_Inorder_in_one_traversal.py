'''

Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.


Examples:
Input : root = [1, 3, 4, 5, 2, 7, 6 ]

Output : [ [5, 3, 2, 1, 7, 4, 6] , [1, 3, 5, 2, 4, 7, 6] , [5, 2, 3, 7, 6, 4, 1] ]

Explanation : The In-order traversal is [5, 3, 2, 1, 7, 4, 6].

The Pre-order traversal is [1, 3, 5, 2, 4, 7, 6].

The Post-order traversal is [5, 2, 3, 7, 6, 4, 1].





Input : root = [1, 2, 3, null, null, null, 6 ]

Output : [ [2, 1, 3, 6] , [1, 2, 3, 6] , [2, 6, 3, 1] ]

Explanation : The In-order traversal is [2, 1, 3, 6].

The Pre-order traversal is [1, 2, 3, 6].

The Post-order traversal is [2, 6, 3, 1].



Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[ [8, 6, 1, 5, 4, 2, 5], [5, 1, 8, 6, 2, 4, 5], [6, 8, 1, 4, 5, 2, 5] ]
Constraints:
1 <= Number of Nodes <= 105
0 <= Node.val <= 105

Intuition
A binary tree's preorder, inorder, and postorder traversals typically require three separate traversals. This can be obtained in a single pass using a stack for state management. The stack tracks the traversal state for each node. In the preorder state, the node's value is recorded, and its left child is pushed onto the stack. In the inorder state, the node's value is recorded, and its right child is pushed onto the stack. In the postorder state, the node's value is recorded, and the node is popped from the stack. This process pushes each value into separate arrays for preorder, inorder, and postorder traversals, enabling a single traversal to compute all three orders.

Approach
Create three vectors to store the results of Preorder, Inorder, and Postorder traversals. Use a stack to keep track of nodes and their traversal states. Start with the root node and a state of 1 (indicating Preorder).While the stack is not empty, pop the top element from the stack.
If the state is 1 (Preorder), add the node's data to the Preorder vector, change the state to 2 (Inorder) and push the node back onto the stack. If the node has a left child, push it onto the stack with a state of 1.
If the state is 2 (Inorder), add the node's data to the Inorder vector. change the state to 3 (Postorder) and push the node back onto the stack. If the node has a right child, push it onto the stack with a state of 1.
If the state is 3 (Postorder), Add the node's data to the Postorder vector. Return the vectors containing the Preorder, Inorder, and Postorder traversals.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def tree_traversal(self, root: TreeNode):
        # Lists to store the traversals
        pre, in_order, post = [], [], []

        # If the tree is empty, return empty traversals
        if root is None:
            return [pre, in_order, post]

        # Stack to maintain nodes and their traversal state
        stack = [(root, 1)]

        while stack:
            # Get the top element from the stack
            node, state = stack.pop()

            # Process the node based on its state
            if state == 1:
                # Preorder: Add node data
                pre.append(node.data)
                # Change state to 2 (inorder) for this node
                stack.append((node, 2))

                # Push left child onto the stack for processing
                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:
                # Inorder: Add node data
                in_order.append(node.data)
                # Change state to 3 (postorder) for this node
                stack.append((node, 3))

                # Push right child onto the stack for processing
                if node.right:
                    stack.append((node.right, 1))
            else:
                # Postorder: Add node data
                post.append(node.data)

        # Return the traversals as a list of lists
        return [in_order, pre, post]

# Main function to test the tree traversal
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    traversals = sol.tree_traversal(root)

    # Print Preorder traversal
    print("Preorder traversal:", *traversals[0])

    # Print Inorder traversal
    print("Inorder traversal:", *traversals[1])

    # Print Postorder traversal
    print("Postorder traversal:", *traversals[2])

Complexity Analysis
Time Complexity: O(3N), where N is the number of nodes, since each node is processed three times (preorder, inorder, postorder).

Space Complexity: O(4N), where N is the number of nodes, due to the stack and three traversal arrays.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        pre, in_order, post = [], [], []
        if root is None:
            return [pre, in_order, post]
        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()
            if state == 1:
                pre.append(node.data)
                stack.append((node, 2))

                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:
                in_order.append(node.data)
                stack.append((node, 3))
                if node.right:
                    stack.append((node.right, 1))
            else:
                post.append(node.data)
        return [in_order, pre, post]
    