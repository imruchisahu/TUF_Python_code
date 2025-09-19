'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Examples:
Input : root = [3, 9, 20, null, null, 15, 7]

Output : [ [3] , [9, 20] , [15, 7] ]

Explanation :





Input : root = [1, 4, null, 4 2]

Output : [ [1] , [4] , [4, 2] ]

Explanation :





Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]

Output:
[5, 1, 2, 8, 4, 5, 6]
Constraints:
0 <= Number of Nodes <= 2000
-1000 <= Node.val <= 2000

#Queue-Based-Approach
Intuition
To traverse a binary tree level by level and capture the values of nodes at each level, we use a method known as level-order traversal. This approach involves examining nodes one level at a time, starting from the root and moving downward through the tree. By using a queue to keep track of nodes at each level, we ensure that nodes are processed in the order they appear at each level. This method efficiently organizes nodes into a 2D structure where each sub-array represents a level of the tree, capturing the complete structure of the tree from top to bottom.

Approach
To perform a level-order traversal iteratively, follow these steps:

Start by initializing an empty queue to hold nodes as we traverse the tree level by level.
Enqueue the root node into the queue. If the tree is empty, return an empty 2D vector immediately.
While the queue is not empty, process each level of the tree:
Determine the number of nodes at the current level by checking the size of the queue.
Create a temporary vector to store the values of nodes at this level.
For each node at the current level:
Dequeue the front node from the queue.
Store the node’s value in the temporary vector.
Enqueue the left and right children of the current node (if they exist) into the queue.
After processing all nodes at the current level, add the temporary vector to the final 2D vector representing the level order traversal.
Once all levels are processed, return the 2D vector containing the level-order traversal of the binary tree.
Dry Run
Here's how the level-order traversal works step-by-step:

Step 1: Initialise an empty queue and a 2D vector to store the level-order traversal result. If the binary tree is empty, return this empty 2D vector.
Step 2: Add the root node to the queue. This starts the traversal process from the top of the tree.
Step 3: While the queue is not empty, perform the following:
Get the size of the queue, which indicates the number of nodes at the current level.
Create a temporary vector to store the nodes' values for the current level.
Iterate through the number of nodes at the current level:
Dequeue the front node from the queue.
Add the node’s value to the temporary vector.
Enqueue the left and right children of this node (if they exist) into the queue.
After processing all nodes at the current level, add the temporary vector to the 2D vector.

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to perform level-order traversal of a binary tree
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty, return an empty list
            return ans
        
        # Create a queue to store nodes for level-order traversal
        q = deque([root])
        
        while q:
            # Create a list to store nodes at the current level
            level = []
            for _ in range(len(q)):
                # Get the front node from the queue
                node = q.popleft()
                # Add the node value to the current level list
                level.append(node.data)
                
                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add the current level to the answer list
            ans.append(level)
        # Return the level-order traversal of the tree
        return ans

# Function to print the elements of a list
def printList(lst):
    # Iterate through the list and print each element
    for num in lst:
        print(num, end=' ')
    print()

# Main function to test the level-order traversal
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Create an instance of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)
    
    print("Level Order Traversal of Tree:")
    # Printing the level order traversal result
    for level in result:
        printList(level)

Complexity Analysis :
Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is enqueued and dequeued exactly once, hence all nodes need to be processed and visited. Processing each node takes constant time operations which contributes to the overall linear time complexity.

Space Complexity: O(N) where N is the number of nodes in the binary tree. In the worst case, the queue has to hold all the nodes of the last level of the binary tree; the last level could at most hold N/2 nodes, hence the space complexity of the queue is proportional to O(N). The resultant vector answer also stores the values of the nodes level by level and hence contains all the nodes of the tree contributing to O(N) space as well.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            # If the tree is empty, return an empty list
            return ans
        
        # Create a queue to store nodes for level-order traversal
        q = deque([root])
        
        while q:
            # Create a list to store nodes at the current level
            level = []
            for _ in range(len(q)):
                # Get the front node from the queue
                node = q.popleft()
                # Add the node value to the current level list
                level.append(node.data)
                
                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add the current level to the answer list
            ans.append(level)
        return ans
    