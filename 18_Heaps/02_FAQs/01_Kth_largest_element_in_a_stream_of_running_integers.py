'''
Implement a class KthLargest to find the kth largest number in a stream. It should have the following methods:

KthLargest(int k, int [] nums) Initializes the object with the integer k and the initial stream of numbers in nums
int add(int val) Appends the integer val to the stream and returns the kth largest element in the stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.


Examples:
Input: [KthLargest(3, [1, 2, 3, 4]), add(5), add(2), add(7)]

Output: [null, 3, 3, 4]

Explanation: initial stream = [1, 2, 3, 4], k = 3.

add(5): stream = [1, 2, 3, 4, 5] -> returns 3

add(2): stream = [1, 2, 2, 3, 4, 5] -> returns 3

add(7): stream = [1, 2, 2, 3, 4, 5, 7] -> returns 4

Input: [KthLargest(2, [5, 5, 5, 5], add(2), add(6), add(60)]

Output: [null, 5, 5, 6]

Explanation: initial stream = [5, 5, 5, 5], k = 2.

add(2): stream = [5, 5, 5, 5, 2] -> returns 5

add(6): stream = [5, 5, 5, 5, 2, 6] -> returns 5

add(60): stream = [5, 5, 5, 5, 2, 6, 60] -> returns 6

Input: [KthLargest(4, [5, 1, 2, 7], add(8), add(2), add(6)]

Output:
[null, 2, 2, 6]
[null, 2, 5, 6]
[null, 2, 2, 5, 7]
[null, 2, 2, 5]

Submit
Constraints:
1 <= Number of instructions <= 1000
-104 <= val & all initial values <= 104
1 <= k <= 104
k - 1 <= nums.length <= 103
The stream will have at least k elements during any add call.


Intuition
A completely naive approach involves adding each new element to a list and sorting the list after every insertion to obtain the kth largest element. Although straightforward, this method incurs a time complexity of O(N logN) and a space complexity of O(N), making it inefficient for large data streams.

An optimized approach stems from a key observation: maintaining only the k largest elements at any given time is sufficient. This significantly reduces the number of elements being processed, leading to improved performance in both time and space.
Understanding
To retrieve the kth largest element from these k largest numbers, it becomes essential to identify the smallest among them. This is due to the fact that the kth largest in the entire stream is the minimum of the top k elements.

A min-heap data structure serves this purpose efficiently. It allows for constant-time access to the smallest element and logarithmic-time insertion and removal, ensuring the heap maintains only the most relevant elements.
Approach
The code maintains a min-heap of size k to keep track of the k largest elements seen so far in the stream.

During initialization, each number from the initial stream is added to the heap.
If the heap size is less than k, the number is pushed directly.
If the heap already has k elements and the current number is larger than the smallest (top of heap), the smallest is removed and the current number is added.
For each new number added to the stream:
If the heap size is less than k, the number is added directly.
If the number is greater than the smallest in the heap, the smallest is removed and the new number is added.
The smallest element in the heap is always the kth largest in the stream and is returned after each addition.

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.K = k  # Integer K
        self.pq = []  # Min-heap

        # Traverse all the elements in the array
        for num in nums:
            # If the size of min-heap is less than k
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)  # Add the current element

            # Else if the top element is smaller than the current element
            elif num > self.pq[0]:
                heapq.heappop(self.pq)  # Pop the top element
                heapq.heappush(self.pq, num)  # Add the current element

    def add(self, val):
        # If the size of the queue is less than K
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

            return self.pq[0]

        # If the smallest element is less than the element to be added
        if val > self.pq[0]:
            heapq.heappop(self.pq)  # Remove the top element
            heapq.heappush(self.pq, val)  # Add the current element

        return self.pq[0]  # Return the Kth largest element

# Driver code
if __name__ == "__main__":
    k = 3
    nums = [1, 2, 3, 4]

    # Creating an object of KthLargest class
    kthLargest = KthLargest(k, nums)

    # Performing different operations
    print("Kth Largest element after adding 5 is:", kthLargest.add(5))
    print("Kth Largest element after adding 2 is:", kthLargest.add(2))
    print("Kth Largest element after adding 7 is:", kthLargest.add(7))

Complexity Analysis:
Time Complexity:
KthLargest(K, nums): O(NlogK), where N is the number of elements in the given list.
For each element, insertion into the min-heap of size at most K takes O(logK) time. Hence, the overall time complexity of this method is O(NlogK)

add(val): O(log K)
If the size of the heap is less than k, inserting the value takes O(log K). If the heap already has k elements and the new value is greater than the smallest (heap top), we remove the top and insert the new value — both operations take O(log K). Therefore, each call to add takes O(log K) time.
Space Complexity: O(K)
This is because a min-heap of size at most K is maintained, which results in O(K) space in the worst case.

'''
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.K = k 
        self.pq = []  
        for num in nums:
            # If the size of min-heap is less than k
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)  # Add the current element

            # Else if the top element is smaller than the current element
            elif num > self.pq[0]:
                heapq.heappop(self.pq)  # Pop the top element
                heapq.heappush(self.pq, num)  # Add the current element


    def add(self, val):
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

            return self.pq[0]

        # If the smallest element is less than the element to be added
        if val > self.pq[0]:
            heapq.heappop(self.pq)  # Remove the top element
            heapq.heappush(self.pq, val)  # Add the current element

        return self.pq[0]  # Return the Kth largest element

