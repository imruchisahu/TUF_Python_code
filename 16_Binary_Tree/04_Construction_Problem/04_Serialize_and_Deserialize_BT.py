'''

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.



Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. Ensure that a binary tree can be serialized to a string, and this string can be deserialized to the original tree structure.



The encoded string should be as compact as possible.


Examples:
Input : root = [2, 1, 3]

Output : [2, 1, 3]

Input : root = [7, 3, 15, null, null, 9, 20]

Output : [7, 3, 15, null, null, 9, 20]

Input : root = [10, 20, 30, 40, 50, 60]

Output:
[10, 20, 30, 40, 50, 60]
[10, 30, 20, 40, 50, 60]
[10, 20, 30, 50, 40, 60]
[10, 20, 40, 30, 50, 60]

Submit
Constraints:
1 <= Number of Nodes <= 104
0 <= Node.val <= 104

Serialisation
Intuition
The concept of serializing a binary tree involves transforming its structure into a string format that preserves the hierarchical arrangement of nodes. By utilizing level-order traversal (BFS), we can ensure that nodes are processed in the order of their levels, which simplifies the reconstruction of the tree during deserialization. In this approach, each node's value is recorded in the string, while null nodes are represented by a special placeholder (e.g., "#") to maintain the integrity of the tree structure.

Approach
First, check if the tree is empty. If the root is null, return an empty string. Otherwise, initialize an empty string to hold the serialized data of the binary tree.
Utilize a queue for level-order traversal. Begin by initializing a queue and enqueueing the root node.
In the level-order traversal process: Dequeue a node from the queue. If the node is null, append "#" to the string. If the node is not null, append its value followed by a comma (",") to the string and enqueue its left and right children.
Continue this process until the queue is empty, and then return the final string which contains the complete serialized representation of the binary tree.
Dry run
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6

1/6


Deserialization
Intuition
Deserialization involves reconstructing a binary tree from its serialized string representation. The process relies on level-order traversal (BFS) to read the nodes in the sequence they appear in the serialized data, facilitating accurate tree reconstruction. Each node's value is extracted from the string, with null nodes represented by a specific character (e.g., "#") to denote the absence of a child node.

Approach
Start by checking if the serialized string is empty. If it is, return null as there is no tree to reconstruct.
Split the serialized string into individual node values using a comma delimiter. The first value represents the root of the tree, which should be used to create the root node. Initialize a queue and enqueue the root node to facilitate level-order construction.
Perform level-order traversal: Dequeue a node from the queue. Read the next value from the tokenized data to determine the left child. If this value is "#", set the left child to null; otherwise, create a new node. Repeat the process for the right child. If the right child’s value is "#", set it to null; otherwise, create a new node. Enqueue both left and right children for further processing.
Continue the traversal until all nodes are processed and the queue is empty. Finally, return the root node of the fully reconstructed binary tree.
from collections import deque

# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
    def serialize(self, root):
        """
        Encodes the tree into a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # Initialize an empty string to store the serialized data
        result = []
        # Use a queue for level-order traversal
        q = deque([root])

        # Perform level-order traversal
        while q:
            node = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                # Push the left and right children to the queue for further traversal
                q.append(node.left)
                q.append(node.right)

        # Return the serialized string
        return ",".join(result)

    def deserialize(self, data):
        """
        Decodes the encoded data to a tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        # Use a deque to tokenize the serialized data
        data = deque(data.split(","))
        # Read the root value from the serialized data
        root = TreeNode(int(data.popleft()))

        # Use a queue for level-order traversal
        q = deque([root])

        # Perform level-order traversal to reconstruct the tree
        while q:
            node = q.popleft()

            # Read the value of the left child from the serialized data
            left_val = data.popleft()
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)

            # Read the value of the right child from the serialized data
            right_val = data.popleft()
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)

        # Return the reconstructed root of the tree
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# Testing the Solution
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()
    print("Original Tree: ", end="")
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    inorder(root)
    print()

    serialized = solution.serialize(root)
    print("Serialized:", serialized)

    deserialized = solution.deserialize(serialized)
    print("Tree after deserialization: ", end="")
    inorder(deserialized)
    print()

    
Complexity Analysis
Time Complexity: O(N) Both serialize and deserialize functions have a time complexity of O(N), where N is the number of nodes in the tree. This is because each function processes every node once.

Space Complexity: O(N) Both serialize and deserialize functions have a space complexity of O(N). This space is used by the queue to hold nodes at various levels of the tree during traversal and reconstruction.

'''
from collections import deque 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, root):
        if not root:
            return ""
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)


    def deserialize(self, data):
        if not data:
            return None
        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        q = deque([root])
        while q:
            node = q.popleft()
            left_val = data.popleft()
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            right_val = data.popleft()
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans