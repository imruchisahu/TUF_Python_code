'''
Provided with a goal integer target and an array of unique integer candidates, provide a list of all possible combinations of candidates in which the selected numbers add up to the target. The combinations can be returned in any order.



A candidate may be selected from the pool an infinite number of times. There are two distinct combinations if the frequency of at least one of the selected figures differs.



The test cases are created so that, for the given input, there are fewer than 150 possible combinations that add up to the target.

If there is no possible subsequences then return empty vector.


Examples:
Input : candidates = [2, 3, 5, 4] , target = 7

Output : [ [2, 2, 3] , [3, 4] , [5, 2] ]

Explanation :

2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.

5 and 2 are candidates, and 5 + 2 = 7.

3 and 4 are candidates, and 3 + 4 = 7.

There are total three combinations.

Input : candidates = [2], target = 1

Output : []

Explanation : There is no way we can choose the candidates to sum up to target.

Input : candidates = [1], target = 1

Output:
[ [1] ]
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Intuition
To understand the problem a bit better, visualize organizing a fundraising event with various items available for purchase, each contributing a different amount to the total donation. The goal is to find all combinations of these items that exactly meet a specific donation target. To achieve this, one would start by selecting an item and adding its contribution to the running total. If this total reaches the target, the current combination is recorded. If it exceeds the target, or if there are no more items to consider, the process must go back and try different combinations of remaining items. This method mirrors recursion, where every decision branches into further possibilities until the target is reached or all options are exhausted.

The core intuition behind this problem involves exploring all possible subsets of a given set of numbers to find combinations that sum up to a specific target value. Starting with the entire set, the approach involves making a series of choices: include or exclude each number in the current subset. By recursively exploring these choices, one generates all potential combinations. If a combination meets the target sum, it is recorded. If it exceeds the target or no further numbers are available, the process reverts to previous choices to explore other possible subsets. This systematic exploration of decisions and re-evaluation of choices mirrors recursion, where each step involves exploring different paths until all possibilities are exhausted.

Approach
Define a recursive function that explores all possible combinations of elements. The function should track the current sum and the elements included in the combination.
Check base cases within the function, if the current sum matches the target, add the current combination to the result. If the sum exceeds the target or no more elements are available, stop further exploration.
For each recursive call, decide whether to include the current element in the combination or exclude it. Update the sum and combination list accordingly, and then proceed with further recursive calls.
After exploring with the current element included, backtrack by removing the last added element to explore other potential combinations.


class Solution:
    # Recursive function to find all subsequences with the given target sum
    def func(self, v, i, sum, v2, ans):
        # Base case: if the sum is zero, add the current subsequence to the result
        if sum == 0:
            ans.append(v2[:])
            return
        
        # Base case: if the sum becomes negative or no elements are left
        if sum < 0 or i < 0:
            return
        
        # Exclude the current element and move to the next
        self.func(v, i - 1, sum, v2, ans)
        
        # Include the current element in the subsequence
        v2.append(v[i])
        
        # Recursively call the function with the included element
        self.func(v, i, sum - v[i], v2, ans)
        
        # Backtrack by removing the last added element
        v2.pop()

    # Main function to find all unique combinations of candidates that sum to the target
    def combinationSum(self, candidates, target):
        ans = []
        
        # Create a copy of the candidates list for easier manipulation
        v = candidates[:]
        
        # Start the recursive process
        self.func(v, len(v) - 1, target, [], ans)
        
        return ans

# Main block to test the solution
if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = sol.combinationSum(candidates, target)
    print(result)
Complexity Analysis
Time Complexity: O(K*2N), where N is the number of elements, due to the exponential number of possible combinations explored in the worst case. For each subset, it may take up to K operations to process, where K is the maximum length of any subset in the result

Space Complexity: O(K*N), where N is the maximum depth of recursion, which corresponds to the length of the combination path stored in memory.

'''
class Solution:
    def func(self, v, i, sum, v2, ans):
        if sum == 0:
            ans.append(v2[:])
            return
        if sum < 0 or i < 0:
            return
        self.func(v, i - 1, sum, v2, ans)
        
        v2.append(v[i])
        self.func(v, i, sum - v[i], v2, ans)
        v2.pop()
    def combinationSum(self, candidates, target):
        ans = []
        v = candidates[:]
        self.func(v, len(v) - 1, target, [], ans) 
        return ans