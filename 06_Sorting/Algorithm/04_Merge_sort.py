'''Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.



A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.


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
1 <= nums.length <= 106
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.

Intuition:
Merge Sort is a powerful sorting algorithm that follows the divide-and-conquer approach. The array is divided into two equal halves until each sub-array contains only one element. Each pair of smaller sorted arrays is then merged into a larger sorted array.

The algorithm consists of two main functions:

merge():This function merges the two halves of the array, assuming both parts are already sorted.
mergeSort():This function divides the array into 2 parts: low to mid and mid+1 to high where, low is the leftmost index of the array, high is the rightmost index of the array, and mid is the middle index of the array.
By repeating these steps recursively, Merge Sort efficiently sorts the entire array.

Approach:
To implement Merge Sort, we will create two functions: mergeSort() and merge().

mergeSort(arr[], low, high)

Divide the Array: Split the given array into two halves by splitting the range. For any range from low to high, the splits will be low to mid and mid+1 to high, where mid = (low + high) / 2. This process continues until the range size is 1.
Recursive Division: In mergeSort(), divide the array around the middle index by making recursive calls: mergeSort(arr, low, mid) for the left half and mergeSort(arr, mid+1, high) for the right half. Here, low is the leftmost index, high is the rightmost index, and mid is the middle index of the array.
Base Case: To complete the recursive function, define the base case. The recursion ends when the array has only one element left, meaning low and high are the same, pointing to a single element. If low >= high, the function returns.
merge(arr[], low, mid, high)

Use a temporary array to store the elements of the two sorted halves after merging. The range of the left half is from low to mid and the range of the right half is from mid+1 to high.
Use two pointers, left starting from low and right starting from mid+1. Using a while loop (while left <= mid && right <= high), compare the elements from each half and insert the smaller one into the temporary array. After the loop, any leftover elements in both halves are copied into the temporary array.
Transfer the elements from the temporary array back to the original array in the range low to high.
This approach ensures that the array is efficiently sorted using the divide-and-conquer strategy of Merge Sort.


Complexity Analysis:  
Time Complexity: O(nlogn). At each step, we divide the whole array, which takes logn steps, and we assume n steps are taken to sort the array. So, the overall time complexity is nlogn.

Space Complexity: O(n). We are using a temporary array to store elements in sorted order.
class Solution:
    # Function to merge two sorted halves of the array
    def merge(self, arr, low, mid, high):
        # Temporary array to store merged elements
        temp = []
        left = low
        right = mid + 1

        # Loop until subarrays are exhausted
        while left <= mid and right <= high:
            # Compare left and right elements
            if arr[left] <= arr[right]:
                # Add left element to temp
                temp.append(arr[left])
                # Move left pointer
                left += 1
            else:
                # Add right element to temp
                temp.append(arr[right])
                # Move right pointer
                right += 1

        # Adding the remaining elements of left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Adding the remaining elements of right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Transferring the sorted elements to arr
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Helper function to perform merge sort from low to high
    def mergeSortHelper(self, arr, low, high):
        # Base case: if the array has only one element
        if low >= high:
            return
        
        # Find the middle index
        mid = (low + high) // 2
        # Recursively sort the left half
        self.mergeSortHelper(arr, low, mid)
        # Recursively sort the right half
        self.mergeSortHelper(arr, mid + 1, high)
        # Merge the sorted halves
        self.merge(arr, low, mid, high)

    # Function to perform merge sort on the given array
    def mergeSort(self, nums):
        n = len(nums) # Size of array
        
        # Perform Merge sort on the whole array
        self.mergeSortHelper(nums, 0, n - 1)
        
        # Return the sorted array
        return nums


if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    # Create an instance of the Solution class
    sol = Solution()
    # Function call to sort the array
    sortedArr = sol.mergeSort(arr)

    print("After Sorting Array: ")
    for i in range(n):
        print(sortedArr[i], end=" ")
    print()

'''
class Solution:
    def merge(self, arr, low, mid, high):
        temp_arr=[]
        left=low
        right = mid + 1
        while left <= mid and right <= high: # loop until subarray are exhausted
            if arr[left] <= arr[right]: #comparing left right ele
                temp_arr.append(arr[left])
                left += 1
            else:
                temp_arr.append(arr[right])
                right += 1

        while left<= mid: # add remaining ele of left ha
            temp_arr.append(arr[left])
            left += 1
        
        while right<= high: # add remaining ele of right
            temp_arr.append(arr[right])
            right += 1

        for i in range(low, high + 1): #transfer the sorted ele to arr
            arr[i] = temp_arr[i-low]
    def mergeSortHelper(self, arr, low, high):
        if low >= high: #if arr has one ele
            return
        mid = (low + high) // 2
        self.mergeSortHelper(arr, low, mid) #sort left halves
        self.mergeSortHelper(arr, mid + 1, high) # sort right halves
        self.merge(arr, low, mid, high) # merge both left and right halves


    def mergeSort(self, nums):
        n=len(nums)
        self.mergeSortHelper(nums, 0, (n - 1))
        return nums
        
