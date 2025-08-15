'''
Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.


Examples:
Input : nums = [4, 9, 2, 5, 1] , k = 10

Output : 2

Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].

Input : nums = [4, 2, 10, 5, 1, 3] , k = 5

Output : 3

Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].

Input : nums = [1, 10, 4, 5] , k = 16

Output:
1
Constraints:
1 <= nums.length <= 20
1 <= nums[i] <= 100
1 <= k <= 2000

Real world example
Consider you are organizing a fundraising event and have a list of donation amounts from various donors. You want to determine how many different combinations of these donations can exactly match a target amount. For instance, with donations of $1, $2, $3, $4, and $5, you want to find out how many unique ways you can combine these amounts to reach a target of $5. In this case, you might find several combinations like $1 and $4 or $2 and $3 together showing that there are multiple ways to achieve the desired sum.

Intuition of the Problem
The problem involves finding all possible subsets of an array that sum up to a given target value. The approach involves recursively exploring each element, considering whether to include it in the current subset or not. By applying this decision recursively to the remaining elements, the algorithm builds up all possible subsets and counts those whose sum matches the target.

Approach
Create a recursive function that explores each element in the array. This function will consider two possibilities for each element: including it in the current subset or excluding it.
Define the base cases for the recursion:
If the target sum is 0, return 1, indicating that a valid subset has been found.
If the target sum becomes negative or if the index exceeds the array bounds, return 0, indicating that no valid subset can be formed with the current configuration.
For each element, make two recursive calls:
One call includes the current element in the subset and subtracts its value from the target sum.
The other call excludes the current element and moves to the next index.
Add the results of the two recursive calls to get the total count of subsets that sum up to the target.


class Solution:
    def func(self, ind, sum, nums):
        # Base case: if sum is 0, one valid subsequence is found
        if sum == 0:
            return 1
        # Base case: if sum is negative or index exceeds array size
        if sum < 0 or ind == len(nums):
            return 0
        # Recurse by including current number or excluding it from the sum
        return self.func(ind + 1, sum - nums[ind], nums) + self.func(ind + 1, sum, nums)

    def countSubsequenceWithTargetSum(self, nums, target):
        return self.func(0, target, nums)

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 5
    print(f"Number of subsequences with target sum {target}: {sol.countSubsequenceWithTargetSum(nums, target)}")
Complexity Analysis
Time Complexity of the recursive approach is O(2^N), where n is the number of elements in the array. This is because each element has two choices (to include or exclude), leading to an exponential number of possible subsets.

Space Complexity is O(N), where n is the maximum depth of the recursion stack. This depth corresponds to the number of elements in the array being considered at any given time.

'''
class Solution:
    def func(self, ind, sum, nums):
        if sum == 0:
            return 1
        
        if sum < 0 or ind == len(nums):
            return 0     
        return self.func(ind + 1, sum - nums[ind], nums) + self.func(ind + 1, sum, nums)

    def countSubsequenceWithTargetSum(self, nums, k):
        return self.func(0, k, nums)
    