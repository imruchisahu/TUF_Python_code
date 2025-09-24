'''
Given the root node of a binary search tree (BST) and an integer key. Return the Inorder predecessor and successor of the given key from the provided BST.



Note: key will always present in given BST.



If predecessor or successor is missing then return -1.


Examples:
Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 10

Output : [7, 12]

Explanation :



Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 12

Output : [10, -1]

Explanation :



Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 1

Output:
[-1, 2]
[1, 2]
[4, 7]
[2, -1]

Submit
Constraints:
1 <= Number of Nodes <= 104
1 <= Node.val <= 105
All the values Node.val are unique.


#Brute
Intuition
To find the successor/predecessor of a given node in a Binary Search Tree (BST), an efficient approach involves performing an in-order traversal of the tree. This traversal generates a sorted list of node values due to the inherent properties of BSTs. Once the sorted list is obtained, a binary search can be conducted on this list to identify the first value greater than the given key, which will be the successor. If the given key is the maximum value in the BST, it will be the last node in the in-order traversal, and hence, the successor does not exist.

Algorithm
Traverse the BST in an in-order manner (Left, Root, Right).
During the traversal, store each node's value in a list. This ensures that the list is sorted in ascending order.
After completing the in-order traversal, the list will contain the BST's node values in sorted order.
Perform a binary search on this sorted list to find the given key.
If such a value is found, its previous will be the predecessor (if it exists) and its next node will be the successor (if it exists) of the given key.
If either predecessor or successor doesn't exist, set it as -1.
Store the values and return the values in a list.

# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def succPredBST(self, root, key):
        sortedList = []
        # Perform in-order traversal to get the sorted list of node values
        self.inorderTraversal(root, sortedList)

        predecessor = -1
        successor = -1

        # Find the key in the inorder list using binary search
        ind = self.binarySearch(sortedList, key)

        if ind > 0:
            predecessor = sortedList[ind - 1]
        if ind < len(sortedList) - 1:
            successor = sortedList[ind + 1]

        return [predecessor, successor]

    # Helper function to perform in-order traversal
    def inorderTraversal(self, node, sortedList):
        if not node:
            return
        self.inorderTraversal(node.left, sortedList)
        sortedList.append(node.data)
        self.inorderTraversal(node.right, sortedList)

    # Helper function to perform binary search 
    def binarySearch(self, arr, key):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# Example usage
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(12)

    sol = Solution()
    result = sol.succPredBST(root, 10)
    print(result)  # Output: [7, 12]

Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the BST.
Finding the inorder traversal takes O(N) time, and the binary search on the sorted list takes O(logN) time.
Thus, the overall time complexity is O(N) + (logN) ~= O(N)

Space Complexity: O(N)
Storing the inorder traversal takes O(N) space and recursive stack space to find the inorder-traversal takes O(H) space, where H is the height of the tree.
Thus, the overall space complexity is O(N) + O(H) ~= O(N).



#BEtter Approach
Intuition
An optimized approach to finding both the inorder predecessor and successor in a Binary Search Tree (BST) involves leveraging the properties of BSTs during traversal. Since an inorder traversal of a BST yields nodes in ascending order, the predecessor of a given key is the closest smaller value, while the successor is the closest greater value.

Algorithm
Begin by performing an inorder traversal of the Binary Search Tree (BST), which can be done using traditional recursive/iterative methods or the Morris Inorder Traversal technique for optimized space complexity.
During the traversal, continuously monitor each node:
Keep track of the last node whose value is less than the specified key; this will represent the inorder predecessor.
Identify the first node whose value is greater than the specified key; this will represent the inorder successor.
When the traversal is complete, the nodes identified in the above steps correspond to the inorder predecessor and successor of the given key.
Return the results:
If no smaller node exists, the predecessor is undefined (or null).
If no greater node exists, the successor is undefined (or null).

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def succPredBST(self, root, key):
        predecessor, successor = -1, -1
        prev = [None]

        def inorderTraversal(node):
            nonlocal predecessor, successor
            if not node:
                return

            # Traverse left
            inorderTraversal(node.left)

            # Process current node
            if prev[0] and prev[0].data < key:
                predecessor = prev[0].data  # last node smaller than key
            if successor == -1 and node.data > key:
                successor = node.data  # first node greater than key

            prev[0] = node

            # Traverse right
            inorderTraversal(node.right)

        inorderTraversal(root)
        return [predecessor, successor]

# Example Usage
if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)

    sol = Solution()
    print(sol.succPredBST(root, 12))  # Output: [10, 15]

Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in BST
In the worst case, inorder traversal will take O(N) time and in each recursive call, constant time operations are performed taking overall O(N) time complexity.

Space Complexity: O(H), where H is the height of the tree
In the worst case, recursive stack space will take O(H) space.


#Optimal Approach
Intuition
In a BST, nodes smaller than the key serve as potential predecessors, while nodes larger than the key serve as potential successors. Traversal naturally updates these candidates, and the key’s subtrees provide the most accurate values when the exact node is found.

Algorithm
Start from the root of the BST.
Move right when the key is greater, updating the possible predecessor.
Move left when the key is smaller, updating the possible successor.
Upon finding the key, explore the left subtree to locate the largest smaller value.
Explore the right subtree to locate the smallest larger value.
Return the values of predecessor and successor, or -1 if they do not exist.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def succPredBST(self, root: TreeNode, key: int):
        predecessor = None
        successor = None
        curr = root

        while curr:
            if key > curr.data:
                # Current node could be predecessor
                predecessor = curr
                curr = curr.right
            elif key < curr.data:
                # Current node could be successor
                successor = curr
                curr = curr.left
            else:
                # Found the node
                # Check left subtree for predecessor
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    predecessor = temp

                # Check right subtree for successor
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    successor = temp
                break

        predVal = predecessor.data if predecessor else -1
        succVal = successor.data if successor else -1

        return [predVal, succVal]

# Example usage
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    result = sol.succPredBST(root, 4)
    print(result)

Complexity Analysis
Time Complexity: O(H), where H is the height of the BST.
The while loop traverses down the BST from the root until the key is found (or a leaf is reached) which takes O(H) time. Once the key is found:

Finding the predecessor requires traversing to the rightmost node of the left subtree, which takes at most O(H).
Finding the successor requires traversing to the leftmost node of the right subtree, which also takes at most O(H).
Thus, the overall time complexity is O(H).

Space Complexity: O(1), because of only constant space being used.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def succPredBST(self, root, key):
        predecessor = None
        successor = None
        curr = root

        while curr:
            if key > curr.data:
                # Current node could be predecessor
                predecessor = curr
                curr = curr.right
            elif key < curr.data:
                # Current node could be successor
                successor = curr
                curr = curr.left
            else:
                # Found the node
                # Check left subtree for predecessor
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    predecessor = temp

                # Check right subtree for successor
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    successor = temp
                break

        predVal = predecessor.data if predecessor else -1
        succVal = successor.data if successor else -1

        return [predVal, succVal]
