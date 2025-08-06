'''Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.


Examples:
Input: nums = [0, 2, 3, 1, 4]

Output: 5

Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Input: nums = [0, 1, 2, 4, 5, 6]

Output: 3

Explanation: nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]

Input: nums = [1, 3, 6, 4, 2, 5]

Output:
0
Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Hint 1
"Use the formula for the sum of the first n natural numbers: S= (n×(n+1))/2. Subtract the sum of the array elements from S to find the missing number."

Hint 2
Leverage the XOR property: x⊕x=0 and x⊕0=x. XOR all indices and array values; the missing number will be the result.

Intuition
For each number between 0 to N, try to find it in the given array using linear search. And if any number is not found, return that number.

Approach 
Iterate let's say i from 0 to N & for each integer i, try to find it in the given array using linear search.
To find the number, run another loop and consider a flag variable to indicate if the element exists in the array, where flag when set to 1 means the element is present and flag when set to 0 means the element is missing.
Initially, the flag value will be set to 0. While iterating the array, if we find the element, set the flag to 1 and break out from the loop. Now, for any number i, if its not found the flag will remain 0 even after iterating the whole array and will return the number.


Complexity Analysis 
Time Complexity: O(N^2), where N is the size of the array. In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N^2).

Space Complexity: O(1) , as no extra space is used.

from typing import List

class Solution:
    # Function to find the missing number
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate N from the length of nums
        N = len(nums) 
        
        # Outer loop that runs from 0 to N
        for i in range(0, N+1):
            """ Flag variable to check 
            if an element exists"""
            flag = 0
            
            """ Search for the element
            using linear search"""
            for num in nums:
                if num == i:
                    # i is present in the array
                    flag = 1
                    break
            
            """ Check if the element 
            is missing (flag == 0)"""
            if flag == 0:
                return i
        
        """ The following line will never 
        execute, it is just to avoid warnings"""
        return -1

# Main function to test the implementation
if __name__ == "__main__":
    nums = [0,1, 2, 4]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the missingNumber method to find the missing number
    ans = solution.missingNumber(nums)
    
    print(f"The missing number is: {ans}")

'''
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        for i in range(0, n+1):
            flag=0
            for num in nums:
                if num == i:
                    flag = 1
                    break
            if flag == 0:
                return i
        return -1