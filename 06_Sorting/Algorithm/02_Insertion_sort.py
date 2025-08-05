'''Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.



A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.


Examples:
Input: nums = [7, 4, 1, 5, 3]

Output: [1, 3, 4, 5, 7]

Explanation: 1 <= 3 <= 4 <= 5 <= 7.

Thus the array is sorted in non-decreasing order.

Input: nums = [5, 4, 4, 1, 1]

Output: [1, 1, 4, 4, 5]

Explanation: 1 <= 1 <= 4 <= 4 <= 5.

Thus the array is sorted in non-decreasing order.

Input: nums = [3, 2, 3, 4, 5]

Output:
[2, 3, 3, 4, 5]
Constraints:
1 <= nums.length <= 1000
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.

Similar Problems

Hint 1
Think of the array as divided into a sorted and unsorted portion. Start with the first element as "sorted" and expand this portion by inserting elements from the unsorted part.

Hint 2
Intuition
Insertion sort builds a sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position within the already sorted part of the array.

Approach
In each iteration, select an element from the unsorted part of the array using an outer loop.
Place this element in its correct position within the sorted part of the array.
Use an inner loop to shift the remaining elements as necessary to accommodate the selected element. This involves shifting the elements by one place until the selected element can be placed at its correct position.
Continue this process until the entire array is sorted.
Dry Run


Complexity Analysis  
Time Complexity: O(N2) for the worst and average cases, where N is the size of the array. This is because the outer loop runs N times, and for each pass, the inner loop runs up to N times as well, resulting in approximately N xN operations, hence O(N2). The best-case time complexity occurs when the array is already sorted, in which case the inner loop doesn't run at all, leading to a time complexity of O(N).

Space Complexity: O(1) because Insertion Sort is an in-place sorting algorithm, meaning it sorts the array by modifying the original array without using additional data structures that grow with the size of the input.
class Solution:
    # Function to sort the array using insertion sort
    def insertionSort(self, nums):
        n = len(nums) # Size of the array 
        
        # For every element in the array 
        for i in range(1, n):
            key = nums[i] # Current element as key 
            j = i - 1
            
            # Shift elements that are greater than key by one position
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            
            nums[j + 1] = key # Insert key at correct position
        
        return nums

if __name__ == "__main__":
    # Create an instance of solution class
    solution = Solution()
    
    nums = [13, 46, 24, 52, 20, 9]
    
    print("Before Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()
    
    # Function call for insertion sort
    nums = solution.insertionSort(nums)
    
    print("After Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()

'''
class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while (j >=0 and nums[j] > key):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
              

    