'''Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in increasing order.


Examples:
Input: nums = [1, 6, 2, 10, 3], target = 7

Output: [0, 1]

Explanation: nums[0] + nums[1] = 1 + 6 = 7

Input: nums = [1, 3, 5, -7, 6, -3], target = 0

Output: [1, 5]

Explanation: nums[1] + nums[5] = 3 + (-3) = 0

Input: nums = [-6, 7, 1, -7, 6, 2], target = 3

Output:
[2, 5]
Constraints:
2 <= nums.length <= 105
-104 <= nums[i] <= 104
-105 <= target <= 105
Only one valid answer exists.

Similar Problems

Hint 1
Use a hash map (dictionary) to store the indices of elements as you iterate through the array. This allows for efficient lookups of the complement (i.e., target−current element).

Hint 2
Intuition
For each element of the given array, try to find another element such that their sum equals the target. If such two numbers exist, return their indices; otherwise, return -1.

Approach 
Iterate in array from 0 to last index of the array (lets call this variable i). Now, run another loop say(j) from i+1 to last index of the array.
If sum of arr[i] and arr[j] equals to target then return the i and j. If no such indices are found then return -1 and -1.


Complexity Analysis 
Time Complexity:O(N 2), For using two nested loops to traverse the array, where N is the length of that array.

Space Complexity: O(1), not using extra space.

from typing import List

class Solution:
    """
    Function to find two indices in the array `nums`
    such that their elements sum up to `target`.
    """
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        # Create ans list to store the indices
        ans = [0, 0]
        for i in range(n):
            for j in range(i + 1, n):
                
                """If nums[i] + nums[j] is equal to target
                put i and j in ans"""
                if nums[i] + nums[j] == target:
                    ans[0] = i
                    ans[1] = j
                    return ans
        
        # Return [-1, -1] if no such pair is found
        return [-1, -1]

if __name__ == "__main__":
    n = 5
    nums = [2, 6, 5, 8, 11]
    target = 14
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Call the twoSum method to find the indices
    ans = sol.twoSum(nums, target)
    
    # Print the result
    print(f"This is the answer: [{ans[0]}, {ans[1]}]")

'''

class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Stores number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return [-1, -1]