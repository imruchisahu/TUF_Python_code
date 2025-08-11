'''Given an array of integers nums and an integer limit as the threshold value, find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, the sum of the division results is less than or equal to the threshold value.

Each result of the division is rounded up to the nearest integer greater than or equal to that element.


Examples:
Input: nums = [1, 2, 3, 4, 5], limit = 8

Output: 3

Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 

The sum is 9(1 + 1 + 2 + 2 + 3) if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

Input: nums = [8,4,2,3], limit = 10

Output: 2

Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9 (4+2+1+2) <= 10 as the answer. So, 2 is the answer.

Input: nums = [8,4,2,3], limit = 4

Output:
2
8
4
3

Submit
Constraints:
1 <= nums.length <= 5 * 104
 1 <= nums[i] <= 106
 nums.length <= limit <= 106
 
 #Linear Search
 Intuition: 
The extremely naive approach is to use linear search to check all possible divisors from 1 to maximum element of the array. The minimum number for which the result is less than or equal to threshold value(limit), will be our answer.

Approach: 
Traverse from 1 to maximum element of the array to check all possible divisors.
Within this loop, divide each element in the array by the current divisor, and sum up the obtained ceiling values.
If result is less than or equal to threshold, return the current divisor as our answer.
Finally, if we are outside the nested loops, return -1 as no such divisor is found.

Cpp
Java
Python
Javascript
C#
Go


import math

class Solution:
    # Function to find the smallest divisor
    def smallestDivisor(self, nums, limit):
        # Size of array
        n = len(nums)

        # Find the maximum element in nums
        maxi = max(nums)

        # Find the smallest divisor
        for d in range(1, maxi + 1):
            sum = 0

            """ Calculate the sum of ceil
            (nums[i] / d) for all elements """
            for num in nums:
                sum += math.ceil(num / d)

            # Check if the sum is <= limit
            if sum <= limit:
                return d

        # Return -1 if no valid divisor found
        return -1

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    limit = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.smallestDivisor(nums, limit)

    # Print the result
    print(f"The minimum divisor is: {ans}")
Complexity Analysis: 
Time Complexity:O(max*N), where max is the maximum element in the array, N is size of the array. As nested loops are being used. The outer loop runs from 1 to max and the inner loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#Binary Search
Intuition: 
Here the idea is to use binary search to efficiently solve this problem by dividing the search space into halves. As, the search space of this probem is in the range[1, max], where max is the maximum element of the array. It can be considered as a sorted search space, hence binary search can be applied.

Approach: 
Working of smallestDivisor(nums, limit):
Iterate using while (low less than or equal to high) to find the smallest divisor.
Compute mid as the midpoint between low and high. Mid would be representing the current divisor.
Use the helper function sumByD(nums, mid) to check if the summation of division values for mid is less than or equal to limit, if yes, eliminate the left half of the search space. Else, eliminate the right half, as we need to find a greater divisor.

Working of sumByD(nums, limit):
Initialize 'n' to the size of nums, 'sum' is initialized to zero, which will accumulate the sum of division results.
Iterate through each element in the array using a for-loop. For each element, the division result is computed. This division result is cast to double to ensure floating-point precision. The ceil function is applied to round up the division result to the nearest integer. This ensures that even if there's a fractional part, it is rounded up.
The rounded-up division result is added to 'sum' in each iteration of the loop. This accumulates the total sum of all such rounded-up division results for all elements in nums.
Finally, after iterating through all elements in array, the return the accumulated sum, which represents the total sum of division results rounded up to the nearest integer for each element divided by limit.

Cpp
Java
Python
Javascript
C#
Go


import math

class Solution:
    """ Helper function to find the 
    summation of division values"""
    def sumByD(self, nums, limit):
        # Size of array
        n = len(nums)  
        
        # Find the summation of division values
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val

    # Function to find the smallest divisor
    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        # Initialize binary search bounds
        low = 1
        high = max(nums)

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1
        #Return the answer
        return low

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    limit = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.smallestDivisor(nums, limit)

    # Print the result
    print(f"The minimum divisor is: {ans}")
Complexity Analysis: 
Time Complexity:O(log(max)*N), where max is the maximum element in the array, N is size of the array.
We are applying binary search on our answers that are in the range of [1, max]. For every possible divisor ‘mid’, calling the sumByD() function. Inside that function, traversing the entire array, which results in O(N).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).
 '''
import math
class Solution:
    
    def sumByD(self, nums, limit):
        n = len(nums)  
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val
    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1
        return low

