'''
Given root of binary tree, return the Inorder traversal of the binary tree.



Morris Inorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure.


Examples:
Input : root = [1, 4, null, 4, 2]

Output : [4, 4, 2, 1]

Explanation :



Input : root = [1, null, 2, 3]

Output : [1, 3, 2]


Constraints:
1 <= Number of Nodes <= 100
-100 <= Node.val <= 100

Intuition:
Morris Traversal provides an efficient method for performing an in-order traversal of a binary tree without relying on recursion or an explicit stack. The core concept involves creating temporary links, referred to as "threads," between nodes to track the current position during the traversal. By establishing temporary links to each node's in-order predecessor, this approach navigates through the tree without requiring additional space. This method ensures that each node is visited in the correct sequence while maintaining the tree's original structure upon completion of the traversal.

The traversal encompasses three primary scenarios: nodes without a left child, nodes with a left child where the in-order predecessor does not have a right child, and nodes with a left child where the right child of the in-order predecessor points back to the current node. Addressing these scenarios allows for an efficient and accurate in-order traversal while preserving the tree's structure.

Approach:
Begin by initializing the current node to the root of the binary tree.
While the current node is not null:
If the current node lacks a left child, print its value and move to the right child by setting the current node to its right child.
If the current node has a left child:
Identify the in-order predecessor of the current node, which is the rightmost node in the left subtree.
If the right child of the in-order predecessor is null, create a thread by setting its right child to the current node. Then, move to the left child by updating the current node to its left child.
If the right child of the in-order predecessor is not null, this indicates a previously established thread. Revert this change by setting the right child of the in-order predecessor back to null. Print the current node's value and then move to the right child by setting the current node to its right child.
Repeat the above steps until the traversal reaches the end of the tree.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# This method performs an inorder traversal of a binary tree
# using the Morris Traversal algorithm, which does not use
# additional space for a stack or recursion.

class Solution:
    def getInorder(self, root):
        # List to store inorder traversal
        inorder = []  
        # Pointer to current node
        cur = root  

        while cur is not None:
            if cur.left is None:
                # Add current node's value and move to right child
                inorder.append(cur.data)  
                cur = cur.right  
            else:
                # Find predecessor
                prev = cur.left  
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if prev.right is None:
                    # Establish temporary link
                    prev.right = cur 
                    # Move to left child 
                    cur = cur.left  
                else:
                    # Remove temporary link
                    # Add current node's value 
                    # Move to right child
                    prev.right = None  
                    inorder.append(cur.data)  
                    cur = cur.right  
                    
        # Return inorder traversal
        return inorder  

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    sol = Solution()
    inorder = sol.getInorder(root)

    print("Binary Tree Morris Inorder Traversal:", end=" ")
    for val in inorder:
        print(val, end=" ")
    print()

Complexity Analysis:
Time Complexity: O(2N), where N is the number of nodes in the Binary Tree. Each node is visited at most twice.
Space Complexity: O(1). Morris Traversal is an in-place algorithm, using only a constant amount of extra space.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def getInorder(self, root):
        inorder = []  
        cur = root  

        while cur is not None:
            if cur.left is None:

                inorder.append(cur.data)  
                cur = cur.right  
            else:
                prev = cur.left  
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = cur 
                    cur = cur.left  
                else:
                    prev.right = None  
                    inorder.append(cur.data)  
                    cur = cur.right  
        return inorder  
