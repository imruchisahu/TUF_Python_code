'''Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.


Examples:
Input: nums = [1, 0, 2, 1, 0]

Output: [0, 0, 1, 1, 2]

Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Input: nums = [0, 0, 1, 1, 1]

Output: [0, 0, 1, 1, 1]

Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos

Input: nums = [1, 1, 2, 2, 1]

Output:
[1, 1, 1, 2, 2]
Constraints:
1 <= nums.length <= 105
nums consists of 0, 1 and 2 only.

Similar Problems

Hint 1

Hint 2
Intuition
The easiest way is to sort the array using any optimal sorting algorithm. It will ensure to sort the array of 0's, 1's and 2's in ascending order.

Approach 
Sort the array using built-in function for sorting. It will manage to sort the array in optimal time.


Complexity Analysis 
Time Complexity: O(NxlogN), where N is the size of the array. As the optimal sorting take O(N * logN) time.

Space Complexity: O(1) no extra space is used to solve the problem.

from typing import List
class Solution:
    # Function to sort the array
    def sortZeroOneTwo(self, nums):
        # Sort the list using sorted() function
        nums.sort()

# Main function
if __name__ == "__main__":
    nums = [2, 0, 1, 1, 0, 2]
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.sortZeroOneTwo(nums)
    
    # Print the array elements
    print(" ".join(map(str, nums)))

'''
class Solution:
    def sortZeroOneTwo(self, nums):
        nums.sort()
        