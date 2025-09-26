'''
Given an array of integers nums, convert it in-place into a min-heap.



A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.


Examples:
Input: nums = [6, 5, 2, 7, 1, 7]

Output: [1, 5, 2, 7, 6, 7]

Explanation: nums[0] <= nums[1], nums[2]

nums[1] <= nums[3], nums[4]

nums[2] <= nums[5]

Input: nums = [2, 3, 4, 1, 7, 3, 9, 4, 6]

Output: [1, 2, 3, 3, 7, 4, 9, 4, 6]

Explanation: nums[0] <= nums[1], nums[2]

nums[1] <= nums[3], nums[4]

nums[2] <= nums[5], nums[6]

nums[3] <= nums[7], nums[8]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Intuition:
To build a min-heap from the given array, the goal must be to individually heapify each non-leaf node so that it starts following the min-heap property. Once, all the non-leaf nodes are heapified, the resultant array will be a min-heap.
Heapify down is preferred in this case because the property violations occur between a node and its children when building a heap from an unsorted array. Fixing the violations downwards ensures that the entire subtree rooted at the node satisfies the min-heap property efficiently.

Note that the leaf nodes don't have any children, i.e., they already follow the min-heap property. Thus, the heapifying down process is performed only for the non-leaf nodes.
Approach:
Start from the last non-leaf node in the array, as leaf nodes are already min-heaps.
Perform a downward heapify operation on each node, ensuring the heap property (the parent is smaller than its children) is maintained.
The heapify operation compares the current node with its children, swaps it with the smallest child if necessary, and recursively heapifies the affected subtree.
Once the iterations are over, the array represents a min-heap.

class Solution:
    # Function to recursively heapify the array downwards
    def heapifyDown(self, arr, ind):
        n = len(arr) # Size of the array

        # Index of smallest element
        smallest_Ind = ind

        # Indices of the left and right children
        leftChild_Ind = 2*ind + 1
        rightChild_Ind = 2*ind + 2
        
        # If the left child holds smaller value, update the smallest index
        if leftChild_Ind < n and arr[leftChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = leftChild_Ind

        # If the right child holds smaller value, update the smallest index
        if rightChild_Ind < n and arr[rightChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = rightChild_Ind

        # If the smallest element index is updated
        if smallest_Ind != ind:
            # Swap the smallest element with the current index
            arr[smallest_Ind], arr[ind] = arr[ind], arr[smallest_Ind]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, smallest_Ind)

        return

    # Function to convert given array into a min-heap
    def buildMinHeap(self, nums):
        n = len(nums)

        # Iterate backwards on the non-leaf nodes
        for i in range(n // 2 - 1, -1, -1):
            # Heapify each node downwards
            self.heapifyDown(nums, i)


# Driver code
if __name__ == "__main__":
    nums = [6, 5, 2, 7, 1, 7]

    # Input array
    print("Input array:", nums)

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to convert the given array into a min-heap
    sol.buildMinHeap(nums)

    # Output array
    print("Min-heap array:", nums)
    
Complexity Analysis:
Time Complexity: O(N) (where N is the number of elements in the array)
Each heapify call has a time complexity of O(h), where h is the height of the subtree, h = log(N). The heapify operation is performed for approximately N/2 non-leaf nodes.
Due to the variable height for all the subtrees, summing the total work done for all the nodes results in an overall time complexity of O(N) for building a heap.

Space Complexity: O(log2N)
The recursive calls during heapify require stack space proportional to the height of the heap, which will be of the order of log(N) in the worst case.

'''
class Solution:
 
    def heapifyDown(self, arr, ind):
        n = len(arr) 
        smallest_Ind = ind

        leftChild_Ind = 2*ind + 1
        rightChild_Ind = 2*ind + 2
        
        if leftChild_Ind < n and arr[leftChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = leftChild_Ind

        if rightChild_Ind < n and arr[rightChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = rightChild_Ind

        if smallest_Ind != ind:
            arr[smallest_Ind], arr[ind] = arr[ind], arr[smallest_Ind]
            self.heapifyDown(arr, smallest_Ind)

        return

    def buildMinHeap(self, nums):
        n = len(nums)

        # Iterate backwards on the non-leaf nodes
        for i in range(n // 2 - 1, -1, -1):
            # Heapify each node downwards
            self.heapifyDown(nums, i)


