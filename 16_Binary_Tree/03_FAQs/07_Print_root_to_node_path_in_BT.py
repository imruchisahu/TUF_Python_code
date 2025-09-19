'''
Given the root of a binary tree. Return all the root-to-leaf paths in the binary tree.



A leaf node of a binary tree is the node which does not have a left and right child.


Examples:
Input : root = [1, 2, 3, null, 5, null, 4]

Output : [ [1, 2, 5] , [1, 3, 4] ]

Explanation : There are only two paths from root to leaf.

From root 1 to 5 , 1 -> 2 -> 5.

From root 1 to 4 , 1 -> 3 -> 4.



Input : root = [1, 2, 3, 4, 5]

Output : [ [1, 2, 4] , [1, 2, 5] , [1, 3] ]

Explanation :



Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]



Output:
[ [1, 2, 4, 7] , [1, 3, 5] , [1, 3, 6] ]
Constraints:
1 <= Number of Nodes <= 3*103
-103 <= Node.val <= 103

Intuition
To determine the path from the root to a specific node in a binary tree, a Depth-First Search (DFS) strategy is employed. This technique involves initializing a vector to record the current path and then performing a recursive traversal of the tree. At each node, the algorithm checks if it is null, which would signify the end of a path and prompt a return of false. If the node’s value matches the target value, the traversal is complete, and true is returned, indicating that the target node has been successfully located.

During the traversal, the value of each visited node is added to the path vector. The algorithm proceeds by recursively exploring both the left and right subtrees. If the target node is not found in the current path, the algorithm backtracks by removing the last node from the path vector, allowing exploration of alternative paths. Ultimately, the function returns a vector that represents the path from the root to the specified target node.

Approach
Initialize an empty vector allPaths to store all root-to-leaf paths.
Use a helper function for DFS traversal that keeps a temporary vector currentPath.
At each node, add its value to currentPath.
If it’s a leaf node (both left and right are nullptr), add currentPath to allPaths.
Otherwise, recursively traverse the left and right children.
After both recursive calls, remove the last element from currentPath to backtrack and explore new paths.
Return allPaths after the traversal completes.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def allRootToLeaf(self, root):
        # Initialize an empty list to store all paths
        all_paths = []
        
        # Helper function to perform DFS and find all paths
        def dfs(node, path):
            if not node:
                return
            
            # Append the current node's data to the path
            path.append(node.data)
            
            # If it's a leaf node, append the path to all_paths
            if not node.left and not node.right:
                all_paths.append(list(path))
            else:
                # Recursively call the function on the left and right children
                dfs(node.left, path)
                dfs(node.right, path)
            
            # Backtrack by removing the current node from the path
            path.pop()
        
        # Call the helper function with the root node and an empty path
        dfs(root, [])
        
        return all_paths

# Example usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    solution = Solution()
    print(solution.allRootToLeaf(root))

Complexity Analysis
Time Complexity : O(N) where N is the number of nodes in the binary tree. Each node of the binary tree is visited exactly once during the traversal.

Space Complexity : O(N) where N is the number of nodes in the binary tree. This is because the stack can potentially hold all nodes in the tree when dealing with a skewed tree (all nodes have only one child), consuming space proportional to the number of nodes.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        all_paths = []
        def dfs(node, path):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                all_paths.append(list(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return all_paths
    