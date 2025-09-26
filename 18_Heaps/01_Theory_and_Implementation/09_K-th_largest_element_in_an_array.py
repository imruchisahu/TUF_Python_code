'''
Given an array nums, return the kth largest element in the array.


Examples:
Input: nums = [1, 2, 3, 4, 5], k = 2

Output: 4

Input: nums = [-5, 4, 1, 2, -3], k = 5

Output: -5

Input: nums = [11, 9, 8, 7, 3, 1], k = 4

Output:
3
7
4
8

Submit
Constraints:
1 <= nums.length <= 105
-1000 <= nums[i] <= 1000
1 <= k <= nums.length


#Brtue/Better
Intuition:
A complete naive approach would be to sort the array and return the kth element from the end. This would take O(N*logN) time due to sorting the array.

The problem is efficiently solved by leveraging the properties of a min-heap. Since only the K largest elements matter, a min-heap of size K is maintained. While processing any element, it is checked if it is among the K largest elements encountered so far. If it is, the smallest element is removed from the min-heap and the new element is inserted.

Algorithm:
A min-heap of size K is maintained to store the K largest elements encountered so far.
The first K elements from the input are inserted into the min-heap.
For each remaining element, if it is greater than the smallest element in the heap, the smallest element is removed, and the new element is inserted.
After processing all elements, the top of the min-heap contains the Kth largest element, which is returned.
Solution:
class Solution:
    # Function to get the Kth largest element 
    def kthLargestElement(self, nums, k):
        
        # Min-heap data structure
        import heapq
        pq = []
        
        # Add the first K elements in the Min-heap
        for i in range(k):
            heapq.heappush(pq, nums[i])
        
        # Process the rest of the elements 
        for i in range(k, len(nums)):
            # Check if a new larger element is found
            if nums[i] > pq[0]:
                heapq.heappop(pq)  # remove the smallest from the min-heap

                # Add the current element to the min-heap
                heapq.heappush(pq, nums[i])
        
        return pq[0]  # Return the kth largest element 

# Driver code
def main():
    nums = [-5, 4, 1, 2, -3]
    k = 5

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to get the Kth largest element 
    ans = sol.kthLargestElement(nums, k)

    # Output array
    print("The Kth largest element in the array is:", ans)

if __name__ == "__main__":
    main()

Complexity Analysis:
Time Complexity: O(N*logK), where N is the size of given input array.
Traversing the array takes O(N) time and for each element, in the worst case, we perform heap operations which take O(logK) time.
Note that K can be equal to N in the worst case, making the worst-case time complexity as O(N*logN).

Space Complexity: O(K), as a Min-heap data structure of size K is used to store the K largest elements.

#Optimal Approach
Intuition:
The earlier approach was taking a worst-case time complexity of O(N*LogN) which is not efficient. This hints to solve the problem in O(N) time complexity. The key idea will be to use the logic in Quick-sort.

In Quick-sort, if the aim is to sort the array in non-increasing order, a pivot element is chosen randomly and the array is partitioned such that all elements greater than the pivot belong to the left portion and all elements smaller than or equal to the pivot belongs to the right portion with the pivot separating the two portions. Refer to the image below for better understanding:


Note that the pivot element will be the Kth largest element when the size of the left portion of the array is K-1. This is because the left portion contains K-1 elements greater than the pivot element.

Thus, if the pivot element is at its correct position, return the element. If the pivot element is smaller than the kth element, search the right side of the pivot. Otherwise, search the left side of the pivot.

Approach:
A random index within the current search range is chosen as the pivot to reduce the risk of worst-case time complexity.
Partition Around the Pivot:
The pivot element is swapped with the leftmost element to simplify the partitioning process.
Elements greater than the pivot are moved to the left portion of the array.
Elements smaller than or equal to the pivot remain in the right portion.
The pivot is then placed in its correct position, ensuring all larger elements are on its left and all smaller ones on its right.
If the pivot index matches k-1, the element at this index is the Kth largest and is returned as the answer.
If the pivot index is greater than k-1, the search continues in the left portion of the array. Otherwise, the search takes place for the right portion of the array.
The process continues until the Kth largest element is found.
Solution:
import random

class Solution:
    # Function to get the Kth largest element
    def kthLargestElement(self, nums, k):
        # Return -1, if the Kth largest element does not exist
        if k > len(nums):
            return -1
        
        # Pointers to mark the part of working array 
        left, right = 0, len(nums) - 1
        
        # Until the Kth largest element is found
        while True:
            # Get the pivot index
            pivotIndex = self.randomIndex(left, right)
            
            # Update the pivotIndex
            pivotIndex = self.partitionAndReturnIndex(nums, pivotIndex, left, right)
            
            # If Kth largest element is found, return
            if pivotIndex == k - 1:
                return nums[pivotIndex]
            
            # Else adjust the end pointers in array 
            elif pivotIndex > k - 1:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
                
    # Function to get a random index 
    def randomIndex(self, left, right):
        # Length of the array 
        length = right - left + 1
        
        # Return a random index from the array 
        return random.randint(left, right)

    # Function to perform the partition and return the updated index of pivot
    def partitionAndReturnIndex(self, nums, pivotIndex, left, right):
        pivot = nums[pivotIndex]  # Get the pivot element
        
        # Swap the pivot with the left element
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        
        ind = left + 1  # Index to mark the start of right portion
        
        # Traverse on the array 
        for i in range(left + 1, right + 1):
            # If the current element is greater than the pivot
            if nums[i] > pivot:
                # Place the current element in the left portion
                nums[ind], nums[i] = nums[i], nums[ind]
                
                # Move the right portion index
                ind += 1
        
        # Place the pivot at the correct index
        nums[left], nums[ind - 1] = nums[ind - 1], nums[left]
        
        return ind - 1  # Return the index of pivot now

# Driver code
def main():
    nums = [-5, 4, 1, 2, -3]
    k = 5

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to get the Kth largest element 
    ans = sol.kthLargestElement(nums, k)

    # Output array
    print("The Kth largest element in the array is:", ans)

if __name__ == "__main__":
    main()

Complexity Analysis:
Time Complexity: O(N), where N is the size of the given array.
In the average case (when the pivot is chosen randomly):
Assuming the array gets divided into two equal parts, with every partitioning step, the search range is reduced by half. Thus, the time complexity is O(N + N/2 + N/4 + ... + 1) = O(N).

In the worst-case scenario (when the element at the left or right index are chosen as pivot):
In such cases, the array is divided into two unequal halves, and the search range is reduced by one element with every partitioning step. Thus, the time complexity is O(N + N-1 + N-2 + ... + 1) = O(N2). However, the probability of this worst-case scenario is negligible.

Space Complexity: O(1), as we are modifying the input array in place and using only a constant amount of extra space.

'''
import random
class Solution:
    def kthLargestElement(self, nums, k):
        if k > len(nums):
            return -1
        left, right = 0, len(nums) - 1
        while True:
            pivotIndex = self.randomIndex(left, right)
            pivotIndex = self.partitionAndReturnIndex(nums, pivotIndex, left, right)
            
            # If Kth largest element is found, return
            if pivotIndex == k - 1:
                return nums[pivotIndex]
        
            elif pivotIndex > k - 1:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
            
    def randomIndex(self, left, right): 
        length = right - left + 1
        return random.randint(left, right)

    # Function to perform the partition and return the updated index of pivot
    def partitionAndReturnIndex(self, nums, pivotIndex, left, right):
        pivot = nums[pivotIndex] 
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        ind = left + 1  
        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                nums[ind], nums[i] = nums[i], nums[ind]      
                # Move the right portion index
                ind += 1
        # Place the pivot at the correct index
        nums[left], nums[ind - 1] = nums[ind - 1], nums[left]
        return ind - 1
    