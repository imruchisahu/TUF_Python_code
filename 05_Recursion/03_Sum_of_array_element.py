'''Given an array nums, find the sum of elements of array using recursion.


Examples:
Input : nums = [1, 2, 3]

Output : 6

Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Input : nums = [5, 8, 1]

Output : 14

Explanation : The sum of elements of array is 5 + 8 + 1 => 14.

Input : nums = [12, 9, 17]

Output:
38
Constraints:
1 <= n <= 100
1 <= nums[i] <= 100
Intuition
Computing the sum of an array's elements through recursion involves thinking about adding the first element to the sum of the rest. This process continues by recursively considering one element at a time, gradually reducing the array until reaching the point where no elements are left to add.

Approach
Define a recursive helper function sum(nums, left) where nums is the array and left is the current index.
In the helper function: Base case: If the left index is out of bounds (i.e., left >= nums.length), return 0 because there are no more elements to add. Recursive case: Add the current element nums[left] to the sum of the remaining elements, obtained by recursively calling the function with the next index left + 1.
The initial call to the helper function is made from the main function with the starting index 0.
Dry Run


Time and Space Complexity
Time Complexity : O(N) The time complexity is O(N) because each element in the array is processed exactly once.
Space Complexity : O(N)The space complexity is O(N) due to the recursion stack, which can grow up to the size of the array.
class Solution:
    def arraySum(self, nums):
        # Start from index 0
        return self.sum(nums, 0)

    def sum(self, nums, left):
        # Base case: out of bounds
        if left >= len(nums):
            return 0
        # Add current element and recurse
        return nums[left] + self.sum(nums, left + 1)

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3] 
    result = solution.arraySum(nums)   
    print(result) 


'''

class Solution:
    def arraySum(self, nums):
        #your code goes here
        return self.sum(nums, 0)

    def sum(self, nums, left):
        if left >= len(nums):
            return 0
        return nums[left] + self.sum(nums, left + 1)
       