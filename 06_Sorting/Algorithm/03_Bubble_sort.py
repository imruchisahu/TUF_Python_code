'''Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.



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

Hint 2

Intuition
The bubble sort algorithm sorts an array by repeatedly swapping adjacent elements if they are in the wrong order. The largest elements "bubble" to the end of the array with each pass.

Approach
Run a loop i from n-1 to 0.
Run a nested loop from j from 0 to i-1.
If arr[j] > arr[j+1], swap them.
Continue until the array is sorted.
Note: Here, after each iteration, the array becomes sorted up to the last index of the range. That is why the last index of the range decreases by 1 after each iteration. This decrement is managed by the outer loop, where the last index is represented by the variable i. The inner loop (variable j) helps to push the maximum element of the range [0...i] to the last index (i.e., index i).


Complexity Analysis:  
Time Complexity: O(N2) for the worst and average cases and O(N) for the best case. Here, N is the size of the array.

Space Complexity: O(1), because Bubble Sort is an in-place sorting algorithm, meaning it only requires a constant amount of extra space for its operations, regardless of the size of the input array.
class Solution:
     # Bubble Sort Function
    def bubbleSort(self, nums):
        n = len(nums)
        # Traverse through the array
        for i in range(n - 1, -1, -1):
            # Track if swaps are made
            isSwapped = False
            for j in range(i):
                # Swap if next element is smaller
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    isSwapped = True
            # Break out of loop if no swaps done
            if not isSwapped:
                break
        return nums

# Main function
if __name__ == "__main__":
    # Create an instance of solution class
    solution = Solution()

    nums = [7, 4, 1, 5, 3]

    print("Array Before Using Bubble Sort:", nums)

    # Function call for Bubble Sort
    sorted_nums = solution.bubble_sort(nums)

    print("Array After Using Bubble Sort:", sorted_nums)


'''

class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n-1, -1, -1):
            isSwapped = False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isSwapped = True

            if not isSwapped:
                break
        return nums