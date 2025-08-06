'''Given an integer array nums, rotate the array to the left by one.



Note: There is no need to return anything, just modify the given array.


Examples:
Input: nums = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation: Initially, nums = [1, 2, 3, 4, 5]

Rotating once to left -> nums = [2, 3, 4, 5, 1]

Input: nums = [-1, 0, 3, 6]

Output: [0, 3, 6, -1]

Explanation: Initially, nums = [-1, 0, 3, 6]

Rotating once to left -> nums = [0, 3, 6, -1]

Input: nums = [7, 6, 5, 4]

Output:
[6, 5, 4, 7]
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Hint 1
Focus on moving the first element of the array to the end while shifting all other elements one position to the left.

Hint 2

Intuition
To rotate an array by one position to the left, consider that the first element of the array will move to the last position, while all other elements shift one position to the left.

The thought process involves first capturing the value of the first element in a temporary variable. Next, iterate through the array starting from the second element and shift each element to the position of its successor. Finally, place the initially captured value into the first position of the array. This approach ensures that the array is rotated by one position to the left effectively.

Approach
Store the value of the first element of the array in a temporary variable.
Iterate through the array starting from the second element.
Shift each element one position to the left by assigning the current element to the position of its predecessor.
After completing the iteration, place the value from the temporary variable into the last position of the array.

Complexity Analysis
Time Complexity: O(N), where N is the number of elements in the array. Each element is visited once during the iteration.

Space Complexity: O(1). The space used does not depend on the size of the input array and remains constant.

class Solution:
    def rotateArrayByOne(self, nums):
        # Store the first element in a temporary variable
        temp = nums[0]
        
        # Shift elements to the left
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        
        # Place the first element at the end
        nums[-1] = temp

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    
    solution.rotateArrayByOne(nums)
    
    print(nums)  # Output the rotated array

'''
class Solution:
    def rotateArrayByOne(self, nums):
        temp=nums[0]
        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
        nums[-1] = temp