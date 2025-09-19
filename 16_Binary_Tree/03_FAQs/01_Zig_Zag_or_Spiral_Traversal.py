'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


Examples:
Input : root = [1, 2, 3, null, 4, 8, 5]

Output : [ [1] , [3, 2], [4, 8, 5] ]

Explanation : So at root we move from left to right.

At next level we move in opposite direction i.e. from right to left.

At next level again reverse the traversal i.e. from left to right.





Input : root = [3, 9, 20, null, null, 15, 7]

Output : [ [3] , [20, 9], [15, 7] ]

Explanation : So at root we move from left to right.

At next level we move in opposite direction i.e. from right to left , from 20 to 9.

At next level again reverse the traversal i.e. from left to right, from 15 to 7.





Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[ [5], [2, 1], [8, 4, 5], [6] ]
Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103

Intuition
Zigzag traversal of a binary tree is an enhancement of the conventional level order traversal. While level order traversal explores nodes at each level from left to right, zigzag traversal adds an alternating pattern to the process. At odd levels, nodes are processed from left to right, but at even levels, the order is reversed, processing nodes from right to left. This alternation is controlled by a `leftToRight` flag, which determines the direction of node processing at each level. When `leftToRight` is true, nodes are inserted into the level vector from left to right, and when false, nodes are inserted from right to left.

Approach
Begin by initializing an empty queue for node storage during traversal and a 2D vector to capture the level order traversal. If the binary tree is empty, return this empty 2D vector immediately. Additionally, create a leftToRight flag to track the traversal direction. When leftToRight is true, nodes are inserted into the level vector from left to right; when false, they are inserted from right to left.
Enqueue the root node of the binary tree into the queue to start the traversal.
Proceed with the following steps while the queue is not empty:
Determine the current size of the queue, which reflects the number of nodes present at the current level of the tree.
Create a vector named level to store the nodes' values at the current level.
For each node at the current level, remove the front node from the queue, store its value in the level vector (inserting from left to right if leftToRight is true, or from right to left if false), and enqueue its child nodes (if they exist).
After processing all nodes at the current level, append the level vector to the ans 2D vector. Toggle the leftToRight flag to reverse the traversal direction for the subsequent level.
After all levels have been processed, return the ans 2D vector, which contains the zigzag level-order traversal of the binary tree.
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        # List to store the result of zigzag traversal
        result = []

        # Check if the root is NULL, return an empty result
        if not root:
            return result

        # Queue to perform level order traversal
        nodesQueue = deque([root])

        # Flag to determine the direction of traversal (left to right or right to left)
        leftToRight = True

        # Continue traversal until the queue is empty
        while nodesQueue:
            # Get the number of nodes at the current level
            size = len(nodesQueue)

            # List to store the values of nodes at the current level
            row = [0] * size

            # Traverse nodes at the current level
            for i in range(size):
                # Get the front node from the queue
                node = nodesQueue.popleft()

                # Determine the index to insert the node's value based on the traversal direction
                index = i if leftToRight else (size - 1 - i)

                # Insert the node's value at the determined index
                row[index] = node.val

                # Enqueue the left and right children if they exist
                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)

            # Switch the traversal direction for the next level
            leftToRight = not leftToRight

            # Add the current level's values to the result list
            result.append(row)

        # Return the final result of zigzag level order traversal
        return result

# Helper function to print the result
def printResult(result):
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()

    # Get the zigzag level order traversal
    result = solution.zigzagLevelOrder(root)

    # Print the result
    printResult(result)

Complexity Analysis
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree, the last level could at most hold N/2 nodes hence the space complexity of the queue is proportional to O(N).

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result

        nodesQueue = deque([root])
        leftToRight = True
        while nodesQueue:
            size = len(nodesQueue)
            row = [0] * size
            for i in range(size):
                node = nodesQueue.popleft()
                index = i if leftToRight else (size - 1 - i)
                row[index] = node.val
                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)
            leftToRight = not leftToRight
            result.append(row)
        return result
    