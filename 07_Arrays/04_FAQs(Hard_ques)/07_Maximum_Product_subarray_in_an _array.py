'''Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.



A subarray is a contiguous non-empty sequence of elements within an array.


Examples:
Input: nums = [4, 5, 3, 7, 1, 2]

Output: 840

Explanation: The largest product is given by the whole array itself

Input: nums = [-5, 0, -2]

Output: 0

Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].

Input: nums = [1, -2, 3, 4, -4, -3]

Output:
144
Constraints:
1 <= nums.length <= 104
-10 <= nums[i] <= 10
-109 <= product of any prefix or suffix of nums <= 109

Similar Problems

Hint 1

Hint 2

Intuition
The naive way is to identify all possible subarrays using nested loops. For each subarray, calculate the product of its elements. Ultimately, return the maximum product found among all subarrays.

Approach
Iterate in the array using i which runs from 0 to sizeOfArray - 1, it will basically identify the starting point of the subarrays.
Now run an inner loop using j from i+1 to sizeOfArray - 1, it will identify the ending point of the subarrays. Inside this loop, iterate again from i to j and multiply elements present in the chosen range.
Update the maximum product after each iteration and finally, return it.

Complexity Analysis 
Time Complexity: O(N3) for using 3 nested loops for finding all possible subarrays and their product. Here N is the size of the array.

Space Complexity: O(1), as no additional space is used apart from the input array.
class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, nums):
        # Initialize result to minimum possible integer
        result = float('-inf')

        # Iterate through all subarrays
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = 1

                # Calculate product of subarray 
                for k in range(i, j + 1):
                    prod *= nums[k]

                # Update result with the maximum product found
                result = max(result, prod)

        # Return the maximum product found
        return result

if __name__ == "__main__":
    nums = [4, 5, 3, 7, 1, 2]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    maxProd = sol.maxProduct(nums)

    # Print the result
    print("The maximum product subarray:", maxProd)

    #TC=O(n3)
'''
class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # Swap when num is negative

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            max_prod = max(max_prod, curr_max)
        
        return max_prod
#Tc=O(n) 