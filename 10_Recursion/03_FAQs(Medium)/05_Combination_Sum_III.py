'''
Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:



There is only use of numerals 1 through 9.
A single use is made of each number.


Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.


Examples:
Input : k = 3 , n = 7

Output : [ [1, 2, 4] ]

Explanation :

1 + 2 + 4 = 7

There are no other valid combinations.

Input : k = 3, n = 9

Output : [[1, 2, 6],[1, 3, 5],[2, 3, 4]]

Explanation :

1 + 2 + 6 = 9

1 + 3 + 5 = 9

2 + 3 + 4 = 9

There are no other valid combinations.

Input : k = 3, n = 8

Output:
[ [1, 2, 3, 4] ]
Constraints:
2 <= k <= 9
1 <= n <= 60'

Intuition
To build the intuition to this problem imagine being a coach who needs to form a team of exactly k players from a pool of players numbered 1 through 9. Each player has a unique skill level represented by their number. The objective is to select players such that the sum of their skill levels equals a specific target, n. Each possible combination of players is considered to find all valid teams where the total skill level precisely matches the target.

In the recursion process, each player is considered in sequence to decide whether to include them in the current team. If included, the player's skill level is subtracted from the remaining target, and the process continues with the next player. If the player's skill level cannot be included, the process backtracks to explore alternative players. This continues until all possible team combinations are evaluated.

Approach
Initialize an empty list to store the valid combinations and another list to track the current combination being formed.
Define a recursive function that accepts the remaining target sum, the next number to consider, and the current combination.
Within the recursive function, check if the remaining sum is zero and the current combination size matches k. If true, add the combination to the result list.
If the remaining sum is less than zero or the combination size exceeds k, terminate the current path. Otherwise, iterate through the possible numbers, adding each to the current combination, calling the function recursively with updated parameters, and then removing the number to explore other paths.

class Solution:
    def func(self, sum, last, nums, k, ans):
        # If the sum is zero and the number of elements is k
        if sum == 0 and len(nums) == k:
            # Add the current combination to the answer
            ans.append(list(nums))
            return
        # If the sum is less than or equal to zero or the number of elements exceeds k
        if sum <= 0 or len(nums) > k:
            return

        # Iterate from the last number to 9
        for i in range(last, 10):
            # If the current number is less than or equal to the sum
            if i <= sum:
                # Add the number to the current combination
                nums.append(i)
                # Recursive call with updated sum and next number
                self.func(sum - i, i + 1, nums, k, ans)
                # Remove the last number to backtrack
                nums.pop()
            else:
                # If the number is greater than the sum, break the loop
                break

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        # Call the recursive function with initial parameters
        self.func(n, 1, nums, k, ans)
        return ans

# Example usage
sol = Solution()
k = 3  # Number of elements in the combination
n = 7  # Target sum
result = sol.combinationSum3(k, n)

# Print the result
for combination in result:
    print(combination)
Complexity Analysis
Time Complexity The time complexity is O(2^9 * k), due to the exploration of all subsets of the set {1, 2, ..., 9}.

Space Complexity The space complexity is O(k), due to the maximum depth of the recursion stack, which is k.
'''
class Solution:
    def func(self, sum, last, nums, k, ans):
        if sum == 0 and len(nums) == k:
            ans.append(list(nums))
            return
       
        if sum <= 0 or len(nums) > k:
            return
        for i in range(last, 10):
            if i <= sum:
                nums.append(i)
                self.func(sum - i, i + 1, nums, k, ans)
                nums.pop()
            else:
                break

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        self.func(n, 1, nums, k, ans)
        return ans

