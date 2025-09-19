'''
Compute the binary tree's vertical order traversal given its root.

The left and right children of a node at location (row, col) will be at (row + 1, col - 1) and (row + 1, col + 1), respectively. The tree's root is located at (0, 0).



The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the binary tree's vertical order traversal.


Examples:
Input : root = [3, 9, 20, null, null, 15, 7]

Output : [ [9] , [3, 15] , [20] , [7] ]

Explanation :

Column -1: Only node 9 is in this column.

Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.

Column 1: Only node 20 is in this column.

Column 2: Only node 7 is in this column.



Input : root = [1, 2, 3, 4, 5, 6, 7]

Output : [ [4] , [2] , [1, 5, 6] , [3] , [7] ]

Explanation :

Column -2: Only node 4 is in this column.

Column -1: Only node 2 is in this column.

Column 0: Nodes 1, 5, and 6 are in this column.1 is at the top, so it comes first. 5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.

Column 1: Only node 3 is in this column.

Column 2: Only node 7 is in this column.



Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[ [8], [1, 6], [5, 4], [2], [5] ]
Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103

Intuition
The vertical order traversal of a binary tree involves organizing nodes based on their horizontal and vertical positions relative to their parent nodes. Each node can be categorized by its vertical column ('x') and level ('y'). Nodes with the same 'x' value are aligned vertically, forming columns, while 'y' represents the depth or level within the tree.

To achieve this traversal, use a level order BFS approach, starting from the root node. This ensures that nodes are processed level by level, and within each level, nodes are processed from left to right. By maintaining a map structure that uses 'x' as keys for vertical columns and 'y' as keys within a nested map for levels, we store node values in a multiset to maintain uniqueness and sorting.


Approach
Begin by initializing an empty map to store nodes according to their 'x' (vertical column) and 'y' (level) coordinates. Utilize a multiset within this map to maintain the correct order of nodes that fall under the same vertical column and level.
Set up a queue for performing a breadth-first search (BFS) traversal of the tree, starting with the root node positioned at coordinates (0, 0), where '0' represents the root's vertical column and level.
While the queue is not empty, perform the following steps: dequeue a node, and record its value in the map at its corresponding 'x' and 'y' coordinates. Then, enqueue the left and right children of the node with updated coordinates: the left child is enqueued with 'x' decremented by 1 and 'y' incremented by 1, while the right child is enqueued with 'x' incremented by 1 and 'y' incremented by 1.
After completing the BFS traversal, process the map to create a list of node values for each vertical column. This involves iterating through the map, collecting values from the multiset for each vertical column, and assembling these values into column vectors.
Finally, compile these column vectors into a 2D vector that represents the vertical order traversal of the binary tree, ensuring that nodes are ordered by their vertical column positions.
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        """
        Perform vertical order traversal of a binary tree.

        :param root: TreeNode - The root of the binary tree.
        :return: List[List[int]] - A list of lists containing the vertical order traversal.
        """

        if not root:
            return []

        # Dictionary to store the nodes at each vertical distance and level.
        # nodes_map[x][y] will hold a list of nodes at vertical distance x and level y.
        nodes_map = defaultdict(lambda: defaultdict(list))

        # Queue for BFS traversal (stores node along with its x and y coordinates)
        queue = deque([(root, 0, 0)])  # (node, x, y)

        # Perform BFS to populate nodes_map with nodes at each (x, y) coordinate.
        while queue:
            node, x, y = queue.popleft()

            # Add the node's value to the map at the correct x and y
            nodes_map[x][y].append(node.data)

            # Add the left child with updated coordinates to the queue
            if node.left:
                queue.append((node.left, x - 1, y + 1))

            # Add the right child with updated coordinates to the queue
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        # Prepare the result by sorting keys and compiling nodes
        result = []
        for x in sorted(nodes_map):
            column = []
            for y in sorted(nodes_map[x]):
                # Sort the nodes at the same position to maintain the order
                column.extend(sorted(nodes_map[x][y]))
            result.append(column)

        return result

# Main method to test the verticalTraversal function
if __name__ == "__main__":
    # Creating a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Creating an instance of Solution
    sol = Solution()

    # Getting the vertical order traversal
    result = sol.verticalTraversal(root)

    # Printing the result
    print("Vertical Order Traversal:", result)

    
Complexity Analysis
Time Complexity:O(N * log2N * log2N * log2N) : This complexity arises from performing postorder traversal using BFS, where each node's insertion and retrieval operations in nested maps take logarithmic time. Overall, it reflects the combined cost of processing each node and managing the node mappings.

Space Complexity: O(N + N/2) : The space usage is dominated by the map storing nodes by their vertical and level information, occupying O(N) space. Additionally, the queue for BFS can occupy up to O(N/2) space in a balanced tree's worst-case scenario, contributing to the total space complexity.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []
        nodes_map = defaultdict(lambda: defaultdict(list))
        queue = deque([(root, 0, 0)])  # (node, x, y)
        while queue:
            node, x, y = queue.popleft()
            nodes_map[x][y].append(node.data)
            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))
        result = []
        for x in sorted(nodes_map):
            column = []
            for y in sorted(nodes_map[x]):
                column.extend(sorted(nodes_map[x][y]))
            result.append(column)

        return result