'''
Given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.



Recover the tree without changing its structure.


Examples:
Input : root = [1, 3, null, null, 2]

Output : [3, 1, null, null, 2]

Explanation :

3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.







Input : root = [3, 1, 4, null, null, 2]

Output : [2, 1, 4, null, null, 3]

Explanation :

2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.



Input : root = [2, 1, 3, null, null, 4]

Output:
[2, 1, 3, null, null, 4]
[2, 1, null, 4, null, 3]
[2, 1, 4, null, null, 3]
[2, 1, 4, 3]

Submit
Constraints:
1 <= Number of Nodes <= 104
-231 <= Node.val <= 231 - 1

#Brute
Intuition
To fix a BST with two swapped nodes, the key is to recognize that an inorder traversal of a BST yields a sorted sequence. First, collect the node values using an inorder traversal, which will provide an array of values. Sorting this array reveals what the inorder sequence should be if the BST were correct. By comparing the BST's actual inorder traversal with this sorted array, it's possible to identify where the nodes are out of order. The task then is to correct these discrepancies by updating the BST nodes with the appropriate values from the sorted array, thereby restoring the BST's correct structure without altering its overall form.

Approach
Perform an inorder traversal of the BST to gather the node values into an array. Sort this array to get the correct inorder sequence of the BST.
Traverse the BST again using inorder traversal, comparing each node's value with the corresponding value in the sorted array.
When a mismatch is found between a node's value and the value from the sorted array, update the BST node with the correct value from the sorted array.
Return the modified BST.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.inorderValues = []
        self.index = 0

    def recoverTree(self, root):
        # Step 1: Collect node values via inorder traversal
        self.collectInorder(root)

        # Step 2: Sort the values to get correct inorder sequence
        self.inorderValues.sort()

        # Step 3: Traverse again and assign sorted values back
        self.restoreInorder(root)

    def collectInorder(self, root):
        if not root:
            return
        self.collectInorder(root.left)
        self.inorderValues.append(root.data)
        self.collectInorder(root.right)

    def restoreInorder(self, root):
        if not root:
            return
        self.restoreInorder(root.left)
        root.data = self.inorderValues[self.index]
        self.index += 1
        self.restoreInorder(root.right)

# Helper to build tree using level order array
def insertLevelOrder(arr, i):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = insertLevelOrder(arr, 2 * i + 1)
    root.right = insertLevelOrder(arr, 2 * i + 2)
    return root

# Helper to print inorder
def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.data, end=" ")
        inorderPrint(root.right)

# Driver code
nodes = [1, 3, None, None, 2]
root = insertLevelOrder(nodes, 0)

sol = Solution()
sol.recoverTree(root)
inorderPrint(root)  # Output should be sorted inorder


Complexity Analysis
Time Complexity: O(N*logN), where N is the number of nodes in the tree.
The inorder traversal takes O(N) time. Sorting the inorder traversal takes O(N*logN) time. Traversing the tree again to correct it will take another O(N) time. Hence, the total complexity becomes O(2N + N*logN) or simply O(N*logN).

Space Complexity: O(N)
Storing the inorder traversal takes O(N) space and the recursive stack space required to compute the inorder traversal recursively is O(H), where H is the height of the tree. In worst cases (in case of skew tree), H is equivalent to N. Hence, the overall space complexity becomes O(N) + O(H) or simply O(N).


#Optimal
Intuition
A Binary Search Tree (BST) has an inorder traversal that results in a sorted sequence. When two elements are swapped, this sorted order is disrupted. To identify these misplaced nodes, traverse the tree and keep track of the previous and next nodes for each visited node. By doing this, it's possible to detect where the order is violated. Once these violations are identified, the algorithm can pinpoint the two nodes that are out of place, whether they are adjacent or not. This allows for the correct nodes to be swapped, restoring the BST's proper structure.

Approach
Use four pointers: first, prev, middle, and last. first and middle help identify the misplaced nodes, prev tracks the previous node during the inorder traversal, and last marks the second node of the misplaced pair if the nodes are not adjacent.
Perform an inorder traversal of the BST, comparing each node's value with the previous node's value (prev) to detect any violations where the current node's value is less than the previous node's value. When a violation is found:
The first violation identifies the first and middle nodes. The first node is the first element encountered that is not greater than its previous node, and the middle node is temporarily stored in case the swapped nodes are adjacent.
If a second violation occurs, it indicates that the swapped nodes are not adjacent, and the last node is identified.
If no second violation is found, implying that the swapped nodes are adjacent, the middle node identified earlier is retained.
Once the misplaced nodes are identified, perform the necessary swaps based on whether the nodes are adjacent or not:
If both first and last are identified, swap the values of the first and last nodes.
If only first and middle are identified, swap their values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize the pointers
        self.first = None
        self.first_next = None
        self.last = None
        self.previous_node = TreeNode(float('-inf'))  # Previous node initialized to negative infinity

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        
        # Traverse the left subtree
        self.inorderTraversal(root.left)

        # Identify misplaced nodes
        if self.previous_node and root.data < self.previous_node.data:
            if not self.first:
                self.first = self.previous_node  # First out-of-order node
                self.first_next = root  # Node next to the first out-of-order node
            else:
                self.last = root  # Second out-of-order node

        # Update previous node to current node
        self.previous_node = root

        # Traverse the right subtree
        self.inorderTraversal(root.right)

    def recoverTree(self, root: TreeNode):
        # Reset the pointers
        self.first = self.first_next = self.last = None
        self.previous_node = TreeNode(float('-inf'))
        
        # Perform the inorder traversal to find the two nodes
        self.inorderTraversal(root)

        # Correct the BST by swapping the misplaced nodes
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data  # Non-adjacent nodes
        elif self.first and self.first_next:
            self.first.data, self.first_next.data = self.first_next.data, self.first.data  # Adjacent nodes

# Helper function to insert nodes in the tree for testing purposes
def insertLevelOrder(arr, i):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = insertLevelOrder(arr, 2 * i + 1)
    root.right = insertLevelOrder(arr, 2 * i + 2)
    return root

# Helper function to print inorder traversal of the tree
def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print(root.data, end=' ')
        inorderPrint(root.right)

if __name__ == "__main__":
    # Example input tree: [1, 3, None, None, 2]
    nodes = [1, 3, None, None, 2]
    root = insertLevelOrder(nodes, 0)

    # Solution instance
    sol = Solution()
    sol.recoverTree(root)

    # Print corrected tree
    inorderPrint(root)

Complexity Analysis
Time Complexity : O(N), traverses the binary tree once.

Space Complexity : O(N), in the worst case, the function call stack can go up to the depth of the tree, which is N nodes in an unbalanced tree.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize the pointers
        self.first = None
        self.first_next = None
        self.last = None
        self.previous_node = TreeNode(float('-inf'))  # Previous node initialized to negative infinity

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        
        # Traverse the left subtree
        self.inorderTraversal(root.left)

        # Identify misplaced nodes
        if self.previous_node and root.data < self.previous_node.data:
            if not self.first:
                self.first = self.previous_node  # First out-of-order node
                self.first_next = root  # Node next to the first out-of-order node
            else:
                self.last = root  # Second out-of-order node

        # Update previous node to current node
        self.previous_node = root

        # Traverse the right subtree
        self.inorderTraversal(root.right)

    def recoverTree(self, root: TreeNode):
        # Reset the pointers
        self.first = self.first_next = self.last = None
        self.previous_node = TreeNode(float('-inf'))
        
        # Perform the inorder traversal to find the two nodes
        self.inorderTraversal(root)

        # Correct the BST by swapping the misplaced nodes
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data  # Non-adjacent nodes
        elif self.first and self.first_next:
            self.first.data, self.first_next.data = self.first_next.data, self.first.data  # Adjacent nodes

