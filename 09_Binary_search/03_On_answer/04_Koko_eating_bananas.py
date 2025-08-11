'''A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.



Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.



Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.


Examples:
Input: n = 4, nums = [7, 15, 6, 3], h = 8

Output: 5

Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

Input: n = 5, nums = [25, 12, 8, 14, 19], h = 5

Output: 25

Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.

Input: n = 4, nums = [3, 7, 6, 11], h = 8

Output:
4
Constraints:
  1 <= n <= 104
  n <= h <= 109
  1 <= nums[i] <= 109


  #Linear SEarch
  #
  Intuition: 
The straightforward solution for this problem is to use linear search algorithm to to check all possible answers from 1 to max, where max is the maximum element of the array. The minimum number for which the required time is less than or equal to h, is our required answer.

Approach: 
Working of minimumRateToEatBananas(nums, h):
First find out the maximum element in array by calling the 'findMax()'.
Then , iterate from 1 to max which signifies the number of bananas eaten per hour, and for each iteration find out the hour taken to eat those bananas by calling calculateToatalHours ().
If the calculated hour is less than or equal to given limit, return the current value of iteration(number of bananas) as an answer.
If no suitable answer is found, return max element as an answer.

Working of findMax(arr):
First initialize a variable 'maxi', which will store maximum element of the array.
Now, literate through the array and find the maximum element among them, and return it.

Working of calculateTotalHours(arr,hourly):
Start with initializing n = size of array, which gives the number of elements in the array. Initialize 'totalH' to 0, which will accumulate the total hours required. 'hourly' represents the number of items that can be processed per hour.
Compute the number of hours required to eat all bananas at the rate of 'hourly' bananas per hour and store in 'totalH'. Use ceil function to round up the division result to ensure that partial hours are counted correctly when necessary. Ater the traversal has ended, return 'totalH' as answer.

Cpp
Java
Python
Javascript
C#
Go


import math

class Solution:
    # Helper function to find the maximum element in the list 
    def findMax(self, v):
        maxi = float('-inf')
        n = len(v)
        
        # Find the maximum element
        for i in range(n):
            maxi = max(maxi, v[i])
        return maxi

    """ Helper function to calculate total hours
        required at given hourly rate """
    def calculateTotalHours(self, v, hourly):
        totalH = 0
        n = len(v)
        
        # Calculate total hours required
        for i in range(n):
            totalH += math.ceil(v[i] / hourly)
        return totalH

    # Function to find the minimum rate to eat bananas 
    def minimumRateToEatBananas(self, nums, h):
        # Find the maximum number of bananas
        maxi = self.findMax(nums)

        """ Find the minimum value of k
            that satisfies the condition """
        for i in range(1, maxi + 1):
            reqTime = self.calculateTotalHours(nums, i)
            if reqTime <= h:
                return i

        """ Dummy return statement (should 
            not be reached in valid cases) """
        return maxi

# Driver Code
if __name__ == "__main__":
    v = [7, 15, 6, 3]
    h = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.minimumRateToEatBananas(v, h)

    # Print the result
    print(f"Koko should eat at least {ans} bananas/hr.")
Complexity Analysis: 
Time Complexity:O(max * N), where max is the maximum element in the array and N is the size of the array. We are running nested loops. The outer loop runs for max times in the worst case and the inner loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

#Binary Search
Intuition: 
The idea here is to use binary search algorithm to solve this problem in a optimized way. Now, the search space will be in the range[1,max], where max is the maximum element in the array because the maximum bananas that the monkey can it per our can be the maximum element of the array. As, the search space is sorted so binary search can be applied for better time complexity.

Approach: 
Working of minimumRateToEatBananas(nums, h):
Starts by initializing low to 1 (minimum possible eating rate) and high to maximum element of the array using findMax function, which finds the maximum element in the given array. This sets up the binary search bounds where the eating rate will be searched.
Initialize a while loop that continues as long as low is less than or equal to high. Compute mid as the midpoint between low and high.
Use the function calculateTotalHours to estimate how many hours would be needed to eat all bananas in the array at the rate `mid` bananas per hour.
Compare total hour (total hours calculated at rate mid) with h (desired total hours), If total hour is less than or equal to h, it means the current eating rate mid is sufficient or possibly too high, so adjust high to mid - 1 to search for potentially smaller rates. Else, adjust low to mid + 1 to search for higher rates that might still satisfy the condition.
Once the binary search completes (low > high), low represents the minimum eating rate such that eating all bananas within h hours is feasible.

Working of findMax(arr):
First initialize a variable 'maxi', which will store maximum element of the array.
Now, literate through the array and find the maximum element among them, and return it.

Working of calculateTotalHours(arr,hourly):
Start with initializing n = size of array, which gives the number of elements in the array. Initialize 'totalH' to 0, which will accumulate the total hours required. 'hourly' represents the number of items that can be processed per hour.
Compute the number of hours required to eat all bananas at the rate of 'hourly' bananas per hour and store in 'totalH'. Use ceil function to round up the division result to ensure that partial hours are counted correctly when necessary. Ater the traversal has ended, return 'totalH' as answer.

Image 1
Image 2
Image 3

1/3


Cpp
Java
Python
Javascript
C#
Go


import math

class Solution:
    """ Helper function to find the
    maximum element in the array"""
    def findMax(self, nums):
        maxi = float('-inf')
        n = len(nums)

        # Find the maximum element
        for i in range(n):
            maxi = max(maxi, nums[i])
        return maxi

    """ Function to calculate total hours
    required at given hourly rate"""
    def calculateTotalHours(self, nums, hourly):
        totalH = 0
        n = len(nums)

        # Calculate total hours required
        for i in range(n):
            totalH += math.ceil(nums[i] / hourly)
        return totalH

    """ Function to find the 
    minimum rate to eat bananas"""
    def minimumRateToEatBananas(self, nums, h):
        # Initialize binary search bounds
        low, high = 1, self.findMax(nums)

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(nums, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    nums = [7, 15, 6, 3]
    h = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.minimumRateToEatBananas(nums, h)

    # Print the result
    print(f"Koko should eat at least {ans} bananas/hr.")
Complexity Analysis: 
Time Complexity:O(N * log(max)), where max is the maximum element in the array and N is size of the array. We are applying Binary search for the range [1, max], and for every value of ‘mid’, we are traversing the entire array inside the function named calculateTotalHours().

Space Complexity: As no additional space is used, so the Space Complexity is O(1).



  '''
import math
class Solution:
    
    def findMax(self, nums):
        maxi = float('-inf')
        n=len(nums)
        for i in range(n):
            maxi=max(maxi, nums[i])
        return maxi

    def calculateTotalHours(self, nums, hourly):
        totalH = 0
        n=len(nums)
        for i in range(n):
            totalH += math.ceil(nums[i] / hourly)
        return totalH

    def minimumRateToEatBananas(self, nums, h):
        low, high = 1, self.findMax(nums)

        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(nums, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low= mid + 1
        return low       