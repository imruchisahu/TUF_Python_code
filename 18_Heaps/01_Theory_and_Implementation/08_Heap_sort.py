'''
Given an array of integers nums, sort the array in non-decreasing order using the heap sort algorithm. Sort the given array itself, there is no need to return anything.



A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.


Examples:
Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation:1 <= 3 <= 4 <= 5 <= 7.

One possible way to get the sorted array using heapSort :

[7, 4, 1, 5, 3] -> [3, 4, 1, 5, 7]

-> [5, 4, 1, 3, 7] -> [3, 4, 1, 5, 7]

-> [4, 3, 1, 5, 7] -> [1, 3, 4, 5, 7]

-> [3, 1, 4, 5, 7] -> [1, 3, 4, 5, 7]

-> [1, 3, 4, 5, 7] -> [1, 3, 4, 5, 7]

Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order.

Input: nums = [6, 2, 3, 1, 5]

Output:
[1, 2, 3, 6, 5]
[1, 2, 3, 5, 6]
[1, 2, 3, 4, 5]
[6, 5, 3, 2, 1]

Submit
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.

Intuition:
The aim is to sort an array in ascending order. A straightforward method is to repeatedly pick out the largest element from the unsorted part of the array and place it at the end. Once the largest element is in its correct spot, the algorithm only needs to focus on the remaining (now smaller) unsorted portion.

To efficiently get the largest element in constant time, the array can be organized into a Max Heap. A Max Heap is a special kind of binary tree where every parent node is greater than or equal to its children. In array form, the biggest element always ends up at index 0 (the root of the heap).

Why a Max-heap?
With a Max Heap, the largest element is immediately available at index 0 without extra searching. This makes it easy to place the largest element at the end of the array. If the goal is to sort the array in descending order, the minimum element must be picked every time, which requires building a Min Heap instead.
Approach:
Rearrange the elements of the array and build a max-heap.
Start iterating with the whole array being unsorted initially.
Swap the element at index 0 (the largest) with the element at the last position in the unsorted portion of the array. The largest element is now at the end, in its correct sorted position.
Reduce the size of unsorted portion of the array by one from the back (since the very last element is now sorted).
Re-heapify from the top (index 0) downwards to restore the Max Heap property for the remaining unsorted portion (the sorted portion of the array must be kept undisturbed).
Solution:
# Function to recursively heapify the array downwards
class Solution:
    def heapifyDown(self, arr, last, ind):
        # Index of largest element
        largestInd = ind

        # Indices of the left and right children
        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2
        
        # If the left child holds larger value, update the largest index
        if leftChildInd <= last and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd

        # If the right child holds larger value, update the largest index
        if rightChildInd <= last and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd

        # If the largest element index is updated
        if largestInd != ind:
            # Swap the largest element with the current index
            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, last, largestInd)
        return

    # Function to build Max-heap from the given array
    def buildMaxHeap(self, nums):
        n = len(nums)
        
        # Iterate backwards on the non-leaf nodes
        for i in range(n // 2 - 1, -1, -1):
            # Heapify each node downwards
            self.heapifyDown(nums, n - 1, i)
        return

    # Function to sort the array using heap-sort
    def heapSort(self, nums):
        # Function call to build a max-heap from the given array
        self.buildMaxHeap(nums)
        
        # To store the last Index
        last = len(nums) - 1
        
        # Until there are elements left to sort in the array
        while last > 0:
            # Swap the greatest element to the current last index
            nums[0], nums[last] = nums[last], nums[0]
            last -= 1  # Decrement the last index
            
            if last > 0:
                # Heapify down the root
                self.heapifyDown(nums, last, 0)
        
        return

# Driver code
if __name__ == "__main__":
    nums = [60, 30, 40, 20, 10, 50]
    
    print("Input Array:", end=" ")
    for x in nums:
        print(x, end=" ")
    
    # Creating an object of Solution class
    sol = Solution()
    
    # Function call to sort the array using heap-sort
    sol.heapSort(nums)
    
    print("\nSorted Array:", end=" ")
    for x in nums:
        print(x, end=" ")

Complexity Analysis:
Time Complexity: O(N*logN), where N is the size of the array
Building a max-heap from the array takes O(N) iterations. Once done, each node is placed at its correct index and the array is heapified (which takes logN iterations) taking overall O(N*logN) time.

Space Complexity: O(logN)
Recursive stack space used while building the max-heap is O(logN). Also, the depth of each heapify Down will take O(logN) space.
Note:
Although heapifyDown() may be invoked multiple times (up to N calls in total), each call finishes before the next one begins. Hence, the recursive calls do not stack on top of each other, ensuring that the maximum stack depth remains O(log N) at any point in time. As a result, the overall auxiliary space complexity (due to recursion) is O(log N).

'''

class Solution:
    def heapifyDown(self, arr, last, ind):
        largestInd = ind

        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2
        
        if leftChildInd <= last and arr[leftChildInd] > arr[largestInd]:
            largestInd = leftChildInd

        if rightChildInd <= last and arr[rightChildInd] > arr[largestInd]:
            largestInd = rightChildInd
        if largestInd != ind:
            arr[largestInd], arr[ind] = arr[ind], arr[largestInd]
            self.heapifyDown(arr, last, largestInd)
        return

    def buildMaxHeap(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapifyDown(nums, n - 1, i)
        return

    def heapSort(self, nums):
        self.buildMaxHeap(nums)
        last = len(nums) - 1
        
        # Until there are elements left to sort in the array
        while last > 0:
            nums[0], nums[last] = nums[last], nums[0]
            last -= 1  
            if last > 0:
                self.heapifyDown(nums, last, 0)
        
        return