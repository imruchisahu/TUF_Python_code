'''
Given two integer arrays preorder and inorder. Where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree.



Construct and return the binary tree using in-order and preorder arrays.


Examples:
Input : preorder = [3, 9, 20, 15, 7] , inorder = [9, 3, 15, 20, 7]

Output : [3, 9, 20, null, null, 15, 7]

Explanation : The output tree is shown below.



Input : preorder = [3, 4, 5, 6, 2, 9] , inorder = [5, 4, 6, 3, 2, 9]

Output : [3, 4, 2, 5, 6, null, 9]

Explanation : The output tree is shown below.



Input : preorder = [5, 1, 8, 6, 2, 4, 7] , inorder = [8, 6, 1, 5, 4, 2, 7]

Output:
[5, 1, 2, 8, null, 7, 4, null, 6]
[5, 1, 8, 2, null, 4, 7, null, 6]
[5, 1, 2, 8, null, 4, 7, null, 6]
[5, 1, 2, 8, null, 4, 7, 6, null]

Submit
Constraints:
1 <= Number of Nodes <= 104
-104 <= Node.val <= 104
All values in the given tree are unique.
Each value of inorder also appears in preorder.
Preorder is guaranteed to be the preorder traversal of the tree.
Inorder is guaranteed to be the inorder traversal of the tree.
Intuition
Understanding the significance of inorder and preorder traversals is crucial. Inorder traversal helps identify a node along with its left and right subtrees, while preorder traversal ensures the root node is encountered first. By leveraging these properties, it becomes possible to uniquely construct a binary tree. The core approach involves a recursive algorithm that creates one node at a time. The root node is located in the inorder traversal, splitting the array into left and right subtrees.


The inorder array continuously gets divided into left and right subtrees. To avoid unnecessary array duplication, variables (inStart, inEnd) and (preStart, preEnd) are used on the inorder and preorder arrays, respectively. These variables effectively define the boundaries of the current subtree within the original inorder and preorder traversals. Every time the root of a subtree is encountered via preorder traversal, its position is located in the inorder array to determine the left and right subtrees. To optimize the linear lookup, a hashmap is used to store the index of each element in the inorder traversal, transforming the search operation into a constant-time lookup.

Algorithm
Create an empty map to store the indices of elements in the inorder traversal. Iterate through each element in the inorder traversal and store its index in the map (inMap) using the element as the key and its index as the value.


Create a recursive helper function buildTree with the following parameters:
Preorder vector
Start index of preorder (preStart), initially set to 0
End index of preorder (preEnd), initially set to preorder.size() - 1
Inorder vector
Start index of inorder (inStart), initially set to 0
End index of inorder (inEnd), initially set to inorder.size() - 1
Map for efficient root index lookup in the inorder traversal
Base Case: Check if preStart is greater than preEnd or inStart is greater than inEnd. If true, return NULL, indicating an empty subtree/node.
The root node for the current subtree is the first element in the preorder traversal (preorder[preStart]). Find the index of this root node in the inorder traversal using the map (inMap[rootValue]). This is the rootIndex.
The left subtree ranges from inStart to rootIndex. Subtracting these indexes gives the leftSubtreeSize.
Make two recursive calls to buildTree to build the left and right subtrees:
For the left subtree:
Update preStart to preStart + 1 (moving to the next element in preorder)
Update preEnd to preStart + leftSubtreeSize (end of left subtree in preorder)
Update inEnd to rootIndex - 1 (end of left subtree in inorder)
For the right subtree:
Update preStart to preStart + leftSubtreeSize + 1 (moving to the next element after the left subtree)
Update preEnd to the original preEnd (end of right subtree in preorder)
Update inStart to rootIndex + 1 (start of right subtree in inorder)
Return the root node constructed for the current subtree. The function returns the root of the entire binary tree constructed from the preorder and inorder traversals.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Create a map to store indices
        # of elements in the inorder traversal
        inMap = {val: idx for idx, val in enumerate(inorder)}

        # Recursive helper function to build the tree
        def helper(preStart, preEnd, inStart, inEnd):
            # Base case: If the start indices
            # exceed the end indices, return null
            if preStart > preEnd or inStart > inEnd:
                return None

            # Create a new TreeNode with value
            # at the current preorder index
            root_val = preorder[preStart]
            root = TreeNode(root_val)

            # Find the index of the current root
            # value in the inorder traversal
            inRoot = inMap[root_val]

            # Calculate the number of
            # elements in the left subtree
            numsLeft = inRoot - inStart

            # Recursively build the left subtree
            root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)

            # Recursively build the right subtree
            root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)

            # Return the current root node
            return root

        # Call the helper function to build the tree
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    # Function to print the
    # inorder traversal of a tree
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=" ")
            self.printInorder(root.right)

    # Function to print the
    # given list
    def printList(self, lst):
        print(" ".join(map(str, lst)))

if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]

    sol = Solution()

    print("Inorder List: ", end="")
    sol.printList(inorder)

    print("Preorder List: ", end="")
    sol.printList(preorder)

    root = sol.buildTree(preorder, inorder)

    print("Inorder of Unique Binary Tree Created:")
    sol.printInorder(root)
    print()

Complexity Analysis:
Time Complexity : The time complexity is O(N), where N is the number of nodes in the Binary Tree. This is because each node of the Binary Tree is visited once.

Space Complexity: O(N), where N is the number of nodes in the Binary Tree. The inorder hashmap used to store the inorder array for fast lookup takes up space proportional to the input nodes. Additionally, an auxiliary stack space of approximately O(H) is used, where H is the height of the Binary Tree.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        inMap = {val: idx for idx, val in enumerate(inorder)}
        def helper(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None
            root_val = preorder[preStart]
            root = TreeNode(root_val)
            inRoot = inMap[root_val]
            numsLeft = inRoot - inStart
            root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
            root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)
            return root
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
