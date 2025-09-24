'''
Given the root of a binary search tree and an integer k.Return true if there exist two elements in the BST such that their sum is equal to k otherwise false.


Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , k = 9

Output : true

Explanation :

The BST contains multiple pair of nodes that sum up to k.

3 + 6 => 9.

5 + 4 => 9.

2 + 7 => 9.

Input : root = [5, 3, 6, 2, 4, null, 7] , k = 14

Output : false

Explanation :

There is no pair in given BST that sum up to k.

Input : root = [5, 3, 6, 2, 4, null, 7] , k = 12

Output:
true
false

Submit
Constraints:
1 <= Number of Nodes <= 104
-104 <= Node.val <= 104
-105 <= k <= 105


#BRute
#Intuition
An inorder traversal of a Binary Search Tree (BST) results in a sorted list of elements. This sorted nature can be utilized to find a pair of elements that add up to a specified sum (K). By applying the Two Sum technique to this sorted list, the solution becomes straightforward. Two pointers are set at the beginning and the end of the list. Their positions are adjusted based on whether their combined value is less than, greater than, or equal to the target sum.

Approach
Execute an inorder traversal of the BST to generate a sorted list of elements. This traversal follows the pattern: left subtree -> root -> right subtree.
With the sorted list in hand, set one pointer at the start (left end) and another at the end (right end) of the list.
Adjust the pointers as follows:
If the sum of the values at the pointers is less than the target, move the left pointer to the right (towards larger values).
If the sum is greater than the target, move the right pointer to the left (towards smaller values).
If the sum equals the target, return the pair of values.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBST(self, root, k):
        # Helper function to perform inorder traversal and get sorted elements
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)
        
        # Get sorted list of elements from BST
        sorted_elements = inorder(root)
        
        # Initialize two pointers
        left, right = 0, len(sorted_elements) - 1
        
        # Use two pointers to find if there is a pair with sum k
        while left < right:
            current_sum = sorted_elements[left] + sorted_elements[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
                
        return False

# Main method to test the solution
if __name__ == "__main__":
    # Example tree: [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    k = 9
    solution = Solution()
    result = solution.twoSumBST(root, k)
    print(result)  # Output: True

Complexity Analysis
Time Complexity: O(N), The time complexity is linear because we are traversing the entire binary search tree once to get the sorted elements, and then we are using two pointers to find the pair that sums to k, which also takes linear time.

Space Complexity: O(N), The space complexity is linear because we are storing the sorted elements in an array, which takes linear space.



#Optimal Approach
Intuition
While a previous method used O(N) space complexity by storing the inorder traversal, this can be avoided by directly utilizing the properties of a Binary Search Tree (BST). Understanding the BST Iterator is crucial for this approach. The BSTIterator class provides functionality to access the next and previous elements in the BST. By initializing pointers 'i' and 'j' to the first and last elements of the inorder traversal using this class, the pointers can be moved through the tree using next() for larger values and before() for smaller values. This method efficiently navigates the BST to find the pair of elements that sum to the target value without needing additional storage for the traversal.

Approach
Initialize pointers 'i' and 'j' to the first and last elements of the BST's inorder traversal using the BSTIterator class.
Use the next() function to move pointer 'i' to larger values and the before() function to move pointer 'j' to smaller values within the BST.
Adjust the pointers based on their sum:
If the sum of the values at the pointers is less than the target, increment pointer 'i' to move towards larger values.
If the sum is greater than the target, decrement pointer 'j' to move towards smaller values.
If the sum equals the target, return true.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# BST Iterator to iterate in the inorder and reverse inorder manner
class BSTIterator:
    def __init__(self, root, is_reverse):
        self.stack = []
        self.reverse = is_reverse
        self.pushAll(root)
    
    # Helper function to push all left or right nodes
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left
    
    # Check if there are more elements in the BST
    def hasNext(self):
        return len(self.stack) > 0
    
    # Get the next element in the inorder or reverse inorder traversal
    def next(self):
        node = self.stack.pop()
        if not self.reverse:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return node.data

class Solution:
    def twoSumBST(self, root, k):
        if not root:
            return False

        # Initialize two iterators
        left_iter = BSTIterator(root, False)  # normal inorder
        right_iter = BSTIterator(root, True)  # reverse inorder

        i = left_iter.next()
        j = right_iter.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = left_iter.next()
            else:
                j = right_iter.next()
        
        return False

def main():
    # Create the tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # Create solution instance
    solution = Solution()
    k = 9
    
    # Check if there exist two elements in the BST such that their sum is equal to k
    result = solution.twoSumBST(root, k)
    print("True" if result else "False")

if __name__ == "__main__":
    main()

Complexity Analysis
Time Complexity: O(N), the code iterates over the BST once to initialize the iterators, and then iterates over the BST again to find the two sum, where N is the number of nodes in the BST.

Space Complexity: O(N), the code uses two iterators, each of which stores at most N nodes in the stack, to iterate over the BST.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root, is_reverse):
        self.stack = []
        self.reverse = is_reverse
        self.pushAll(root)
    
    # Helper function to push all left or right nodes
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left
    
    # Check if there are more elements in the BST
    def hasNext(self):
        return len(self.stack) > 0
    
    # Get the next element in the inorder or reverse inorder traversal
    def next(self):
        node = self.stack.pop()
        if not self.reverse:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return node.data
class Solution:
    def twoSumBST(self, root, k):
        if not root:
            return False
        # Initialize two iterators
        left_iter = BSTIterator(root, False)  # normal inorder
        right_iter = BSTIterator(root, True)  # reverse inorder

        i = left_iter.next()
        j = right_iter.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = left_iter.next()
            else:
                j = right_iter.next()
        
        return False