'''
Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.



A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.


Examples:
Input: nums = [10, 20, 30, 21, 23]

Output: true

Explanation: Each node has a lower or equal value than its children.

Input: nums = [10, 20, 30, 25, 15]

Output: false

Explanation: The node with value 20 has a child with value 15, thus it is not a min-heap.

Input: nums = [1, 2, 1, 3]

Output:
true
false

Submit
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
The array represents a complete binary tree.


Intution:
To check if the given array represents a min-heap, all the nodes must follow the min-heap property.

Min-Heap Property: Each node value must be smaller than the value of its immediate left and right children node.

Since the leaf-nodes have no children, directly checking the min-heap property for the non-leaf nodes will be enough to check if the array represents a min heap.

Approach:
Iterate over the non-leaf nodes as the leaf-nodes follow the min-heap property by-default.
For each non-leaf node, check if its left child or the right child (if they exist) has a smaller value than the parent node.
If a child node is found having smaller value than the parent, then the parent node violates the min-heap property and the function can return the false.
If all the node satisfy the min-heap property, the function returns true.
Solution:
class Solution:
    
    # Function to check if the given array is a min-heap
    def isHeap(self, nums):
        n = len(nums)  # Size of the array
        
        # Iterate on the non-leaf nodes from the back
        for i in range(n//2 - 1, -1, -1):
            leftChildInd = 2*i + 1
            rightChildInd = 2*i + 2
            
            # If left child has a smaller value than the parent
            if leftChildInd < n and nums[leftChildInd] < nums[i]:
                return False
                
            # If right child has a smaller value than parent
            if rightChildInd < n and nums[rightChildInd] < nums[i]:
                return False
        
        return True

def main():
    nums = [10, 20, 30, 21, 23]
    
    print("Given Array: ", end="")
    for x in nums:
        print(x, end=" ")
    
    # Creating an object of the Solution class
    sol = Solution()

    # Function call to check if the given array is a min-heap
    ans = sol.isHeap(nums)

    if ans:
        print("\nThe given array is a min-heap.")
    else:
        print("\nThe given array is not a min-heap.")

if __name__ == "__main__":
    main()

Complexity Analysis:
Time Complexity: O(N) (where N represents the number of elements in the array)
Iterating on all the non-leaf nodes will take N/2 iterations which is of the order of O(N) (Constant factors like 1/2 are ignored while following the Big-O notation).

Space Complexity: O(1), as there is no extra space used.
'''
class Solution:
    def isHeap(self, nums):
        n = len(nums)  # Size of the array
        
        # Iterate on the non-leaf nodes from the back
        for i in range(n//2 - 1, -1, -1):
            leftChildInd = 2*i + 1
            rightChildInd = 2*i + 2
            
            # If left child has a smaller value than the parent
            if leftChildInd < n and nums[leftChildInd] < nums[i]:
                return False
                
            # If right child has a smaller value than parent
            if rightChildInd < n and nums[rightChildInd] < nums[i]:
                return False
        
        return True
    