'''
Given the root node of a binary search tree (BST) and an integer k.



Return the kth smallest and largest value (1-indexed) of all values of the nodes in the tree.



Return the 1st integer as kth smallest and 2nd integer as kth largest in the returned array.


Examples:
Input : root = [3,1,4,null,2] , k = 1

Output : [1, 4]

Explanation :

The 1st smallest value in given BST is 1.

The 1st largest value in given BST is 4.

Input : root = [5, 3, 6, 2, null, null, null, 1] , k = 3

Output : [3, 3]

Explanation :

The 3rd smallest value in given BST is 3.

The 3rd largest value in given BST is 3.

Input : root = [3,1,4,null,2] , k = 2

Output:
[1, 2]
[2, 3]
[3, 4]
[1, 3]

Submit
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 105

#Brute
Intuition
To find the Kth smallest and largest elements in a Binary Search Tree (BST) using a brute force method, a simple approach is to traverse the tree and collect all its node values in a list. or a vector. By sorting this list, the desired elements can be easily retrieved based on their indices. To find the Kth smallest element, access the element at index ‘k - 1’ in the array, and to find the Kth largest element, access the element at index ‘array.length - K’ index. Note that it is preferred to consider the inorder traversal of the BST because it will come out to be sorted already.

Approach
Begin by creating a list or vector to serve as a storage container for the values of the nodes present in the Binary Search Tree (BST).
Perform an inorder traversal of the BST utilizing the depth-first search (DFS) technique, during which each node's value should be added to the previously initialized array.
To identify the Kth smallest element, retrieve the element located at the index 'k - 1' of the sorted array, keeping in mind that array indexing begins at zero.
To determine the Kth largest element, retrieve the element positioned at the index 'array.length - k' within the sorted array.
Finally, return a pair of elements: the Kth smallest and the Kth largest, as determined by the aforementioned steps.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def kLargesSmall(self, root, k):
        # Helper function to perform an in-order traversal of the BST
        def inorder_traversal(node, values):
            if node:
                inorder_traversal(node.left, values)
                values.append(node.data)
                inorder_traversal(node.right, values)
        
        # List to store the node values
        values = []
        # Perform in-order traversal and collect values
        inorder_traversal(root, values)
        
        # Find the kth smallest and kth largest values
        kth_smallest = values[k - 1]
        kth_largest = values[-k]
        
        return [kth_smallest, kth_largest]

# Example usage:
# Constructing the tree: [3,1,4,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

solution = Solution()
k = 1
print(solution.kLargesSmall(root, k))  # Output: [1, 4]

Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the BST
Because the code performs an in-order traversal of the BST, which requires O(N) time.
Space Complexity: O(N), since the code stores all the node values in a list.

#Optimal
Intuition
When aiming to identify the Kth smallest and largest elements within a Binary Search Tree (BST), one strategy strategy involves leveraging the inorder traversal technique. This method, which adheres to the Left Node Right sequence, inherently orders the tree's elements in ascending order. The unique structure of a BST, where the left child node holds a value smaller than its parent node and the right child node holds a value greater than the parent, guarantees that an inorder traversal will produce a sorted sequence. This characteristic significantly helps the task of extracting the Kth smallest and largest elements, making the process both efficient and straightforward.

Methodology
Begin by initializing an array that will be used to store the values of the nodes within the BST.
Execute an inorder traversal of the BST, during which each node's value is sequentially added to the array.
Utilize a counter to monitor the progress of the traversal, particularly focusing on the Kth position, thereby eliminating the necessity for an additional data structure.
To determine the Kth smallest element, observe the counter, and upon reaching the value of K, record the current node's value as the Kth smallest.
For identifying the Kth largest element, conduct a reverse inorder traversal, starting from the root node. As each node is visited, increment a counter to track the number of visited nodes. The traversal should follow the order: right subtree first, then the current node, and finally the left subtree.
Ultimately, return the values corresponding to the Kth smallest and Kth largest elements as derived from the aforementioned steps.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to find the kth smallest element
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    # Helper function for inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.data
                return
            self.inorder(node.right)

    # Function to find the kth largest element
    def kthLargest(self, root, k):
        self.k = k
        self.result = None
        self.reverse_inorder(root)
        return self.result

    # Helper function for reverse inorder traversal
    def reverse_inorder(self, node):
        if node is not None:
            self.reverse_inorder(node.right)
            self.k -= 1
            if self.k == 0:
                self.result = node.data
                return
            self.reverse_inorder(node.left)

    # Function to return kth smallest and kth largest elements
    def kLargesSmall(self, root, k):
        return [self.kthSmallest(root, k), self.kthLargest(root, k)]

# Example usage
if __name__ == "__main__":
    # Constructing the tree: [3, 1, 4, None, 2]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    
    solution = Solution()
    k = 1
    result = solution.kLargesSmall(root, k)
    
    print(result)  # Output: [1, 4]

Complexity Analysis
Time Complexity O(N), where N is the number of nodes in the binary tree. The reason is that in the worst-case scenario, the inorder and reverse inorder traversals visit each node exactly once.

Space Complexity O(H), where H is the height of the binary tree.


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    # Helper function for inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.data
                return
            self.inorder(node.right)

    # Function to find the kth largest element
    def kthLargest(self, root, k):
        self.k = k
        self.result = None
        self.reverse_inorder(root)
        return self.result

    # Helper function for reverse inorder traversal
    def reverse_inorder(self, node):
        if node is not None:
            self.reverse_inorder(node.right)
            self.k -= 1
            if self.k == 0:
                self.result = node.data
                return
            self.reverse_inorder(node.left)
    def kLargesSmall(self, root, k):
         return [self.kthSmallest(root, k), self.kthLargest(root, k)]
