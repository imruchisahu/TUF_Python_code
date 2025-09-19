'''
Given a target node data and a root of binary tree. If the target is set on fire, determine the shortest amount of time needed to burn the entire binary tree.



It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.


Examples:
Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]. target = 1

Output : 3

Explanation : The node with value 1 is set on fire.

In 1st second it burns node 2 and node 3.

In 2nd second it burns nodes 4, 5, 6.

In 3rd second it burns node 7.



Input : root = [1, 2, 3, null, 5, null, 4], target = 4

Output : 4

Explanation : The node with value 4 is set on fire.

In 1st second it burns node 3.

In 2nd second it burns node 1.

In 3rd second it burns node 2.

In 4th second it burns node 5.



Input : root = [1, 2, 3, 6, 5, 8, 4], target = 4





Output:
4
Constraints:
1 <= Number of Nodes <= 104
-105 <= Node.val <= 105
All Node.val values are unique.

Intuition
To determine how long it will take for a fire to completely burn a binary tree starting from a specific node, the problem can be effectively solved using a breadth-first search (BFS) approach. The essence of the problem is to simulate the spreading of the fire level by level, considering that the fire can propagate to a node’s left child, right child, and parent. Therefore, it is crucial to maintain a record of each node’s parent to allow traversal up the tree when necessary. By calculating the maximum distance from the starting node to the furthest node affected by the fire, we can determine the total time required for the entire tree to be consumed by the fire.

Approach
Start by using BFS to establish a map where each node is associated with its parent. This mapping helps in tracking the parent of each node, facilitating upward traversal during the fire spread simulation.
Locate the node where the fire begins. This node will serve as the starting point for the BFS that simulates the spread of the fire through the tree.
Initiate another BFS from the starting node to model how the fire spreads through the tree. During this traversal, consider all possible directions: left, right, and upward, ensuring that each node is only processed once.
Keep track of the nodes that have already been visited to avoid redundant processing and to ensure that the BFS traversal is efficient.
Measure the farthest distance reached during the BFS to determine the total time needed for the fire to consume the entire tree. This distance, in terms of BFS levels, represents the time required for complete combustion.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        # Map to store parent nodes
        mpp = {}
        # Get the target node (starting node for burning)
        target = self.bfsToMapParents(root, mpp, start)
        # Find the maximum distance to burn the tree
        maxi = self.findMaxDistance(mpp, target)
        return maxi

    # Method to map parents of all nodes using BFS
    def bfsToMapParents(self, root, mpp, start):
        # Queue for BFS
        q = [root]
        res = None

        while q:
            # Get the front node from the queue
            node = q.pop(0)
            # Check if this is the start node
            if node.data == start:
                res = node
            # Map the left child to its parent
            if node.left:
                mpp[node.left] = node
                q.append(node.left)
            # Map the right child to its parent
            if node.right:
                mpp[node.right] = node
                q.append(node.right)
        return res

    # Method to find the maximum distance to burn the tree
    def findMaxDistance(self, mpp, target):
        # Queue for BFS to find max distance
        q = [target]
        # Set to check visited nodes
        vis = {target}
        maxi = 0

        while q:
            size = len(q)
            fl = 0

            for _ in range(size):
                node = q.pop(0)

                # Check left child
                if node.left and node.left not in vis:
                    fl = 1
                    vis.add(node.left)
                    q.append(node.left)

                # Check right child
                if node.right and node.right not in vis:
                    fl = 1
                    vis.add(node.right)
                    q.append(node.right)

                # Check parent node
                if node in mpp and mpp[node] not in vis:
                    fl = 1
                    vis.add(mpp[node])
                    q.append(mpp[node])

            # Increment max distance if any node was burned
            if fl == 1:
                maxi += 1
        return maxi

# Main function to test the functionality
if __name__ == "__main__":
    sol = Solution()

    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    start = 4

    # Get the time to burn the tree
    result = sol.timeToBurnTree(root, start)
    print("Time to burn the tree:", result)

Complexity Analysis
Time Complexity : O(N) where n is the number of nodes in the tree, due to BFS traversals

SpaceComplexity : O(N) for storing the parent mapping and the visited set.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        mpp = {}
        # Get the target node (starting node for burning)
        target = self.bfsToMapParents(root, mpp, start)
        # Find the maximum distance to burn the tree
        maxi = self.findMaxDistance(mpp, target)
        return maxi

    # Method to map parents of all nodes using BFS
    def bfsToMapParents(self, root, mpp, start):
        # Queue for BFS
        q = [root]
        res = None

        while q:
            # Get the front node from the queue
            node = q.pop(0)
            # Check if this is the start node
            if node.data == start:
                res = node
            # Map the left child to its parent
            if node.left:
                mpp[node.left] = node
                q.append(node.left)
            # Map the right child to its parent
            if node.right:
                mpp[node.right] = node
                q.append(node.right)
        return res

    # Method to find the maximum distance to burn the tree
    def findMaxDistance(self, mpp, target):
        # Queue for BFS to find max distance
        q = [target]
        # Set to check visited nodes
        vis = {target}
        maxi = 0

        while q:
            size = len(q)
            fl = 0

            for _ in range(size):
                node = q.pop(0)

                # Check left child
                if node.left and node.left not in vis:
                    fl = 1
                    vis.add(node.left)
                    q.append(node.left)

                # Check right child
                if node.right and node.right not in vis:
                    fl = 1
                    vis.add(node.right)
                    q.append(node.right)

                # Check parent node
                if node in mpp and mpp[node] not in vis:
                    fl = 1
                    vis.add(mpp[node])
                    q.append(mpp[node])

            # Increment max distance if any node was burned
            if fl == 1:
                maxi += 1
        return maxi

        