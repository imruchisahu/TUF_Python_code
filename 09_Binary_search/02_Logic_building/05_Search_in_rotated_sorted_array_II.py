'''Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.


Examples:
Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3

Output: True

Explanation: The element 3 is present in the array. So, the answer is True.

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10

Output: False

Explanation:The element 10 is not present in the array. So, the answer is False.

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 7

Output:
True
Constraints:
  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  nums is guaranteed to be rotated at some pivot.
  -104 <= k <= 104

#Brute Force
# 
Intuition
The simplest way to solve this problem is by using a linear search to check each element of the array one by one.

Approach
Traverse the array from start to end & compare each element with the target value.
If an element matches the target, return True. If no match is found by the end of the array, return False.

Complexity Analysis: 
Time Complexity:O(N), for iterating through N elements, where N is the size of the given array.

Space Complexity:O(1), not using any extra space to solve this problem.

class Solution:
    # Function to search for the target element in a rotated sorted array
    def searchInARotatedSortedArrayII(self, arr, target):
        n = len(arr) 
        
        # Traverse the array to find the target element
        for i in range(n):
            # If the current element matches the target, return true
            if arr[i] == target:
                return True
        # If the target is not found, return false
        return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6] 
    target = 3 

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to search for the target element
    result = sol.searchInARotatedSortedArrayII(arr, target)

    if not result:
        print("Target is not present.")
    else:
        print("Target is present in the array.")

        
#Optimal Approach
Intuition
For looking for a target in a rotated sorted array that has duplicates, use binary search for most optimal results. The tricky part is handling duplicates, especially when they are at both ends of the array. Start by finding the sorted half of the array and checking if the target is there. If duplicates make it hard to find the sorted half, just skip them by moving our pointers. This way, keep narrowing down the search space efficiently.

Approach
Initialize two pointers: low at the start and high at the end of the array.
Inside a loop, calculate the midpoint (mid). If arr[mid] is the target, return True.
Check if arr[low], arr[mid], and arr[high] are equal. If so, increment low and decrement high to skip duplicates.
Identify the sorted half: If arr[low] <= arr[mid], the left half is sorted. Otherwise, the right half is sorted.
Adjust the pointers based on the target's location: If the left half is sorted and the target is within this range, adjust high to mid - 1. Otherwise, adjust low to mid + 1. If the right half is sorted and the target is within this range, adjust low to mid + 1. Otherwise, adjust high to mid - 1.
Continue this process until low exceeds high. If no target is found, return False.

Complexity Analysis: 
Time Complexity:O(logN) for the best and average cases. As in the best and average scenarios, the binary search algorithm is primarily used and hence the time complexity is O(logN).
However, in the worst-case scenario, it'll be O(N/2) where all array elements are the same but not the target (e.g., given array = {3, 3, 3, 3, 3, 3, 3}), we continue to reduce the search space by adjusting the low and high pointers until they intersect, which will end up taking O(N/2) time complexity.

Space Complexity:O(1), as we are not using any extra space to solve this problem.

class Solution:
    # Function to search for the target element
    # in a rotated sorted array with duplicates
    def searchInARotatedSortedArrayII(self, arr, target):
        n = len(arr)
        low, high = 0, n - 1
        
        # Applying binary search algorithm 
        while low <= high:
            mid = (low + high) // 2

            # Check if mid points to the target
            if arr[mid] == target:
                return True

            # Handle duplicates: if arr[low], arr[mid], and arr[high] are equal
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue

            # Check if the left part is sorted
            if arr[low] <= arr[mid]:
                # Eliminate the right part if target exists in the left sorted part
                if arr[low] <= target <= arr[mid]:
                    high = mid - 1
                # Otherwise eliminate the left part
                else:
                    low = mid + 1
            else:
                # If the right part is sorted and target exists in the right sorted part, eliminate the left part
                if arr[mid] <= target <= arr[high]:
                    low = mid + 1
                # Otherwise eliminate the right part
                else:
                    high = mid - 1
        
        # If target is not found
        return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    target = 3 

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to search for the target element
    result = sol.searchInARotatedSortedArrayII(arr, target)

    if not result:
        print("Target is not present.")
    else:
        print("Target is present in the array.")


'''
class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        n=len(nums)
        for i in range(n):
            if nums[i] == k:
                return True
        return False