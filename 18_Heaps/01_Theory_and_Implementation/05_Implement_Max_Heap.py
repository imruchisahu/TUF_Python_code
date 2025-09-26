'''
You need to implement the Max Heap with the following given methods.

insert (x) -> insert value x to the max heap
getMax -> Output the maximum value from the max heap
exctractMax -> Remove the maximum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
initializeHeap -> Initialize the heap

Examples:
Input : operation = [ "initializeHeap", "insert", "insert", "insert", "getMax", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]

nums = [ [4], [1], [10], [0, 16] ]

Output : [ null, null, null, null, 10, 3, 0, null, null, 16 ]

Explanation : In 1st operation we initialize the heap to empty heap.

In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [10, 4, 1].

In 5th operation we output the maximum element from the heap i.e. 10.

In 6th operation we output the size of the current heap i.e. 3.

In 7th operation we output whether the heap is empty or not i.e. false (0).

In 8th operation we remove the maximum element from heap. So the ne heap becomes -> [4, 1].

In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 1]. After heapify -> [16, 1].

In 10th operation we output the maximum element of the heap i.e. 16.

Input : operation = [ "initializeHeap", "insert", "insert", "exctractMax", "getMax", "insert", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]

nums = [ [4], [1], [4], [0, 2] ]

Output : [ null, null, null, null, 1, null, 2, 0, null, null, 2 ]

Explanation : In 1st operation we initialize the heap to empty heap.

In 2nd, 3rd operation we insert 4, 1 to the heap respectively. The heap after 4th operation will be -> [4, 1].

In 4th operation we remove the maximum element from heap. So the ne heap becomes -> [1].

In 5th operation we output the maximum element of the heap i.e. 1.

In 6th operation we operation we insert 4 to the heap. The heap after 6th operation will be -> [4, 1].

In 7th operation we output the size of the current heap i.e. 2.

In 8th operation we output whether the heap is empty or not i.e. false (0).

In 9th operation we remove the maximum element from heap. So the ne heap becomes -> [1].

In 10th operation we change the 0th index element to 2. So new heap becomes -> [2].

In 11th operation we output the maximum element of the heap i.e. 2.

Constraints:
1 <= n <= 105
-105 <= nums[i] <= 105

Approach:
The goal is to implement a maximum heap data structure that will provide different operations to the user. The idea to use a list/array to store the elements in an order that follows the max-heap property. An array stores a complete binary tree without using extra pointers for child links. It allows calculating parent and child positions with simple index arithmetic and keeps all elements close together for faster memory access, making it both space-efficient and quick to update or reorder elements. Here's how different function can be implemented:
1. Insert(val):
The element can be added at the back of the list. Since, this element may not follow the max-heap property, it can be heapified upwards.
2. Get Maximum():
The maximum value will always be stored at the 0th index as the array follows the max-heap property.
3. Extract Maximum():
If the largest value (located at 0th index) is removed directly, all the elements in the array will need to be shifted by one index making it a costly operation. Instead, the largest value can be swapped with the element at last index. The value at the last index (currently storing the largest value) can be popped out from the back of the array/list.

Since, the element at the 0th index does not follow the max-heap property (because it was swapped), it must be heapified downwards.
4. Heap Size():
The size of the array/list can be returned directly as the heap size.
5. Is Empty():
If the array size is zero, the heap can be marked as empty.
6. Change Key(ind, val):
The value at particular index can be easily updated in the list. This updated value might disturb the max-heap property of the array, so it needs to be heapified upwards or downwards accordingly.

class Solution:
    def __init__(self):
        self.arr = []  # list to store the max-heap
        self.count = 0  # to store the count of elements in max-heap

    # Function to recursively heapify the array upwards
    def heapifyUp(self, ind):
        parentInd = (ind - 1)//2

        # If current index holds larger value than the parent
        if ind > 0 and self.arr[ind] > self.arr[parentInd]:
            # Swap the values at the two indices
            self.arr[ind], self.arr[parentInd] = self.arr[parentInd], self.arr[ind]
            
            # Recursively heapify the upper nodes
            self.heapifyUp(parentInd)
        return

    # Function to recursively heapify the array downwards
    def heapifyDown(self, ind):
        n = len(self.arr)  # Size of the array

        # To store the index of largest element
        largestInd = ind

        # Indices of the left and right children
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2
        
        # If the left child holds larger value, update the largest index
        if leftChildInd < n and self.arr[leftChildInd] > self.arr[largestInd]:
            largestInd = leftChildInd

        # If the right child holds larger value, update the largest index
        if rightChildInd < n and self.arr[rightChildInd] > self.arr[largestInd]:
            largestInd = rightChildInd

        # If the largest element index is updated
        if largestInd != ind:
            # Swap the largest element with the current index
            self.arr[largestInd], self.arr[ind] = self.arr[ind], self.arr[largestInd]

            # Recursively heapify the lower subtree
            self.heapifyDown(largestInd)
        return

    # Method to intialize the max-heap data structure
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    # Method to insert a given value in the max-heap
    def insert(self, key):
        # Insert the value at the back of the list
        self.arr.append(key)
        
        # Heapify upwards
        self.heapifyUp(self.count)
        self.count += 1  # Increment the counter
        return

    # Method to change the value at a given index in max-heap
    def changeKey(self, index, new_val):
        # If the current value is replaced with a larger value
        if self.arr[index] < new_val:
            self.arr[index] = new_val
            self.heapifyUp(index)
        # Otherwise (if the current value is replaced with smaller value)
        else:
            self.arr[index] = new_val
            self.heapifyDown(index)
        return

    # Method to extract the maximum value from the max-heap
    def extractMax(self):
        ele = self.arr[0]  # maximum value in the heap

        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]

        # Pop the maximum value from the list
        self.arr.pop()
        self.count -= 1  # Decrement the counter

        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(0)

    # Method to return if the max-heap is empty
    def isEmpty(self):
        return (self.count == 0)

    # Method to return the maximum value in the max-heap
    def getMax(self):
        # Return the value stored at the root
        return self.arr[0]

    # Method to return the size of max-heap
    def heapSize(self):
        return self.count


# Driver code
def main():
    # Creating an object of the Solution class
    heap = Solution()

    # Initializing a max heap data structure
    heap.initializeHeap()
    
    # Performing different operations
    heap.insert(4); print("Inserting 4 in the max-heap")
    heap.insert(1); print("Inserting 1 in the max-heap")
    heap.insert(10); print("Inserting 10 in the max-heap")
    print("Maximum value in the heap is:", heap.getMax())
    print("Size of max-heap is:", heap.heapSize())
    print("Is heap empty:", heap.isEmpty())
    print("Extracting maximum value from the heap")
    heap.extractMax()
    print("Changing value at index 0 to 16")
    heap.changeKey(0, 16)
    print("Maximum value in the heap is:", heap.getMax())

if __name__ == "__main__":
    main()
    
Complexity Analysis:
Considering there are maximum N elements inserted in the heap data structure,

Time Complexity:
Insert(val): Inserting and Heapifying upwards contribute to O(logN) time.
Get Maximum(): Constant time operation, i.e., O(1).
Extract Maximum(): Involves Heapifying downwards contributing to O(logN) time.
Heap Size(): Constant time operation, i.e., O(1).
Is Empty(): Constant time operation, i.e., O(1).
Change Key(ind, val): Involves heapifying which takes O(logN) time.

Space Complexity: O(N), because of the array used to store the elements.
'''
class Solution:
    def __init__(self):
        self.arr = []  # list to store the max-heap
        self.count = 0  # to store the count of elements in max-heap

    # Function to recursively heapify the array upwards
    def heapifyUp(self, ind):
        parentInd = (ind - 1)//2
        if ind > 0 and self.arr[ind] > self.arr[parentInd]:
            self.arr[ind], self.arr[parentInd] = self.arr[parentInd], self.arr[ind]
            self.heapifyUp(parentInd)
        return

    # Function to recursively heapify the array downwards
    def heapifyDown(self, ind):
        n = len(self.arr)  
        largestInd = ind
        leftChildInd = 2*ind + 1
        rightChildInd = 2*ind + 2
        
        if leftChildInd < n and self.arr[leftChildInd] > self.arr[largestInd]:
            largestInd = leftChildInd
        if rightChildInd < n and self.arr[rightChildInd] > self.arr[largestInd]:
            largestInd = rightChildInd
        if largestInd != ind:
            self.arr[largestInd], self.arr[ind] = self.arr[ind], self.arr[largestInd]
            self.heapifyDown(largestInd)
        return

    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.count)
        self.count += 1  
        return

    def changeKey(self, index, new_val):
        if self.arr[index] < new_val:
            self.arr[index] = new_val
            self.heapifyUp(index)
        # Otherwise (if the current value is replaced with smaller value)
        else:
            self.arr[index] = new_val
            self.heapifyDown(index)
        return


    def extractMax(self):
        ele = self.arr[0]  # maximum value in the heap

        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]

        # Pop the maximum value from the list
        self.arr.pop()
        self.count -= 1  # Decrement the counter

        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(0)

    def isEmpty(self):
        return (self.count == 0)
        

    def getMax(self):
        return self.arr[0]

    def heapSize(self):
        return self.count