'''
Given two integer arrays Postorder and Inorder. Where Postorder is the postorder traversal of a binary tree and Inorder is the inorder traversal of the same tree.



Construct and return the binary tree using the postorder and inorder arrays.


Examples:
Input : postorder = [9, 15, 7, 20, 3] , inorder = [9, 3, 15, 20, 7]

Output : [3, 9, 20, null, null, 15, 7]

Explanation : The output tree is shown below.



Input : postorder = [5, 6, 4, 9, 2, 3] , inorder = [5, 4, 6, 3, 2, 9]

Output : [3, 4, 2, 5, 6, null, 9]

Explanation : The output tree is shown below.



Input : postorder = [6, 8, 1, 4, 7, 2, 5], inorder = [8, 6, 1, 5, 4, 2, 7]

Output:
[5, 1, 2, 8, null, 7, 4, null, 6]
[5, 1, 2, 8, null, 4, 7, null, 6]
[5, 2, 1, 8, null, 4, 7, null, 6]
[5, 2, 1, 8, null, 7, 4, null, 6]

Submit
Constraints:
1 <= Number of Nodes <= 3000
-104 <= Node.val <= 104
All values in the given tree are unique.
Each value of inorder also appears in postorder.
Postorder is guaranteed to be the postorder traversal of the tree.
Inorder is guaranteed to be the inorder traversal of the tree.

Intuition
The process of constructing a binary tree from inorder and postorder traversals involves understanding how these traversals reveal the tree's structure. The inorder traversal allows us to determine the left and right subtrees of each node, while the postorder traversal ensures that the root node is the last node visited. By utilizing these characteristics, the binary tree can be reconstructed uniquely. The fundamental approach employs a recursive algorithm that constructs the tree one node at a time. The root node is identified from the postorder traversal and located in the inorder traversal, which divides the array into left and right subtrees.


To optimize the process and avoid unnecessary duplication of arrays, variables (inStart, inEnd) and (postStart, postEnd) are used to define the boundaries of the current subtree within the inorder and postorder arrays, respectively. These variables delineate the sections of the arrays that pertain to the current subtree. By finding the root of a subtree within the inorder array, the left and right subtrees can be determined. Additionally, a hashmap is used to store the indices of elements in the inorder traversal, allowing for constant-time lookups and enhancing the efficiency of the reconstruction process.

Algorithm
Create an empty hashmap to record the indices of elements in the inorder traversal. Traverse the inorder array and populate the hashmap (inMap) such that each element is a key, and its corresponding index is the value.


Create a recursive helper function buildTree with the following parameters:
Postorder vector
Start index of postorder (postStart), initially set to 0
End index of postorder (postEnd), initially set to postorder.size() - 1
Inorder vector
Start index of inorder (inStart), initially set to 0
End index of inorder (inEnd), initially set to inorder.size() - 1
Map for efficient root index lookup in the inorder traversal
Base Case: Check if postStart is greater than postEnd or inStart is greater than inEnd. If true, return NULL, indicating an empty subtree/node.
The root node for the current subtree is the last element in the postorder traversal (postorder[postEnd]).
Find the index of this root node in the inorder traversal using the map (inMap[rootValue]). This is the rootIndex.
The left subtree ranges from inStart to rootIndex. Subtracting these indexes gives the leftSubtreeSize.
Make two recursive calls to buildTree to build the left and right subtrees:
For the left subtree:
Update postStart to postEnd - leftSubtreeSize (moving to the next element in postorder)
Update postEnd to postEnd - 1 (end of left subtree in postorder)
Update inEnd to rootIndex - 1 (end of left subtree in inorder)
For the right subtree:
Update postStart to postStart (moving to the next element in postorder)
Update postEnd to postEnd - leftSubtreeSize - 1 (end of right subtree in postorder)
Update inStart to rootIndex + 1 (start of right subtree in inorder)
Return the root node constructed for the current subtree. The function returns the root of the entire binary tree constructed from the inorder and postorder traversals.

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) != len(postorder):
            return None
        
        # Create a map to store the indices
        # of elements in the inorder traversal
        hm = {}
        for i, val in enumerate(inorder):
            hm[val] = i
        
        # Call the recursive function
        # to build the binary tree
        return self.buildTreePostIn(inorder, 0, len(inorder) - 1, postorder, 0,
                                    len(postorder) - 1, hm)
    
    # Recursive function to build a binary
    # tree from inorder and postorder traversals
    def buildTreePostIn(self, inorder: List[int], is_: int, ie: int,
                        postorder: List[int], ps: int, pe: int,
                        hm: dict) -> TreeNode:
        
        # Base case: If the subtree
        # is empty, return None
        if ps > pe or is_ > ie:
            return None
        
        # Create a new TreeNode
        # with the root value from postorder
        root = TreeNode(postorder[pe])
        
        # Find the index of the root
        # value in inorder traversal
        inRoot = hm[postorder[pe]]
        
        # Number of nodes in the left subtree
        numsLeft = inRoot - is_
        
        # Recursively build the
        # left and right subtrees
        root.left = self.buildTreePostIn(inorder, is_, inRoot - 1, postorder,
                                         ps, ps + numsLeft - 1, hm)
        
        root.right = self.buildTreePostIn(inorder, inRoot + 1, ie, postorder,
                                          ps + numsLeft, pe - 1, hm)
        
        # Return the root of
        # the constructed subtree
        return root

def printInorder(root: TreeNode):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

def printList(lst: List[int]):
    for num in lst:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    # Example input lists
    inorder = [40, 20, 50, 10, 60, 30]
    postorder = [40, 50, 20, 60, 30, 10]

    # Display the input lists
    print("Inorder List:", end=" ")
    printList(inorder)

    print("Postorder List:", end=" ")
    printList(postorder)

    sol = Solution()

    # Build the binary tree and
    # print its inorder traversal
    root = sol.buildTree(inorder, postorder)

    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()

Complexity Analysis :
Time Complexity : The time complexity of the algorithm is O(N) where N is the number of nodes in the Binary Tree. This is because each node is processed and visited exactly once.

Space Complexity : The space complexity of the algorithm is O(N + log N) where N is the number of nodes in the Binary Tree.

'''
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) != len(postorder):
            return None
        hm = {}
        for i, val in enumerate(inorder):
            hm[val] = i
        return self.buildTreePostIn(inorder, 0, len(inorder) - 1, postorder, 0,
                                    len(postorder) - 1, hm)
    def buildTreePostIn(self, inorder: List[int], is_: int, ie: int,
                        postorder: List[int], ps: int, pe: int,
                        hm: dict) -> TreeNode:
        if ps > pe or is_ > ie:
            return None
        root = TreeNode(postorder[pe])
        inRoot = hm[postorder[pe]]
        numsLeft = inRoot - is_
        root.left = self.buildTreePostIn(inorder, is_, inRoot - 1, postorder,
                                         ps, ps + numsLeft - 1, hm)
        
        root.right = self.buildTreePostIn(inorder, inRoot + 1, ie, postorder,
                                          ps + numsLeft, pe - 1, hm)
        return root