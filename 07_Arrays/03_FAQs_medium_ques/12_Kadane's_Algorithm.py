'''Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.



A subarray is a contiguous non-empty sequence of elements within an array.


Examples:
Input: nums = [2, 3, 5, -2, 7, -4]

Output: 15

Explanation: The subarray from index 0 to index 4 has the largest sum = 15

Input: nums = [-2, -3, -7, -2, -10, -4]

Output: -2

Explanation: The element on index 0 or index 3 make up the largest sum when taken as a subarray

Input: nums = [-1, 2, 3, -1, 2, -6, 5]

Output:

6

Submit
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Hint 1
"Maintain two variables: currentMax: Tracks the maximum sum ending at the current index. globalMax: Stores the maximum sum seen so far."

Hint 2
If adding the current element decreases the sum, start a new subarray from the current element. This happens when the previous sum becomes negative.
Intuition 
The idea is to find out all the subarrays of the given array and while finding out the subarray calculate the sum of all the elements of that particular subarray. Finally, find out the maximum sum among them and that will be the result.

Approach 
Iterate in the array lets say i, this variable will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).
Inside the loop, run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
After that for each subarray starting from index i and ending at index j, iterate again to calculate the sum of all the elements(of that particular subarray). Use a max variable to store the maximum sum so far and finally, return the max variable.


Complexity Analysis 
Time Complexity: O(N3), where N is the size of the array. Using three nested loops, each running approximately N times.

Space Complexity: O(1) no extra space used.
from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: list[int]) -> int:
        
        """ Initialize maximum sum with
        the smallest possible integer"""
        maxi = float('-inf')

        # Iterate over each starting index of subarrays
        for i in range(len(nums)):
            
            """ Iterate over each ending index
            of subarrays starting from i"""
            for j in range(i, len(nums)):
                
                """ Variable to store the sum
                of the current subarray"""
                sum = 0

                # Calculate the sum of subarray nums[i...j]
                for k in range(i, j + 1):
                    sum += nums[k]

                """ Update maxi with the maximum of itscurrent
                value and the sum of the current subarray"""
                maxi = max(maxi, sum)

        # Return the maximum subarray sum found
        return maxi

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#create an isinstance of Solution class
sol = Solution()

maxSum = sol.maxSubArray(arr)

#Print the max sum of subarrays
print("The maximum subarray sum is:", maxSum)

'''
class Solution:
    def maxSubArray(self, nums):
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            for j in range(i, n):
                sum=0
                for k in range(i, j+1):
                    sum += nums[k]
                maxi = max(maxi, sum)
        return maxi
#O(N^3) and space complexity= O(1)


 #optimize code         
class Solution:
    def maxSubArray(self, nums):
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
#optimize code tiem complexity=O(N) and space Complexity=O(1)      
           
