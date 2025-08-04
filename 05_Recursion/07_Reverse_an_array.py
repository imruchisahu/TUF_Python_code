'''Given an array nums of n integers, return reverse of the array.


Examples:
Input : nums = [1, 2, 3, 4, 5]

Output : [5, 4, 3, 2, 1]

Input : nums = [1, 3, 3, 3, 5]

Output : [5, 3, 3, 3, 1]

Input : nums = [1, 2, 1]

Output:
[1, 2, 1]
Constraints:
1 <= n <= 100
1 <= nums[i] <= 100

Intuition
The concept of reversing an array involves swapping elements from both ends, moving towards the center. Recursion facilitates this by initially swapping the first and last elements, then progressively moving inward until the pointers converge at the center.

Approach
Start with two pointers p1 and p2, for example: one at the beginning of the array and one at the end. Swap the elements at these two pointers.
Move the left pointer one step to the right and the right pointer one step to the left. Repeat the swap operation until the two pointers meet or cross each other.
Post swapping, call the recursion to perform the same operations again on the next pair of elements.
Return the reversed array.
Dry Run


Complexity Analysis
Time Complexity: O(N) The time complexity is O(N) because we perform a constant-time swap operation for each element pair.

Space Complexity : O(N) The space complexity is O(N) due to the recursion stack.

class Solution:
    def reverseArray(self, nums):
        # Call the helper function to reverse the array
        self.reverse(nums, 0, len(nums) - 1) 
        # Return the reversed array 
        return nums  

    def reverse(self, nums, left, right):
        if left >= right:
            return 
        # Swap the elements        
        nums[left], nums[right] = nums[right], nums[left]  
        # Recursive call with updated pointers
        self.reverse(nums, left + 1, right - 1)  

# Main method for testing the reverseArray function
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]  
    result = solution.reverseArray(nums)  
    print(result)  # Print the reversed array

'''
class Solution:
    def reverseArray(self, nums):
        self.reverse(nums, 0, len(nums) - 1)
        return nums
    
    def reverse(self, nums, left, right):
        if left >= right:
            return
        nums[left], nums[right] = nums[right], nums