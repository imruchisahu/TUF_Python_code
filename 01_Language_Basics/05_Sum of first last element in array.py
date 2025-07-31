'''Given an integer array nums, return the sum of the 1st and last element of the array.


Examples:
Input: nums = [2, 3, 4, 5, 6]

Output: 8

Explanation: 1st element = 2, last element = 6, sum = 2 + 6 = 8.

Input: nums = [2]

Output: 4

Explanation: 1st element = last element = 2, sum = 2 + 2 = 4.

Input: nums = [-1, 2, 4, 1]

Output:
0
Constraints:
1 <= Number of elements in nums <= 100
-100 <= nums[i] <= 100

Approach:
Check Array Length: Ensure that the array is not empty to avoid accessing elements in an empty array.
Retrieve Elements:
Access the first element of the array.
Access the last element of the array.
Compute Sum: Add the first and last elements.
Return Result: Return the computed sum.
//Solution:

class Solution:
    # Function to return the sum of
    # the 1st and last element of the array
    def sumOfFirstAndLast(self, nums):
        # Check if the array is empty
        if not nums:
            return 0 # Return 0

        # Get the first element
        first = nums[0]
        # Get the last element
        last = nums[-1]
        
        # Return sum of the first and last elements
        return first + last

# Creating an instance of Solution class
sol = Solution()

nums = [2, 3, 4, 5, 6]

# Function call to return the sum of
# the 1st and last element of the array
ans = sol.sumOfFirstAndLast(nums)

print("Sum of first and last element:", ans)
'''
class Solution:
    def sumOfFirstAndLast(self, nums):
        if not nums:
            return 0
        first = nums[0]
        last = nums[-1]

        return first + last
Solution()