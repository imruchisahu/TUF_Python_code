'''
Given root of binary tree, return the bottom view of the binary tree.



The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the node that appears later in level traversal.


Examples:
Input : root = [20, 8, 22, 5, 3, null, 25, null, null, 10 ,14]

Output : [5, 10, 3, 14, 25]

Explanation : From left to right the path is as follows :

First we encounter node with value 5.

Then we have nodes 8 , 10 but from bottom only 10 will be visible.

Next we have 20 , 3 but from bottom only 3 will be visible.

Next we have 14 , 22 but from bottom only 14 will be visible.

Then we encounter node with value 25.



Input : root = [20, 8, 22, 5, 3, 4, 25, null, null, 10 ,14]

Output : [5, 10, 4, 14, 25]

Explanation : From left to right the path is as follows :

First we encounter node with value 5.

Then we have nodes 8 , 10 but from bottom only 10 will be visible.

Next we have 20 , 3 and 4. The 3 and 4 will be nodes visible from bottom but as the node 4 appears later from left to right , so only node 4 will be considered visible.

Next we have 14 , 22 but from bottom only 14 will be visible.

Then we encounter node with value 25.



Input: root = [10, 20, 30, 40, 60]





Output:
[40, 20, 60, 30]
Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103

Intuition
To determine the bottom view of a binary tree, we need to capture the nodes that are visible when observing the tree from below. This involves identifying nodes that appear at the lowest vertical level for each horizontal distance from the root. A Breadth-First Search (BFS) traversal is well-suited for this task, as it processes nodes level by level. By tracking the horizontal distance of each node from the root and storing the most recent node encountered at each distance in a map, we can accurately capture the bottom view. The horizontal distance helps in maintaining the vertical alignment of nodes, ensuring that we only keep the nodes that are visible from the bottom.

Approach
Begin by initializing an empty vector to hold the final result of the bottom view.
If the tree is empty (i.e., the root is null), immediately return the empty result vector.
Create a map to store nodes based on their horizontal distances from the root. The map's key will be the horizontal distance, and the value will be the node's data, ensuring that only the latest node for each distance is recorded.
Set up a queue to facilitate BFS traversal. Each entry in the queue will be a pair consisting of a node and its corresponding horizontal distance.
Start the BFS traversal by enqueuing the root node with a horizontal distance of 0.
While the queue contains elements, execute the following steps:
Dequeue the front element to retrieve the node and its associated horizontal distance.
Update the map with the node's value for the current horizontal distance, ensuring that only the most recent node at each distance is stored.
If the node has a left child, enqueue this child with a horizontal distance one less than the current node's distance.
If the node has a right child, enqueue this child with a horizontal distance one more than the current node's distance.
After completing the BFS traversal, extract the values from the map in ascending order of their horizontal distances and store them in the result vector.
Return the result vector, which now contains the bottom view of the binary tree.
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root):
        # List to store the result
        ans = []

        # Check if the tree is empty
        if not root:
            return ans

        # Dictionary to store the bottom view nodes
        # based on their vertical positions
        mpp = {}

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical position
        q = deque([(root, 0)])

        # BFS traversal
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()

            # Update the dictionary with the node's data
            # for the current vertical position
            mpp[line] = node.data

            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))

            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))

        # Transfer values from the
        # dictionary to the result list
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])

        return ans

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    solution = Solution()

    # Get the Bottom View traversal
    bottom_view = solution.bottomView(root)

    # Print the result
    print("Bottom View Traversal: ")
    for node in bottom_view:
        print(node, end=" ")

        
Complexity Analysis
Time Complexity: O(N*logN), where N is the number of nodes in the binary tree.
This arises from visiting each node exactly once during the BFS traversal that takes O(N) time. Each node is then inserted in the map, taking O(logH) (where H is the number of unique horizontal distances, which can be up to N in the worst case) time. Thus, in the worst case, the overall time complexity comes out to be O(N*logN).

Space Complexity: O(N), where N represents the number of nodes in the binary tree.
The main space-consuming data structure is the queue used for BFS traversal. In the worst case of a balanced binary tree, the queue will have at most N/2 nodes, representing the maximum width of the tree.
'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def bottomView(self, root):
        ans =[]
        if not root:
            return ans
        mpp ={}
        q=deque([(root, 0)])
        while q:
            node, line = q.popleft()
            mpp[line] = node.data
            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])

        return ans
        
        

