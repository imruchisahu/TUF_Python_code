'''
Given the root of a binary tree, return the maximum width of the given tree.



The maximum width of a tree is the maximum width among all levels. The width of a level is determined by measuring the distance between its end nodes, which are the leftmost and rightmost non-null nodes. The length calculation additionally takes into account the null nodes that would be present between the end nodes if a full binary tree were to stretch down to that level.


Examples:
Input : root = [1, 3, 2, 5, 3, null, 9]

Output : 4

Explanation :

So if the below tree would be a full binary tree then there would be total 4 nodes in the last level.

So the maximum width of the binary tree is between the nodes with value 5 and 9 is equal to 4.



Input : root = [1, 3, 2, 5, null, null, 9, 6, null, 7]

Output : 7

Explanation :

If the below tree would be a full binary tree then at last levels there would b 7 nodes including the node with value 6 and 7.

So the maximum width of binary tree is 7.



Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
4
Constraints:
1 <= Number of Nodes <= 3000
-1000 <= Node.val <= 1000

Intuition
The objective is to determine the maximum width of a binary tree, which is defined as the widest level of the tree in terms of node count. To achieve this, we track the leftmost and rightmost node indices at each level. By calculating the width at each level using these indices, we can ascertain the maximum width of the tree. The approach involves assigning an index to the root node and then using level-order traversal to explore the tree. The index of each child node is derived from its parent node's index, which facilitates the calculation of widths at each level. This method ensures a systematic and efficient evaluation of the tree's width, ultimately identifying the maximum width observed throughout the traversal.

Approach
Begin by initializing a variable ans to keep track of the maximum width encountered. If the root node is null, return 0 as the width of an empty tree is zero.
Set up a queue for level-order traversal, where each queue element is a Pair consisting of a node and its index within the level. Start by enqueuing the root node along with its initial index of 0.
While the queue contains elements, process each level as follows:
Determine the number of nodes at the current level by measuring the size of the queue. Capture the index of the first node in the level to establish the leftmost position at that level.
Initialize variables first and last to record the indices of the first and last nodes at the current level.
For each node in the current level, compute its relative position based on the level's minimum index. Update the first and last variables to reflect the indices of the first and last nodes in this level. Enqueue the left and right children of the current node, assigning them indices of 2 x current index and 2 x current index + 1, respectively.
Pair Class Definitio
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function widthOfBinaryTree to find the 
    # maximum width of the Binary Tree
    def widthOfBinaryTree(self, root):
        # If the root is null,
        # the width is zero
        if not root:
            return 0

        # Initialize a variable 'ans'
        # to store the maximum width
        ans = 0

        # Create a queue to perform level-order
        # traversal, where each element is a pair
        # of TreeNode* and its position in the level
        q = deque([(root, 0)])

        # Perform level-order traversal
        while q:
            # Get the number of
            # nodes at the current level
            size = len(q)
            # Get the position of the front
            # node in the current level
            mmin = q[0][1]

            # Store the first and last positions 
            # of nodes in the current level
            first = last = 0

            # Process each node
            # in the current level
            for i in range(size):
                # Calculate current position relative
                # to the minimum position in the level
                cur_id = q[0][1] - mmin
                # Get the current node
                node = q[0][0]
                # Pop the front node from the queue
                q.popleft()

                # If this is the first node in the level, 
                # update the 'first' variable
                if i == 0:
                    first = cur_id

                # If this is the last node in the level,
                # update the 'last' variable
                if i == size - 1:
                    last = cur_id

                # Enqueue the left child of the 
                # current node with its position
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))

                # Enqueue the right child of the
                # current node with its position
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))

            # Update the maximum width by calculating
            # the difference between the first and last
            # positions, and adding 1
            ans = max(ans, last - first + 1)

        # Return the maximum
        # width of the binary tree
        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()
    maxWidth = sol.widthOfBinaryTree(root)

    print("Maximum width of the binary tree is:", maxWidth)


Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).


'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        ans = 0
        q = deque([(root, 0)])
        while q:
            size = len(q)
            mmin = q[0][1]
            first = last = 0
            for i in range(size):
                cur_id = q[0][1] - mmin
                node = q[0][0]
                q.popleft()
                if i == 0:
                    first = cur_id
                if i == size - 1:
                    last = cur_id
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))
            ans = max(ans, last - first + 1)
        return ans

