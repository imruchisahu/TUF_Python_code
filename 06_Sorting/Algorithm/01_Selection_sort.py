''''Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.



A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.


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
Think Small First, at each step, identify the smallest element in the unsorted portion of the array and place it in its correct position.

Hint 2
Use Divide and Conquer Mindset, visualize sorting as splitting the array into sorted and unsorted parts, and shrinking the unsorted part one element at a time.

Hint 3

Intuition
The selection sort algorithm sorts an array by repeatedly finding the minimum element from the unsorted part and putting it at the beginning. The largest element will end up at the last index of the array.

Approach
Select the starting index of the unsorted part using a loop with i from 0 to n-1.
Find the smallest element in the range from i to n-1 using an inner loop.
Swap this smallest element with the element at index i.
Repeat the process for the next starting index.


Complexity Analysis  
Time Complexity: O(N2) where N is the length of the input array. The outer loop runs through each element, and the inner loop finds the smallest element in the unsorted portion of the array.

Space Complexity: O(1) as it is an in-place sorting algorithm and does not require additional storage proportional to the input size.



class Solution:
    def selectionSort(self, nums):
        # Loop through unsorted part 
        # of the array (0 to n-2)
        for i in range(len(nums) - 1):
            #Assume current  element is minimum 
            min_index = i

            #Find actual minimum in unsorted part (i+1 to n-1)
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j

         #Swap only if minIndex changed (optimization) 
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums

# Main function to test the selection sort
if __name__ == "__main__":
    solution = Solution()
    nums = [64, 25, 12, 22, 11]
    sorted_nums = solution.selectionSort(nums)
    print("Sorted array:", sorted_nums)


'''
class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j 
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums