'''
Given a root of binary search tree and a key(node) value, find the floor and ceil value for that particular key value.



Floor Value Node: Node with the greatest data lesser than or equal to the key value. 


Ceil Value Node: Node with the smallest data larger than or equal to the key value.


If a particular floor or ceil value is not present then output -1.


Examples:
Input : root = [8, 4, 12, 2, 6, 10, 14] , key = 11

Output : [10, 12]

Explanation :



Input : root = [8, 4, 12, 2, 6, 10, 14] , key = 15

Output : [14, -1]

Explanation :



Input : root = [8, 4, 12, 2, 6, 10, 14] , key = 1

Output:
[2, 4]
[-1, 2]
[-1, 14]
[4, 6]

Submit
Constraints:
1 <= Number of Nodes <= 5000
1 <= Node.val <= 107
1 <= key <= 107

#Floor
Intuition
Finding the floor value in a Binary Search Tree (BST) involves tracking the largest node value that is smaller than or equal to the given key. The thought process here is to either find the exact key or reach nodes close to the key’s value. During traversal, if the key matches the node’s value, this value is assigned as the floor, and the search concludes. If the key is smaller than the current node’s value, the algorithm moves to the left subtree to find a smaller value. If the key is larger, the algorithm updates the floor with the current node’s value and explores the right subtree for potentially larger values.

Approach
Initialize a variable floor to -1 to store the floor value initially.
Traverse the Binary Search Tree starting from the root and continue until reaching the end of the tree or finding the key. At each node:
If the key value equals the node’s value, assign it as the floor value and return.
If the key value is greater than the current node’s value, update floor with the current node’s value and move to the right subtree.
If the key value is smaller than the current node’s value, move to the left subtree as the potential floor value should be smaller.
Return the computed floor value if the key is not found in the tree. This floor value represents the largest node value smaller than the key, or -1 if no such value exists in the BST.
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        # Initialize floor and ceil values to -1, indicating not found
        floor = -1
        ceil = -1

        # Find the floor value

		# Start from the root of the BST
        current = root  
        while current:
			# If the key matches the current node's value
            if current.data == key:  
				# Set floor to this value
                floor = current.data  
                break
            # If the key is greater than the current node's value
            # Update floor to the current node's value
            # If the key is smaller than the current node's value
            # Move to the left subtree to find a smaller value
            elif current.data < key:
                floor = current.data
                current = current.right
            else:
                current = current.left

        # Find the ceil value

		# Reset current to start from the root again
        current = root  
        while current:
			# If the key matches the current node's value
            if current.data == key:  
				# Set ceil to this value
                ceil = current.data  
                break
            # If the key is smaller than the current node's value
            # Update ceil to the current node's value
            # If the key is greater than the current node's value
            # Move to the right subtree to find a larger value
            elif current.data > key:
                ceil = current.data
                current = current.left
            else:
                current = current.right

        # Return floor and ceil values as a list
        return [floor, ceil]

if __name__ == "__main__":
    # Creating a sample BST
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)

    sol = Solution()
    key = 11  # Key to find floor and ceil for

    # Find and print floor and ceil values
    result = sol.floorCeilOfBST(root, key)
    print(f"Floor: {result[0]}, Ceil: {result[1]}")


Complexity Analysis
Time Complexity : O(H) where h is the height of the BST, since we traverse down the tree once for each of the floor and ceil searches

Space Complexity : O(1) as we only use a constant amount of extra space for storing the floor and ceil values.

#Celling
Intuition
The goal of finding the ceil value in a Binary Search Tree (BST) is to keep track of the smallest node value that is greater than or equal to the given key. The thought process involves traversing the tree, continuing until either the tree is fully explored or the key is found. During traversal, if the key matches the node’s value, this value is directly assigned as the ceiling and the search ends. If the key is greater than the current node’s value, the algorithm moves to the right subtree to find a larger value. If the key is smaller, the algorithm updates the ceil value with the current node’s value and explores the left subtree for potentially smaller values.

Approach
Initialize a variable ceil to -1 to store the ceiling value initially.
Traverse the Binary Search Tree starting from the root and continue until reaching the end of the tree or finding the key. At each node:
If the key value matches the node’s value, assign it as the ceiling value and return.
If the key value is greater than the current node’s value, move to the right subtree.
If the key value is smaller than the current node’s value, update ceil with the current node’s value and move to the left subtree.
Return the computed ceil value if the key is not found in the tree. This ceil value represents the smallest node value greater than the key, or -1 if no such value exists in the BST.
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        # Initialize floor and ceil values to -1, indicating not found
        floor = -1
        ceil = -1

        # Find the floor value

		# Start from the root of the BST
        current = root  
        while current:
			# If the key matches the current node's value
            if current.data == key:  
				# Set floor to this value
                floor = current.data  
                break
            # If the key is greater than the current node's value
            # Update floor to the current node's value
            # If the key is smaller than the current node's value
            # Move to the left subtree to find a smaller value
            elif current.data < key:
                floor = current.data
                current = current.right
            else:
                current = current.left

        # Find the ceil value

		# Reset current to start from the root again
        current = root  
        while current:
			# If the key matches the current node's value
            if current.data == key:  
				# Set ceil to this value
                ceil = current.data  
                break
            # If the key is smaller than the current node's value
            # Update ceil to the current node's value
            # If the key is greater than the current node's value
            # Move to the right subtree to find a larger value
            elif current.data > key:
                ceil = current.data
                current = current.left
            else:
                current = current.right

        # Return floor and ceil values as a list
        return [floor, ceil]

if __name__ == "__main__":
    # Creating a sample BST
    root = TreeNode(8)
    root.left = TreeNode(4)
    root.right = TreeNode(12)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(14)

    sol = Solution()
    key = 11  # Key to find floor and ceil for

    # Find and print floor and ceil values
    result = sol.floorCeilOfBST(root, key)
    print(f"Floor: {result[0]}, Ceil: {result[1]}")


Complexity Analysis
Time Complexity : O(H) where h is the height of the BST, since we traverse down the tree once for each of the floor and ceil searches

Space Complexity : O(1) as we only use a constant amount of extra space for storing the floor and ceil values.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        floor = -1
        ceil = -1
        current = root  
        while current:
	
            if current.data == key:  
			
                floor = current.data  
                break
    
            elif current.data < key:
                floor = current.data
                current = current.right
            else:
                current = current.left

        current = root  
        while current:
            if current.data == key:  
                ceil = current.data  
                break
            elif current.data > key:
                ceil = current.data
                current = current.left
            else:
                current = current.right
        return [floor, ceil]