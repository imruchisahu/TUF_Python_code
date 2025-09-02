'''
Given a binary array nums and an integer goal. Return the number of non-empty subarrays with a sum goal.



A subarray is a continuous part of the array.


Examples:
Input : nums = [1, 1, 0, 1, 0, 0, 1] , goal = 3

Output : 4

Explanation : The subarray with sum 3 are

[1, 1, 0, 1]

[1, 1, 0, 1, 0]

[1, 1, 0, 1, 0, 0]

[1, 0, 1, 0, 0, 1].

Input : nums = [0, 0, 0, 0, 1] , goal = 0

Output : 10

Explanation : Some of the subarray with sum 0 are

[0]

[0, 0]

[0, 0, 0]

[0, 0, 0, 0]

Constraints:
1 <= nums.length <= 3*104
0 <= goal <= nums.length
nums consist of only 0 and 1.

Intuition:
Here, the idea is to use two-pointers approach to optimize the solution. So, basically instead of finding the count of substrings which have sum exactly equal to goal, try to find out count of subarrays whose sum is less than or equal to goal and the count of subarrays whose sum is less than or equal to goal-1. The difference of both the counts will provide the required result in linear time.

Approach:
Main Function:
It call the helper function to find out number of subarrays with sum less than or equal to goal.
In the second call, it gets the number of subarrays with sum less than or equal to goal - 1. Finally, the difference gives the exact count of subarrays with sum equal to goal.

Helper Function:
First, check for the edge case, if goal is negative, immediately return 0 because no valid subarray can have a negative sum.
Now, initialize few variables: l(left) and r (right) to mark the current window of subarrays within nums, sum to zero to track the current sum of elements in the window, count to zero to accumulate the number of valid subarrays.
Iterate through the array using the right pointer r. Add the element at right pointer to sum to include the current element in the window. While the sum is greater than goal decrease the sum and move the left pointer forward to shrink the window.
Then, Count all subarrays ending at r pointer that satisfy the sum condition. Move the right pointer forward and iterate the whole array. Finally, return count as an answer.

from typing import List

class Solution:
    """ Function to find the number of 
    subarrays with sum equal to `goal` """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """ Calculate the number of subarrays with 
        sum exactly equal to `goal` by using the 
        difference between subarrays with sum less
        than or equal to `goal` and those with sum
        less than or equal to `goal-1` """
        return self.numSubarraysWithSumLessEqualToGoal(nums, goal) - self.numSubarraysWithSumLessEqualToGoal(nums, goal - 1)
    
    """ Helper function to find the number of 
    subarrays with sum less than or equal to `goal` """
    def numSubarraysWithSumLessEqualToGoal(self, nums: List[int], goal: int) -> int:
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
            sum_val += nums[r]
            
            """ Shrink the window from the left
            side if the sum exceeds `goal` """
            while sum_val > goal:
                sum_val -= nums[l]
                
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
    nums = [1, 0, 0, 1, 1, 0]
    goal = 2
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.numSubarraysWithSum(nums, goal)
    
    # Print the result
    print(f"Number of substrings with sum \"{goal}\" is: {ans}")

Complexity Analysis: 
Time Complexity:O(2*2N), where N is the size of the string. The outer loop runs for N time and the inner while loop might be running for N time throughout the program. So it becomes O(2N), also the helper function is being called twice so overall time complexity is O(2*2N).

Space Complexity: O(1). There is no extra space being used.

'''
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        return self.numSubarraysWithSumLessEqualToGoal(nums, goal) - self.numSubarraysWithSumLessEqualToGoal(nums, goal - 1)
    def numSubarraysWithSumLessEqualToGoal(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
        l, r = 0, 0 
        sum_val = 0     
        count = 0   
        while r < len(nums):
            sum_val += nums[r]
            while sum_val > goal:
                sum_val -= nums[l]
                l += 1
            count += (r - l + 1)
            r += 1 
        return count