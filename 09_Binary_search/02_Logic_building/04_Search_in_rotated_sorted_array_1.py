'''Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.


Examples:
Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0

Output: 4

Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3

Output: -1

Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 5

Output:
1
Constraints:
  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  All values of nums are unique.
  nums is an ascending array that is possibly rotated.
  -104 <= k <= 104
  
  #Linear Search Approach
  Intuition:
The naive approach to solve this problem is by traversing the array linearly and returning the index at which we find the target element. In case we don't find the target element in the array we return -1.

Approach:
Traverse the array & for each element in the array, check if it is equal to the target. If a match is found, return the index of the matching element.
If the entire array is traversed and no matching element is found, return -1 to indicate that the target is not present in the array.
Dry Run: Please refer to the video for the dry-run.


Complexity Analysis: 
Time Complexity: O(N), N = size of the given array. Since we have to iterate through the entire array to check if the target is present in the array.

Space Complexity: O(1), as we have not used any extra data structures. This makes space complexity, even in the worst case, O(1).

class Solution:
    # Function to search for the target element in the array
    def search(self, nums, target):
        # Get the size of the array
        n = len(nums)

        # Loop through the array to find the target element
        for i in range(n):
            # Check if the current element is the target
            if nums[i] == target:
                # Return the index if the target is found
                return i

        # Return -1 if the target is not found
        return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    # Create an instance of the Solution class
    sol = Solution()
    
    # Function call to search for the target element
    result = sol.search(nums, target)

    if result == -1:
        print("Target is not present.")
    else:
        print("The index is:", result)

#Binary Search Approach
Intuition:
The optimal approach would be by dividing the array in halves and implement binary search. The most important thing to note here is that, at any middle point, one side of the array will still be sorted. Use this logic & by figuring out which half is sorted, decide which half to keep searching in, making the search efficient even in a rotated array.

Approach:
Start with two pointers: low at the beginning and high at the end of the array & calculate the midpoint (mid). If nums[mid] is the target, return mid.
Determine which half of the array is sorted. If the left half is sorted and the target is within this range, search in the left half. Otherwise, search in the right half, if it is sorted and the target is within this range, search in the right half. Otherwise, search in the left half.
Continue this process until the pointers low and high cross. If the target is not found, return -1.
class Solution:
    # Function to search for the target element in a rotated sorted array
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        # Applying binary search algorithm
        while low <= high:
            mid = (low + high) // 2

            # Check if mid points to the target
            if nums[mid] == target:
                return mid

            # Check if the left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    # Target exists in the left sorted part
                    high = mid - 1
                else:
                    # Target does not exist in the left sorted part
                    low = mid + 1
            else:
                # Check if the right part is sorted
                if nums[mid] <= target <= nums[high]:
                    # Target exists in the right sorted part
                    low = mid + 1
                else:
                    # Target does not exist in the right sorted part
                    high = mid - 1

        # If target is not found
        return -1

if __name__ == "__main__":
    nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    target = 1

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to search for the target element
    result = sol.search(nums, target)

    if result == -1:
        print("Target is not present.")
    else:
        print("The index is:", result)
Complexity Analysis: 
Time Complexity: O(logN), as the search space is reduced logarithmically, where N is the size of the given array.

Space Complexity: O(1), not using any extra data structure.
  '''
class Solution:
    def search(self, nums, k):
        n=len(nums)
        for i in range(n):
            if nums[i] == k:
                return i
        return -1

