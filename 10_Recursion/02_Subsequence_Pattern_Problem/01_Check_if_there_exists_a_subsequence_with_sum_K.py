'''
Given an array nums and an integer k. R﻿eturn true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.


Examples:
Input : nums = [1, 2, 3, 4, 5] , k = 8

Output : Yes

Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Input : nums = [4, 3, 9, 2] , k = 10

Output : No

Explanation : No subsequence can sum up to 10.

Input : nums = [1, 10, 4, 5] , k = 16

Output:
Yes
Constraints:
1 <= nums.length <= 20
1 <= nums[i] <= 100
1 <= k <= 2000

Real-Life Analogy
Imagine deciding which coins to use to reach an exact amount of money. Each coin represents a choice: include it in the total or leave it out. By recursively considering each coin and updating the target amount, explore every possible combination of coins. The goal is to determine if any combination of coins can exactly meet the target amount. This method effectively tests all possible ways to reach the target by including or excluding each coin, similar to the problem of finding a subsequence with a specific sum.

Intuition
The problem involves determining whether a subsequence of a given array can sum up to a specified target. By recursively exploring all possible ways to include or exclude each element of the array, the goal is to find out if any combination of these elements can achieve the target sum. The challenge is to exhaustively check all potential subsequences and see if their sum matches the target value.


Approach
Start with the first item and explore two options: including the item in the current expenditure or excluding it.
Recursively repeat the process for the next item with the updated target amount, adjusting the sum accordingly.
Base cases include: achieving the target amount (success), running out of items (failure if target not met), or if the target becomes negative (failure).
Continue this process until all combinations are explored, and determine if any of them meet the exact target amount.


class Solution:
    # This method recursively checks for the subsequence with the given sum
    def solve(self, i, n, arr, k):
        # Base case: if the sum k is 0, a subsequence is found
        if k == 0:
            return True
        # Base case: if k is negative, no valid subsequence can be found
        if k < 0:
            return False
        # Base case: if all elements are processed, check if k is 0
        if i == n:
            return k == 0
        
        # Recursive call: include the current element in the subsequence
        # or exclude the current element from the subsequence
        return self.solve(i + 1, n, arr, k - arr[i]) or self.solve(i + 1, n, arr, k)

    # This method initiates the recursive process
    def checkSubsequenceSum(self, nums, target):
        n = len(nums) # Get the length of the input array
        return self.solve(0, n, nums, target) # Start the recursive process

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    target = 5
    print(sol.checkSubsequenceSum(nums, target)) # Expected output: True
Complexity Analysis
Time Complexity O(2n) - Each item has two choices (include or exclude), leading to an exponential number of combinations.

Space Complexity: O(n) - The maximum depth of the recursive call stack is equal to the number of items.
'''
class Solution:
    def solve(self, i, n, arr, k):
        if k == 0:
            return True 
        if k < 0:
            return False 
        if i == n:
            return k == 0        
        return self.solve(i + 1, n, arr, k - arr[i]) or self.solve(i + 1, n, arr, k)
    def checkSubsequenceSum(self, nums, target):
        n = len(nums) 
        return self.solve(0, n, nums, target) 