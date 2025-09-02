'''
Given an array nums and an integer k. An array is called nice if and only if it contains k odd numbers. Find the number of nice subarrays in the given array nums.



A subarray is continuous part of the array.


Examples:
Input : nums = [1, 1, 2, 1, 1] , k = 3

Output : 2

Explanation : The subarrays with three odd numbers are

[1, 1, 2, 1]

[1, 2, 1, 1]

Input : nums = [4, 8, 2] , k = 1

Output : 0

Explanation : The array does not contain any odd number.

Input : nums = [41, 3, 5] , k = 2

Output:
2
Constraints:
1 <= nums.length <= 5*104
1 <= nums[i] <= 105
1 <= k <= nums.length

Intuition:
Here, the idea is to use two-pointers approach to optimize the solution. As, this problem is a slight variation of the problem of finding count of subarrays with given sum in binary array, the thought process would be very similar. Take the modulo 2 of the elements and if the element is even it will become 0 , else it will become 1, thus the array would be converted into a binary subarray. So, basically instead of finding the count of substrings which have exactly k odd elements, try to find out count of subarrays where the number of odd elements is less than or equal to k and the count of subarrays with odd elements less than or equal to goal-1. The difference of both the counts will provide the required result in linear time.

Approach:
Main Function:
It call the helper function to find out number of subarrays with odd numbers less than or equal to k.
In the second call, it gets the number of subarrays with odd numbers less than or equal to k - 1. Finally, the difference gives the exact count of subarrays with k odd elements.

Helper Function:
First, check for the edge case, if goal is negative, immediately return 0 because no valid subarray can have a negative sum.
Now, initialize few variables: l(left) and r (right) to mark the current window of subarrays within nums, sum to zero to track the current sum of elements in the window, count to zero to accumulate the number of valid subarrays.
Iterate through the array using the right pointer r. Add the element at right pointer to sum to include the current element in the window. While the sum is greater than k decrease the sum and move the left pointer forward to shrink the window.
Then, Count all subarrays ending at r pointer that satisfy the sum condition. Move the right pointer forward and iterate the whole array. Finally, return count as an answer.

from typing import List

class Solution:
    """ Function to find the number of 
    nice subarrays with k odd numbers` """
    def numberOfOddSubarrays(self, nums: List[int], k: int) -> int:
        """ Calculate the number of subarrays with 
        sum exactly equal to `k` by using the 
        difference between subarrays with sum less
        than or equal to `k` and those with sum
        less than or equal to `k-1` """
        return self.helper(nums, k) - self.helper(nums, k - 1)
    
    """ Helper function to find the number of 
    subarrays with sum less than or equal to `goal` """
    def helper(self, nums: List[int], goal: int) -> int:
        """ If goal is negative, there 
        can't be any valid subarray sum """
        if goal < 0:
            return 0
        
        # Pointers to maintain the current window
        l, r = 0, 0 
        
        """ Variable to track the current
        sum of elements in the window"""
        sum_val = 0     
        
        # Variable to count the number of subarrays
        count = 0   
        
        # Iterate through the array 
        while r < len(nums):
            sum_val += nums[r] % 2
            
            """ Shrink the window from the left
            side if the sum exceeds `goal` """
            while sum_val > goal:
                sum_val -= nums[l] % 2
                
                # Move the left pointer `l` forward
                l += 1
            
            """ Count all subarrays ending at
            `r` that satisfy the sum condition """
            count += (r - l + 1)
            
            # Move the right pointer `r` forward 
            r += 1 
        
        # Return the total count of subarrays
        return count

# Example usage:
if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 1
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.numberOfOddSubarrays(nums, k)
    
    # Print the result
    print(f"Number of nice subarrays with \"{k}\" odd numbers is: {ans}")
    
Complexity Analysis: 
Time Complexity:O(2*2N), where N is the size of the string. The outer loop runs for N time and the inner while loop might be running for N time throughout the program. So it becomes O(2N), also the helper function is being called twice so overall time complexity is O(2*2N).

Space Complexity: O(1). There is no extra space being used.

'''
from typing import List
class Solution:
    def numberOfOddSubarrays(self, nums, k):
        return self.helper(nums, k) - self.helper(nums, k - 1)
    def helper(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
        l, r = 0, 0 
        sum_val = 0    
        count = 0   
        while r < len(nums):
            sum_val += nums[r] % 2
            while sum_val > goal:
                sum_val -= nums[l] % 2
                l += 1
            count += (r - l + 1)
            r += 1 
        return count