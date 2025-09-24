'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):



BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.


boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.


int next() Moves the pointer to the right, then returns the number at the pointer.


Notice that by initializing the pointer to a non-existent smallest number, the first call to the next() will return the smallest element in the BST.



Assume that the next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when the next() is called.


Examples:
Input : [ "BSTIterator" , "next" , "next" , "hasNext" , "next" , "hasNext" , "next" , "hasNext" , "next" , "hasNext" ] , root = [7, 3, 15, null, null, 9, 20]

Output : [3, 7, true, 9, true, 15, true, 20, false]

Explanation :

BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);

bSTIterator.next();  // return 3

bSTIterator.next();  // return 7

bSTIterator.hasNext(); // return True

bSTIterator.next();  // return 9

bSTIterator.hasNext(); // return True

bSTIterator.next();  // return 15

bSTIterator.hasNext(); // return True

bSTIterator.next();  // return 20

bSTIterator.hasNext(); // return False

Input : [ "BSTIterator" , "next" , "next" , "next", "hasNext" , "next" , "hasNext" ] , root = [7, 3, 15, null, null, 9, 20]

Output : [3, 7, 9, true, 15, true]

Explanation :

BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);

bSTIterator.next();  // return 3

bSTIterator.next();  // return 7

bSTIterator.next(); // return 9

bSTIterator.hasNext(); // return True

bSTIterator.next();  // return 15

bSTIterator.hasNext(); // return True

Input :  [ "BSTIterator" , "next" , "next" , "next", "next" , "next" , "hasNext" ] , root = [7, 3, 15, null, null, 9, 20]



Output:
[3, 7, 9, 15, 20, true]
[3, 7, 9, 15, 20, false]
[3, 7, 9, 20, 15, false]
[3, 7, 9, 20, 15, true]

Submit
Constraints:
1 <= Number of Nodes <= 104
At most 104 calls will be made to next and hasNext.
0 <= Node.val <= 1054


#Brute
Intuition
When performing an inorder traversal on a Binary Search Tree (BST), the result is a sorted list of node values. By storing these values in an array, it's possible to easily access them in ascending order. The BSTIterator class leverages this idea by maintaining an index to track the current position within the array. This index is initialized to -1, and with each call to next(), the index is incremented to provide the next element in the sorted sequence.

Approach
Execute an inorder traversal of the BST and store the node values in an array. This involves recursively visiting the left subtree, the current node, and then the right subtree.
In the BSTIterator() constructor, initialize an index variable to -1. This variable will keep track of the current position within the array.
Implement the next() function to increment the index by 1 and return the value at the updated index from the inorder traversal array.
Implement the hasNext() function to return true if index + 1 is less than the length of the inorder traversal array; otherwise, return false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root): 
        # Initialize the BSTIterator with the root of the BST.
        # List to store inorder traversal values
        self.values = []  
        # Index to track the current position
        self.index = -1  
        # Perform inorder traversal and store values
        self.inorderTraversal(root)  

    def hasNext(self):
        # Return True if there are more elements in the BST.
        return self.index + 1 < len(self.values)

    def next(self):
        # Return the next element in the BST.
        self.index += 1
        return self.values[self.index]

    def inorderTraversal(self, node):
        # Helper function to perform inorder traversal.
        if node is None:
            return
        self.inorderTraversal(node.left)
        self.values.append(node.data)
        self.inorderTraversal(node.right)

# Main method to demonstrate the usage of BSTIterator
if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    # Instantiate the BSTIterator with the root of the tree
    iterator = BSTIterator(root)

    # Use the iterator to get the elements in sorted order
    while iterator.hasNext():
        print(iterator.next(), end=" ")

    # Output: 3 7 9 15 20

Complexity Analysis
Time Complexity O(N) where n is the number of nodes in the tree for inorder traversal and constant time O(1) for hasNext and next.

SpaceComplexity O(N) due to the storage of values from the inorder traversal in an array


#Optimal
Intuition
While a previous approach used O(N) space complexity, it can be optimized to O(H) space complexity, where H is the height of the tree, by utilizing the properties of a Binary Search Tree (BST). This method creates an iterator that uses a stack to manage the traversal, resulting in efficient O(1) time complexity for the next() and hasNext() operations. By initially traversing to the leftmost node and maintaining a stack of nodes, the BST can be iterated over efficiently.

Approach
Constructor BSTIterator(TreeNode root):
Use a stack (Last In First Out) within the constructor.
Start from the root and traverse to the leftmost node, pushing each encountered node onto the stack.
next() function:
Pop the top element from the stack.
Move to the right subtree of the popped node and traverse down its left subtree, pushing encountered nodes onto the stack.
Return the value of the popped node.
hasNext() function:
Check if the stack is not empty.
If the stack contains elements, return true, indicating there are more nodes to iterate over.
If the stack is empty, return false, indicating there are no more nodes to iterate over.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class BSTIterator:

    def __init__(self, root):
        # Initialize the iterator on the root of the BST      
        self.stack = []
        self._pushAll(root)

    def hasNext(self):
        # Returns true if there is a next element in the iterator     
        return len(self.stack) > 0

    def next(self):
        # Returns the next smallest element in the BST
        temp = self.stack.pop()
        self._pushAll(temp.right)
        return temp.data

    def _pushAll(self, node):
        # Helper function to push all the left nodes onto the stack
        # type node: TreeNode
       
        while node is not None:
            self.stack.append(node)
            node = node.left

# Main method to demonstrate the BSTIterator
if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)
    while iterator.hasNext():
        print(iterator.next(), end=" ")

Complexity Analysis
Time Complexity O(1)as next() and hasNext() occur is constant time, the element pushed onto the stack during traversal to the leftmost node and during subsequent traversals will take O(H) time for each traversal.

Space Complexity : O(H), where H is the height of the tree. This is because, in the worst case, the stack can contain all the nodes from the root to the leftmost leaf node

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._pushAll(root)
    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        temp = self.stack.pop()
        self._pushAll(temp.right)
        return temp.data
    
    def _pushAll(self, node):   
        while node is not None:
            self.stack.append(node)
            node = node.left

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

