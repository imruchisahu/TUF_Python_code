'''
You need to implement the Min Heap with the following given methods.

insert (x) -> insert value x to the min heap
getMin -> Output the minimum value from min heap
exctractMin -> Remove the minimum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
initializeHeap -> Initialize the heap

Examples:
Input : operation = [ "initializeheap", "insert", "insert", "insert", "getMin", "heapSize", "isEmpty", "extractMin", "changeKey" , "getMin" ]

nums = [ [4], [1], [10], [0, 16] ]

Output : [ null, null, null, null, 1, 3, 0, null, null, 10 ]

Explanation : In 1st operation we initialize the heap to empty heap.

In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [1, 4, 10].

In 5th operation we output the minimum element from the heap i.e. 1.

In 6th operation we output the size of the current heap i.e. 3.

In 7th operation we output whether the heap is empty or not i.e. false (0).

In 8th operation we remove the minimum element from heap. So the ne heap becomes -> [4, 10].

In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 10]. After heapify -> [10, 16].

In 10th operation we output the minimum element of the heap i.e. 10.

Input : operation = [ "initializeheap", "insert", "insert", "extractMin", "getMin", "insert", "heapSize", "isEmpty", "extractMin", "changeKey" , "getMin" ]

nums = [ [4], [1], [1], [0, 2] ]

Output : [ null, null, null, null, 4, null, 2, 0, null, null, 2 ]

Explanation : In 1st operation we initialize the heap to empty heap.

In 2nd, 3rd operation we insert 4, 1 to the heap respectively. The heap after 4th operation will be -> [1, 4].

In 4th operation we remove the minimum element from heap. So the ne heap becomes -> [4].

In 5th operation we output the minimum element of the heap i.e. 4.

In 6th operation we operation we insert 1 to the heap. The heap after 6th operation will be -> [1, 4].

In 7th operation we output the size of the current heap i.e. 2.

In 8th operation we output whether the heap is empty or not i.e. false (0).

In 9th operation we remove the minimum element from heap. So the ne heap becomes -> [4].

In 10th operation we change the 0th index element to 2. So new heap becomes -> [2].

In 11th operation we output the minimum element of the heap i.e. 2.

Constraints:
1 <= n <= 105
-105 <= nums[i] <= 105

Approach:
The goal is to implement a minimum heap data structure that will provide different operations to the user. The idea to use a list/array to store the elements in an order that follows the min-heap property. An array stores a complete binary tree without using extra pointers for child links. It allows calculating parent and child positions with simple index arithmetic and keeps all elements close together for faster memory access, making it both space-efficient and quick to update or reorder elements. Here's how different function can be implemented:
1. Insert(val):
The element can be added at the back of the list. Since, this element may not follow the min-heap property, it can be heapified upwards.
2. Get Minimum():
The minimum value will always be stored at the 0th index as the array follows the min-heap property.
3. Extract Minimum():
If the smallest value (located at 0th index) is removed directly, all the elements in the array will need to be shifted by one index ahead making it a costly operation. Instead, the smallest value can be swapped with the element at last index. The value at the last index (currently storing the smallest value) can be popped out from the back of the array/list.

Since, the element at the 0th index does not follow the min-heap property (because it was swapped), we must heapify it downwards.
4. Heap Size():
The size of the array/list can be returned directly as the heap size.
5. Is Empty():
If the size of the array is zero, the heap can be marked as empty.
6. Change Key(ind, val):
The value at particular index can be easily updated in the list. This updated value might disturb the min-heap property of the array, so it needs to be heapified upwards or downwards accordingly.
class Solution:
    def __init__(self):
        self.arr = []  # list to store the min-heap
        self.count = 0  # to store the count of elements in min-heap

    # Function to recursively heapify the array upwards
    def heapifyUp(self, arr, ind):
        parentInd = (ind - 1)//2 

        # If current index holds smaller value than the parent
        if ind > 0 and arr[ind] < arr[parentInd]:
            # Swap the values at the two indices
            arr[ind], arr[parentInd] = arr[parentInd], arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(arr, parentInd)

        return

    # Function to recursively heapify the array downwards
    def heapifyDown(self, arr, ind):
        n = len(arr)  # Size of the array

        # To store the index of smallest element
        smallestInd = ind 

        # Indices of the left and right children
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2

        # If the left child holds smaller value, update the smallest index
        if leftChildInd < n and arr[leftChildInd] < arr[smallestInd]:
            smallestInd = leftChildInd

        # If the right child holds smaller value, update the smallest index
        if rightChildInd < n and arr[rightChildInd] < arr[smallestInd]:
            smallestInd = rightChildInd

        # If the smallest element index is updated
        if smallestInd != ind:
            # Swap the largest element with the current index
            arr[smallestInd], arr[ind] = arr[ind], arr[smallestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, smallestInd)

        return

    # Method to intialize the min-heap data structure
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    # Method to insert a given value in the min-heap
    def insert(self, key):
        # Insert the value at the back of the list
        self.arr.append(key)

        # Heapify upwards
        self.heapifyUp(self.arr, self.count)
        self.count += 1  # Increment the counter

        return

    # Method to change the value at a given index in min-heap
    def changeKey(self, index, new_val):
        # If the current value is replaced with a smaller value
        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapifyUp(self.arr, index)
        # Else if the current value is replaced with a larger value
        else:
            self.arr[index] = new_val
            self.heapifyDown(self.arr, index)

        return

    # Method to extract the minimum value from the min-heap
    def extractMin(self):
        ele = self.arr[0]  # minimum value in the heap

        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]

        # Pop the minimum value from the list
        self.arr.pop()
        self.count -= 1  # Decrement the counter

        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(self.arr, 0)

    # Method to return if the min-heap is empty
    def isEmpty(self):
        return (self.count == 0)

    # Method to return the minimum value in the min-heap
    def getMin(self):
        # Returning the value stored at the root
        return self.arr[0]

    # Method to return the size of min-heap
    def heapSize(self):
        return self.count


# Driver code
def main():
    # Creating an object of the Solution class
    heap = Solution()

    # Initializing a min heap data structure
    heap.initializeHeap()

    # Performing different operations
    heap.insert(4); print("Inserting 4 in the min-heap")
    heap.insert(5); print("Inserting 5 in the min-heap")
    heap.insert(10); print("Inserting 10 in the min-heap")
    print("Minimum value in the min-heap is:", heap.getMin())
    print("Size of min-heap is:", heap.heapSize())
    print("Is heap empty:", heap.isEmpty())
    print("Extracting minimum value from the heap")
    heap.extractMin()
    print("Changing value at index 0 to 10")
    heap.changeKey(0, 10)
    print("Minimum value in the min-heap is:", heap.getMin())


if __name__ == "__main__":
    main()
    
Complexity Analysis:
Considering there are maximum N elements inserted in the heap data structure,

Time Complexity:
Insert(val): Inserting and Heapifying upwards contribute to O(logN) time.
Get Minimum(): Constant time operation, i.e., O(1).
Extract Minimum(): Involves Heapifying downwards contributing to O(logN) time.
Heap Size(): Constant time operation, i.e., O(1).
Is Empty(): Constant time operation, i.e., O(1).
Change Key(ind, val): Involves heapifying which takes O(logN) time.

Space Complexity: O(N), because of the array used to store the elements.
'''
class Solution:
    def __init__(self):
        self.arr = []  # list to store the min-heap
        self.count = 0  # to store the count of elements in min-heap

    # Function to recursively heapify the array upwards
    def heapifyUp(self, arr, ind):
        parentInd = (ind - 1)//2 

        # If current index holds smaller value than the parent
        if ind > 0 and arr[ind] < arr[parentInd]:
            # Swap the values at the two indices
            arr[ind], arr[parentInd] = arr[parentInd], arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(arr, parentInd)

        return

    def heapifyDown(self, arr, ind):
        n = len(arr)  # Size of the array

        # To store the index of smallest element
        smallestInd = ind 

        # Indices of the left and right children
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2

        # If the left child holds smaller value, update the smallest index
        if leftChildInd < n and arr[leftChildInd] < arr[smallestInd]:
            smallestInd = leftChildInd

        # If the right child holds smaller value, update the smallest index
        if rightChildInd < n and arr[rightChildInd] < arr[smallestInd]:
            smallestInd = rightChildInd

        # If the smallest element index is updated
        if smallestInd != ind:
            # Swap the largest element with the current index
            arr[smallestInd], arr[ind] = arr[ind], arr[smallestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, smallestInd)

        return


    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    def insert(self, key):
        self.arr.append(key)

        # Heapify upwards
        self.heapifyUp(self.arr, self.count)
        self.count += 1  # Increment the counter

        return

    def changeKey(self, index, new_val):
        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapifyUp(self.arr, index)
        # Else if the current value is replaced with a larger value
        else:
            self.arr[index] = new_val
            self.heapifyDown(self.arr, index)

        return

    def extractMin(self):
        ele = self.arr[0]  # minimum value in the heap

        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]

        # Pop the minimum value from the list
        self.arr.pop()
        self.count -= 1  # Decrement the counter

        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(self.arr, 0)

    def isEmpty(self):
        return (self.count == 0)

    def getMin(self):
        return self.arr[0]

    def heapSize(self):
        return self.count