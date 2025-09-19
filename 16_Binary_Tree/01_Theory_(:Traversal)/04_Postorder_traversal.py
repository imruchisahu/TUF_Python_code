'''
Given root of binary tree, return the Postorder traversal of the binary tree.


Examples:
Input : root = [1, 4, null, 4, 2]

Output : [4, 2, 4, 1]

Explanation :





Input : root = [1, null, 2, 3]

Output : [3, 2, 1]

Explanation :





Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[1]
Constraints:
1 <= Number of Nodes <= 100
-100 <= Node.val <= 100

#Recursive Approach
Intuition:
Postorder traversal is another method for exploring trees, where we follow the sequence of exploring the left subtree first, then the right subtree, and finally visiting the root node. This approach ensures that we only process the current node after we have fully traversed its left and right subtrees. The order we follow is Left, Right, and then Root.

Approach:
In postorder traversal, the method starts by fully exploring the left subtree, followed by the right subtree, and then processing the current node. This traversal method is particularly useful in scenarios where you need to ensure that both child nodes are processed before the parent node. We use a recursive approach to naturally follow this sequence, with each call diving deeper into the left and right children before handling the current node.

Dry Run
Let's break down the steps and the data structures involved:

Step 1: Check if the current node is null. If it is, we've reached the end of a subtree, and the recursive function stops.
Step 2: Recursively traverse the left subtree. This means making a call to the postorder function on the left child of the current node.
Step 3: Recursively traverse the right subtree by calling the postorder function on the right child of the current node.
Step 4: Process the current node by adding its value to the postorder traversal array. This step is done after the left and right subtrees have been fully explored.
This recursive approach uses the call stack to manage the traversal, ensuring that each node is visited in the correct postorder sequence.


Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the given tree.
Each node is visited exactly once during the traversal and at each node, we perform constant time operations (checking null, function calls, push_back). Thus, the overall Time Complexity is O(N).

Space Complexity: O(N)
The recursive stack space will be equal to the height of the tree, which can be O(N) in worst case (in case of skewed tree). Also, the result array takes O(N) space to store the postorder traversal. Thus, the overall Space Complexity is O(2N) or O(N).

#Iterative Approach
Intuition:
The idea behind the iterative approach will be to use a stack to perform postorder traversal to mimick the recursive stack. A recursive approach naturally follows this order by going left, then right, and finally visiting the root when returning from recursion. But in an iterative approach, we don't have the function call stack to track nodes, so we need a way to simulate this order.

A key observation is that if we traverse the tree in Root → Right → Left order (a modified preorder), the result will be a reverse of postorder. This means that if we store nodes in this reversed order and then reverse the list at the end, we get the desired postorder sequence.

Approach:
Push the root node onto the stack to begin traversal.
Process nodes in a modified preorder order (Root → Right → Left) by popping a node, storing its value, and pushing its left and right children onto the stack (right first, then left).
Continue until the stack is empty, ensuring all nodes are processed in this modified order.
Reverse the stored result at the end to transform it into the correct postorder sequence (Left → Right → Root).
Return the final postorder traversal list.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to perform postorder traversal on the tree
    def postorder(self, root):
        result = []  # to store the result
        
        nodeStack = []  # stack to process the nodes
        if root:
            nodeStack.append(root)  # push the root initially
        
        # Until the stack is empty 
        while nodeStack:
            node = nodeStack.pop()  # get the top node 
            
            result.append(node.data)  # add it to the list
            
            # Add its left child if it exists
            if node.left:
                nodeStack.append(node.left)
            
            # Add its right child if it exists
            if node.right:
                nodeStack.append(node.right)
        
        # Reverse the list to get the postorder traversal
        result.reverse()

        return result  # Return the result

# Create a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Create Solution object and call postorder method
sol = Solution()
result = sol.postorder(root)

# Print the result
print(" ".join(map(str, result)))  # Output: 4 5 2 6 3 1

Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the tree. Because traversing each nodes once takes O(N) time.

Space Complexity: O(H), where H is the height of the tree. Due to the stack used to mimick the recursive stack behaviour.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursive_postorder(self, root, arr):
        if root is None:
            return
        self.recursive_postorder(root.left, arr)
        self.recursive_postorder(root.right, arr)
        arr.append(root.val)

    def postorder(self, root):
        arr = []
        self.recursive_postorder(root, arr)
        return arr
    