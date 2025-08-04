'''Given an array arr of size n, the task is to find the sum of all the elements in the array.


Examples:
Input: n=5, arr = [1,2,3,4,5]



Output: 15



Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Input: n=6, arr = [1,2,1,1,5,1]



Output: 11



Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11

Input: n=3, arr = [2,1,1]

Output:
4
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104
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
    def sum(self,arr, n): 
        return sum(arr)
    
