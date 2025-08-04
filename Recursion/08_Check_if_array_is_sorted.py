'''Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


Examples:
Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Input : nums = [1, 2, 1, 4, 5]

Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

Input : nums = [1,9,6,8,5,4,0]

Output:
false
Constraints:
1 <= n <= 100
1 <= nums[i] <= 100

Intuition
To determine if an array is sorted in non-decreasing order using recursion, consider comparing each element with the one following it. If an element exceeds the next one, the array is not sorted. This comparison is then repeated for the entire array.

Approach
If the array has 0 or 1 elements, it is already sorted. So, return true.
Use a helper function sort that takes the array and two pointers, left and right, to compare elements.
In the helper function, check if the array is sorted by comparing elements at the left and right pointers; if right reaches the end of the array, the array is sorted, so return true; if the element at left is greater than the element at right, return false because the array is not sorted; otherwise, move both pointers to the next elements and call the helper function recursively.
Dry Run


Complexity Analysis
Time Complexity O(N): The time complexity of this recursive solution is O(N) because the helper function makes a recursive call for each element in the array, moving from the beginning to the end of the array.

Space Complexity O(N): The space complexity of this solution is O(N) Due to the recursion stack. Each recursive call adds a new frame to the call stack, and in the worst case, there will be n frames on the stack (one for each call).

class Solution:
    def isSorted(self, nums):
        # Ensure nums is a list to use len() function
        nums = list(nums)
        # An array with 0 or 1 element is always considered sorted
        if len(nums) <= 1:
            return True
        # Check if the array is sorted starting from index 0 to 1
        return self.sort(nums, 0, 1)
    
    def sort(self, nums, left, right):
        # If we reach the end of the array
        # it means the array is sorted
        if right >= len(nums):
            return True
        # If we find a pair where the left element is greater than the right
        # the array is not sorted
        if nums[left] > nums[right]:
            return False
        # Move to the next pair of elements
        return self.sort(nums, left + 1, right + 1)

# Main method for testing the isSorted function
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5] 
    result = solution.isSorted(nums) 
    print("Array is sorted" if result else "Array is not sorted")

'''
class Solution:
    def isSorted(self, nums):
        #your code goes here
        nums = list(nums)
        if len(nums) <= 1:
            return True
        return self.sort(nums, 0, 1)
    
    def sort(self, nums, left, right):
        if right >= len(nums):
            return True

        if nums[left] > nums[right]:
            return False

        return self.sort(nums, left + 1, right + 1)
            