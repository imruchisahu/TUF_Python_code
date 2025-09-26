'''
Given an array nums representing a min-heap and two integers ind and val, set the value at index ind (0-based) to val and perform the heapify algorithm such that the resulting array follows the min-heap property.

Modify the original array in-place, no need to return anything.


Examples:
Input: nums = [1, 4, 5, 5, 7, 6], ind = 5, val = 2

Output: [1, 4, 2, 5, 7, 5]

Explanation: After setting index 5 to 2, the resulting heap in array form = [1, 4, 5, 5, 7, 2]

Parent of nums[5] = nums[2] = 5 > nums[5] = 2, so they are swapped.

Final array = [1, 4, 2, 5, 7, 5]

Input: nums = [2, 4, 3, 6, 5, 7, 8, 7], ind = 0, val = 7

Output: [3, 4, 7, 6, 5, 7, 8, 7]

Explanation: After setting index 0 to 7, the resulting heap in array form =[7, 4, 3, 6, 5, 7, 8, 7]

The parent of nums[2] = nums[0] = 7 > nums[2] = 3, so they are swapped. No further swaps are needed.

Final array = [3, 4, 7, 6, 5, 7, 8, 7]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
0 <= ind < nums.length
-104 <= val <= 104
nums represents a min-heap


Intuition:
When a value is updated at a particular index, the array following the min-heap property consistently gets distorted. To make the array consistent again, the heapify algorithm is used.

When a particular index value is updated, there can be two cases:

Updated value is greater than the initial value: For a min-heap array, this updated value must actually belong to its bottom subtree. Hence, the array is heapified downwards.
Updated value is smaller than the initial value: For a min-heap array, this updated value must actually belong to the upper levels of the tree. Hence, the array is heapified upwards.

While heapifying upwards or downwards, the value of the nodes are updated such that the value of parent node is always lesser than the values of its children nodes.
Approach:
The value at the specified index is updated to the given value.
If the new value is smaller than the original, the array is heapfied upwards, otherwise the array is heapified downwards.
Heapify-Up:
Starting from the updated index, the value is compared with its parent.
If the parent is larger, the values are swapped.
This process continues recursively until the min-heap property is restored.
Heapify-Down:
Starting from the updated index, the value is compared with its children.
If either child is smaller, the smallest child is swapped with the current value.
The process continues recursively until the min-heap property is restored.
Once the recursive call ends, the min-heap array is restored.

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

    # Function to recursively heapify the array upwards
    def heapifyUp(self, arr, ind):
        parent_Ind = (ind - 1)//2

        # If current index holds smaller value than the parent
        if ind > 0 and arr[ind] < arr[parent_Ind]:
            # Swap the values at the two indices
            arr[ind], arr[parent_Ind] = arr[parent_Ind], arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(arr, parent_Ind)

        return

    # Function to implement the heapify algorithm for a min-heap
    def heapify(self, nums, ind, val):
        # If the current value is replaced with a smaller value
        if nums[ind] > val:
            nums[ind] = val
            self.heapifyUp(nums, ind)
        # Else if the current value is replaced with a larger value
        else:
            nums[ind] = val
            self.heapifyDown(nums, ind)

        return

# Driver code
def main():
    nums = [1, 4, 5, 5, 7, 6]
    ind = 5
    val = 2

    # Input array
    print("Input array:", end=" ")
    for it in nums:
        print(it, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to heapify the array
    sol.heapify(nums, ind, val)

    # Output array
    print("\nModified array after heapifying:", end=" ")
    for it in nums:
        print(it, end=" ")

if __name__ == "__main__":
    main()

Complexity Analysis:
Time Complexity: O(log2N) (where N is the number of elements of the array)
The heapify function calls either heapifyUp or heapifyDown, both of which in the worst case will make number of recursive calls equal to the height of the heap which is log2N.

Space Complexity: O(log2N)
The recursive stack space will contribute to log2N in the worst-case. There is no extra space used other than this as the array is modified in-place.
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

    # Function to recursively heapify the array upwards
    def heapifyUp(self, arr, ind):
        parent_Ind = (ind - 1)//2
        if ind > 0 and arr[ind] < arr[parent_Ind]:
            arr[ind], arr[parent_Ind] = arr[parent_Ind], arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(arr, parent_Ind)

        return

    # Function to implement the heapify algorithm for a min-heap
    def heapify(self, nums, ind, val):
        if nums[ind] > val:
            nums[ind] = val
            self.heapifyUp(nums, ind)
        else:
            nums[ind] = val
            self.heapifyDown(nums, ind)

        return
    