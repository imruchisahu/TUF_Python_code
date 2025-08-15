'''
Given an array nums of n integers. Return array of sum of all subsets of the array nums.



Output can be printed in any order.


Examples:
Input : nums = [2, 3]

Output : [0, 2, 3, 5]

Explanation :

When no elements is taken then Sum = 0.

When only 2 is taken then Sum = 2.

When only 3 is taken then Sum = 3.

When element 2 and 3 are taken then sum = 2+3 = 5.

Input : nums = [5, 2, 1]

Output : [0, 1, 2, 3, 5, 6, 7, 8]

Explanation :

When no elements is taken then Sum = 0.

When only 5 is taken then Sum = 5.

When only 2 is taken then Sum = 2.

When only 1 is taken then Sum = 1.

When element 2 and 1 are taken then sum = 2+1 = 3.

Input : nums = [1]

Output:
[0, 1]

Real-life Analogy
Consider a scenario where an individual is tasked with determining all possible expenditure amounts from a set of available items, each with a specific price. The process begins with an empty expenditure and involves evaluating each item sequentially. For each item, a decision is made whether to include its price in the current expenditure or not. This decision-making process continues until all items have been considered, resulting in a comprehensive list of all possible total expenditures.

Intuition
In the recursive approach, the problem is decomposed into simpler sub-problems by making binary decisions for each item: either include the item in the current sum or exclude it. The recursion explores both possibilities for every item until all items are processed. The base case is reached when all items have been evaluated, at which point the accumulated sum is recorded. This method ensures that every potential combination of included and excluded items is considered, thereby generating all possible subset sums.

Approach
Initialize an empty list to store the results of subset sums.
Define a recursive function that takes the current index, current sum, the input array, and the result list as parameters.
In the recursive function, check if the current index has reached the end of the array. If so, add the current sum to the result list and return.
Recursively call the function twice:
First call includes the current element in the sum, incrementing the index.
Second call excludes the current element from the sum, incrementing the index.
Start the recursion with the initial index 0 and sum 0.
Return the result list containing all possible subset sums after the recursion completes.

class Solution:
    def subsetSums(self, nums):
        def func(ind, sum, nums, ans):
            # Base case: if index reaches the end of the nums list
            if ind == len(nums):
                # Add the current sum to the ans list
                ans.append(sum)
                return
            # Recursively include the current element in the sum
            func(ind + 1, sum + nums[ind], nums, ans)
            # Recursively exclude the current element from the sum
            func(ind + 1, sum, nums, ans)
        
        ans = []
        # Start the recursion with index 0 and initial sum 0
        func(0, 0, nums, ans)
        return ans

# Example usage
solution = Solution()
nums = [1, 2, 3]
result = solution.subsetSums(nums)
print("Subset sums are:", result)
Complexity Analysis
Time Complexity: O(2N), where N is the size of the given array.
Each element has two possibilities (include or exclude), resulting in 2N combinations.

Space Complexity: O(N)
The recursion stack space will take O(N). Note that if you consider the space used to return the output that the space complexity can go up to O(2N).

'''
class Solution:
   def subsetSums(self, nums):
        def func(ind, sum, nums, ans):
            if ind == len(nums):
                ans.append(sum)
                return
            func(ind + 1, sum + nums[ind], nums, ans)
            func(ind + 1, sum, nums, ans)
        
        ans = []
        func(0, 0, nums, ans)
        return ans