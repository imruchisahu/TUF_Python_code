'''
Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.



A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.

A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.



Since there can be multiple answers, the compiler will return true if it's correct, else false.


Examples:
Input: nums = [10, 20, 30, 21, 23]

Output: [30, 21, 23, 10, 20]

Explanation:

Input: nums = [-5, -4, -3, -2, -1]

Output: [-1, -2, -3, -4, -5]

Explanation:

Input: nums = [2, 6, 3, 100, 120, 4, 5]

Output:
[120, 100, 5, 3, 4, 2, 6]
[100, 120, 6, 3, 4, 2, 5]
[120, 100, 6, 3, 2, 2, 5]
[120, 100, 6, 3, 4, 2, 5]

Submit
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums represents a min-heap

Intution:
This problem is similar to building heap from a given array. The fact that the given array is a min-heap array can be overlooked, boiling down the problem to building a Max-heap array from the given array.

Approach:
Start from the last non-leaf node in the array, as leaf nodes are already min-heaps.
Perform a downward heapify operation on each node, ensuring the max-heap property (the parent must be larger than its children) is maintained.
The heapify operation compares the current node with its children, swaps it with the larger child if necessary, and recursively heapifies the affected subtree.
Once the iterations are over, the given array is converted into a max-heap.
Solution:
class Solution:
    # Function to recursively heapify the array downwards
    def _heapifyDown(self, arr, ind):
        n = len(arr)  # Size of the array

        # To store the index of largest element
        largestInd = ind

        # Indices of the left and right children
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2
        
        # If the left child holds larger value, update the largest index
        if leftChildInd < n and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd

        # If the right child holds larger value, update the largest index
        if rightChildInd < n and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd

        # If the largest element index is updated
        if largestInd != ind:
            # Swap the largest element with the current index
            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]

            # Recursively heapify the lower subtree
            self._heapifyDown(arr, largestInd)
        return

    def minToMaxHeap(self, nums):
        n = len(nums)
        
        # Iterate backwards on the non-leaf nodes
        for i in range(n//2 - 1, -1, -1):
            # Heapify each node downwards
            self._heapifyDown(nums, i)
        
        return nums

def main():
    nums = [10, 20, 30, 21, 23]
    
    print("Initial Min-heap Array: ", end="")
    for x in nums:
        print(x, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to convert the given array from min-heap to max-heap
    nums = sol.minToMaxHeap(nums)

    print("\nMax-heap converted Array: ", end="")
    for x in nums:
        print(x, end=" ")

if __name__ == "__main__":
    main()

Complexity Analysis:
Time Complexity: O(N) (where N is the number of elements in the array)
Each heapify call has a time complexity of O(h), where h is the height of the subtree, h = log(N). The heapify operation is performed for approximately N/2 non-leaf nodes.

Due the variable height for all the subtrees, summing the total work done for all the nodes results in an overall time complexity of O(N) for building a heap.

Space Complexity: O(logN)
The recursive calls during heapify require stack space proportional to the height of the heap which will be of the order of log(N) in the worst-case.

'''
class Solution:
    def _heapifyDown(self, arr, ind):
        n = len(arr)  
        largestInd = ind
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2

        if leftChildInd < n and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd

        if rightChildInd < n and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd

        if largestInd != ind:

            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]
            self._heapifyDown(arr, largestInd)
        return

    def minToMaxHeap(self, nums):
        n = len(nums)
        
        # Iterate backwards on the non-leaf nodes
        for i in range(n//2 - 1, -1, -1):
            self._heapifyDown(nums, i)
        
        return nums
