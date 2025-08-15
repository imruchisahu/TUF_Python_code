'''
Given collection of candidate numbers (candidates) and a integer target.Find all unique combinations in candidates where the sum is equal to the target.There can only be one usage of each number in the candidates combination and return the answer in sorted order.



e.g : The combination [1, 1, 2] and [1, 2, 1] are not unique.


Examples:
Input : candidates = [2, 1, 2, 7, 6, 1, 5] , target = 8

Output : [ [1, 1, 6] , [1, 2, 5] , [1, 7] , [2, 6] ]

Explanation : The combinations sum up to target are

1 + 1 + 6 => 8.

1 + 2 + 5 => 8.

1 + 7 => 8.

2 + 6 => 8.

Input : candidates = [2, 5, 2, 1, 2] , target = 5

Output : [ [1, 2, 2] , [5] ]

Explanation : The combinations sum up to target are

1 + 2 + 2 => 5.

5 => 5.

Input : candidates = [2, 1, 2] , target = 5

Output:
[ [1, 2, 2] ]
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

Real-Life Problem Solving
To visualize the problem, imagine having a set of coins with different denominations and a target amount to achieve. The goal is to find all unique combinations of coins that add up to the target amount without reusing the same coin denominations multiple times in the same combination. An approach to solving this can involve systematically choosing coins, reducing the target by the coin's value, and continuing until the exact target is met or exceeded. If the target is exceeded, the combination is invalid and must be discarded.

Recursion Process Intuition
The recursive process mirrors the real-life approach by first selecting a coin and subtracting its value from the target. It then recursively tries to find the remaining sum with the next coins. If a valid combination is found (target becomes zero), it is stored. If the target becomes negative or all coins are considered, the current path is abandoned, and the process backtracks to explore other combinations. This ensures all possible unique combinations are examined.

Approach
Sort the coin denominations to handle duplicates efficiently.
Use a recursive function to explore combinations, starting with an initial index and target sum.
Include the current coin in the combination and recursively call the function with the updated sum and next index.
Backtrack by removing the last added coin and skip duplicate coins to ensure unique combinations.


class Solution:
    def __init__(self):
        self.ans = []
    
    def func(self, ind, sum, nums, candidates):
        # If the sum is zero, add the current combination to the result
        if sum == 0:
            self.ans.append(nums[:])
            return
        
        # If the sum is negative or we have exhausted the candidates, return
        if sum < 0 or ind == len(candidates):
            return
        
        # Include the current candidate
        nums.append(candidates[ind])
        
        # Recursively call with updated sum and next index
        self.func(ind + 1, sum - candidates[ind], nums, candidates)
        
        # Backtrack by removing the last added candidate
        nums.pop()
        
        # Skip duplicates: if not picking the current candidate, 
        # ensure the next candidate is different
        for i in range(ind + 1, len(candidates)):
            if candidates[i] != candidates[ind]:
                self.func(i, sum, nums, candidates)
                break

    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort candidates to handle duplicates
        self.ans = []
        self.func(0, target, [], candidates)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = sol.combinationSum2(candidates, target)

    print("Combinations are: ")
    for combination in result:
        print(combination)
Complexity Analysis
Time Complexity: O(2^N * N), where n is the number of coins. This accounts for exploring all subsets of coins.

Space Complexity: O(N), due to the recursion stack depth and storage for the current combination.

'''
class Solution:
    def __init__(self):
        self.ans = []
    
    def func(self, ind, sum, nums, candidates):
        if sum == 0:
            self.ans.append(nums[:])
            return
        if sum < 0 or ind == len(candidates):
            return
        nums.append(candidates[ind])
        self.func(ind + 1, sum - candidates[ind], nums, candidates)
        nums.pop()
        for i in range(ind + 1, len(candidates)):
            if candidates[i] != candidates[ind]:
                self.func(i, sum, nums, candidates)
                break
    def combinationSum2(self, candidates, target):
        candidates.sort()  
        self.ans = []
        self.func(0, target, [], candidates)
        return self.ans
