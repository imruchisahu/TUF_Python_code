'''

Given a pair of tree traversal, return true if a unique binary tree can be constructed otherwise false. Each traversal is represented with integer: 1 -> Preorder , 2 -> Inorder , 3 -> Postorder.


Examples:
Input : 1 2

Output : true 

Explanation : Answer is True.

It is possible to construct a unique binary tree. This is because the preorder traversal provides the root of the tree, and the inorder traversal helps determine the left and right subtrees.

Input : 2 2

Output : false

Explanation : Two inorder traversals are insufficient to uniquely determine a binary tree.

Input : 1 3

Output:
false
Constraints:
1 <= a, b <= 3

Intuition
The concept of "uniqueness" implies that there must be only one binary tree that matches the provided traversal sequences. Without this requirement, multiple trees could fit the same traversals, leading to ambiguity.

Let’s examine the scenarios where two types of traversals—preorder, postorder, and inorder—are given:

Scenario 1: Given Preorder and Postorder Traversal
When provided with just preorder and postorder traversals, it is not possible to uniquely reconstruct a binary tree. This is because multiple trees can produce the same preorder and postorder sequences, leaving room for ambiguity.


Scenario 2: Given Preorder and Inorder Traversal
Preorder traversal starts with the root node and explores the left subtree before the right subtree. This traversal identifies the root and helps in constructing the tree structure. In contrast, inorder traversal processes nodes by visiting the left subtree first, followed by the root, and then the right subtree. This approach clearly separates the left and right subtrees, enabling a unique reconstruction of the binary tree.

Image 1
Image 2
Image 3

1/3


Scenario 3: Postorder and Inorder Traversal Given
Postorder traversal visits nodes in the left subtree, then the right subtree, and finally the root node. The last element represents the root, while preceding elements identify subtrees. Inorder traversal provides a clear division between left and right subtrees. This combination allows for the unique construction of the binary tree.

Image 1
Image 2
Image 3

1/3


Importance of Inorder Traversal
Inorder traversal is crucial for constructing a unique binary tree. Preorder and postorder traversals alone do not provide explicit division between left and right subtrees, leading to multiple possible structures for nodes with a single child.


Full Binary Tree Case
For a full binary tree, where every node has either zero or two children, the structure is fixed. Preorder and postorder traversals provide sufficient information to uniquely reconstruct the tree due to the absence of single-child nodes.

Approach
To determine if a unique binary tree can be constructed from two given traversals identify combinations that fail to provide sufficient information for unique reconstruction. Return false if the two traversals are the same, as they do not provide additional distinguishing information, or if the traversals are preorder and postorder, which cannot uniquely define a binary tree due to their inability to differentiate between certain tree structures. By checking these conditions, the solution ensures that only valid traversal pairs, which can uniquely define a binary tree, are considered.

class Solution:
    # Method to check if a unique binary tree can be constructed
    def unique_binary_tree(self, a, b):
        # Return false if both traversals are the same
       #  or if they are preorder and postorder
        return not (a == b or (a == 1 and b == 3) or (a == 3 and b == 1))

if __name__ == "__main__":
    solution = Solution()
    # Example test cases
    print(solution.unique_binary_tree(1, 2)) 
    print(solution.unique_binary_tree(1, 3)) 

Complexity Analysis
Time Complexity: The time complexity of this solution is O(1) because it involves only a few constant-time comparisons and logical operations. There are no loops or recursive calls that depend on the input size.

Space Complexity: The space complexity of this solution is also O(1) since it uses a constant amount of extra space, regardless of the size of the input. The method only involves a few integer variables and does not allocate additional memory based on the input size.


'''
class Solution:
    def unique_binary_tree(self, a, b):
        return not (a == b or (a == 1 and b == 3) or (a == 3 and b == 1))
    