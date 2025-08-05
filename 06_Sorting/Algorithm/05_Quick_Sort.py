'''Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.



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
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.

Similar Problems

Hint 1
Focus on choosing a pivot element. All elements smaller than the pivot go to its left, and all larger elements go to its right. Think about recursively applying the same partitioning logic to the left and right subarrays created by the pivot.

Hint 2

Intuition:
Quick Sort is a divide-and-conquer algorithm like Merge Sort. However, unlike Merge Sort, Quick Sort does not use an extra array for sorting (though it uses an auxiliary stack space). This makes Quick Sort slightly better than Merge Sort from a space perspective.

This algorithm follows two simple steps repeatedly:

Pick a pivot and place it in its correct position in the sorted array.
Move smaller elements (i.e., smaller than the pivot) to the left of the pivot and larger ones to the right.
To summarize: The main goal is to place the pivot at its final position in each recursion call, where it should be in the final sorted array.

Dry Run:
Quick Sort
Approach:
To implement Quick Sort, we will create two functions: quickSort() and partition().

quickSort(arr[], low, high)
Initial Setup: The low pointer points to the first index, and the high pointer points to the last index of the array.
Partitioning: Use the partition() function to get the index where the pivot should be placed after sorting. This index, called the partition index, separates the left and right unsorted subarrays.
Recursive Calls: After placing the pivot at the partition index, recursively call quickSort() for the left and right subarrays. The range of the left subarray will be [low to partition index - 1] and the range of the right subarray will be [partition index + 1 to high].
Base Case: The recursion continues until the range becomes 1.
partition(arr[], low, high)
Select pivot (random element) and swap it with the first element.
Use pointers i (low) and j (high). Move i forward to find element > pivot, and j backward to find element < pivot. Ensure i <= high - 1 and j >= low + 1.
If i < j, swap arr[i] and arr[j].
Continue until j < i.
Swap pivot (arr[low]) with arr[j] and return j as partition index.
This approach ensures that Quick Sort efficiently sorts the array using the divide-and-conquer strategy.


Complexity Analysis:  
Time Complexity: O(N*logN), where N = size of the array. At each step, we divide the whole array, which takes logN steps, and n steps are taken for the partition() function, so overall time complexity will be N*logN.

The following recurrence relation can be written for Quick sort:

F(n) = F(k) + F(n-1-k)

Here, k is the number of elements smaller or equal to the pivot and n-1-k denotes elements greater than the pivot.

There can be 2 cases:

Worst Case: This case occurs when the pivot is the greatest or smallest element of the array. If the partition is done and the last element is the pivot, then the worst case would be either in the increasing order of the array or in the decreasing order of the array.

Recurrence:

F(n) = F(0) + F(n-1) or F(n) = F(n-1) + F(0)

Worst Case Time Complexity: O(n2)

Best Case: This case occurs when the pivot is the middle element or near to middle element of the array.

Recurrence:

F(n) = 2F(n/2)

Time Complexity for the best and average case: O(N*logN)

Space Complexity: O(1) + O(N) auxiliary stack space, where N = size of the array.

import random

class Solution:
    # Function to partition the array
    def partition(self, arr, low, high):
        # Choosing a random index between low and high
        randomIndex = low + random.randint(0, high - low)
        # Swap the random element with the first element
        arr[low], arr[randomIndex] = arr[randomIndex], arr[low]

        # Now choosing arr[low] as the pivot after the swap
        pivot = arr[low]
        # Starting index for left subarray
        i = low
        # Starting index for right subarray
        j = high

        while i < j:
            # Move i to the right until we find an element greater than the pivot
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            # Move j to the left until we find an element smaller than the pivot
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            # Swap elements at i and j if i is still less than j
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Pivot placed in correct position
        arr[low], arr[j] = arr[j], arr[low]
        return j

    # Helper Function to perform the recursive quick sort
    def quickSortHelper(self, arr, low, high):
        # Base case: If the array has one or no elements, it's already sorted
        if low < high:
            # Get the partition index
            pIndex = self.partition(arr, low, high)
            # Sort the left subarray
            self.quickSortHelper(arr, low, pIndex - 1)
            # Sort the right subarray
            self.quickSortHelper(arr, pIndex + 1, high)

    # Function to perform quick sort on given array
    def quickSort(self, nums):
        # Get the size of array
        n = len(nums)

        # Perform quick sort
        self.quickSortHelper(nums, 0, n - 1)

        # Return sorted array
        return nums


if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    n = len(arr)

    print("Before Sorting Array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    # Create an instance of Solution class
    solution = Solution()

    # Function call to sort the array using quick sort
    sortedArr = solution.quickSort(arr)

    print("After Sorting Array: ")
    for i in range(n):
        print(sortedArr[i], end=" ")
    print()

'''
import random
class Solution:

    def partition(self, arr, low, high):
        randomIndex = low + random.randint(0, high - low)
        arr[low], arr[randomIndex] = arr[randomIndex], arr[low]
        pivot = arr[low]
        i=low
        j=high
        while i < j:
            while arr[i] <= pivot and i <= high -1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
    def quickSortHelper(self, arr, low, high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSortHelper(arr, low, pIndex - 1)
            self.quickSortHelper(arr, pIndex + 1, high)
    def quickSort(self, nums):
        n= len(nums)
        self.quickSortHelper(nums, 0, n - 1)
        return nums

