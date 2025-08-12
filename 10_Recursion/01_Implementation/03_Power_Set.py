'''
Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.


Do not include the duplicates in the answer.


Examples:
Input : nums = [1, 2, 3]

Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]

Input : nums = [1, 2]

Output : [ [ ] , [1] , [2] , [1,2] ]

Input : nums = [0]

Output:
[ [ ] , [0] ]
[ [0] ]
[ [ ] ]
[]

Submit
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Real life Example
To understand the approach to solving the problem better let us compare this to a real-life example. Given a set of items (e.g., fruits), generate all possible combinations. Start with an empty basket. For each item, decide whether to exclude or include it in the basket, then move to the next item. When all items are considered, record the current combination. Revert to the previous step by removing the last included item and explore other combinations. This recursive process covers all possible subsets.

Intuition
Following up from the example above, to generate all possible subsets (power set) of a given set of items, start with an empty combination. For each item, decide whether to include it or not, and move to the next item. Once all items are considered, add the current combination to the list of subsets. Go back by removing the last item and explore other combinations. This recursive process ensures that all combinations are explored and recorded.


Approach
Base Case: When the current index equals the length of the array, it means all items have been considered. At this point, add the current subset (combination of included items) to the result list.
Make a recursive call to the function without adding the current item to the subset. This explores the possibility of subsets that do not include the current item.
Add the current item to the subset and make a recursive call to the function to explore subsets that include this item.
Backtrack: After exploring the subsets that include the current item, remove it from the subset (backtrack) and continue exploring subsets with the next items. This step ensures that all combinations are considered.
Continue the process recursively for each item, using both inclusion and exclusion to cover all possible subsets until all combinations are generated.


class Solution:
    def backtrack(self, index, n, nums, current, ans):
        # Base case: if the index reaches the length of the array,
        # add the current subset to the answer list
        if index == n:
            ans.append(current[:])  # Add a copy of the current list
            return
        
        # Recursive case: Exclude the current element and move to the next element
        self.backtrack(index + 1, n, nums, current, ans)
        
        # Include the current element in the subset and move to the next element
        current.append(nums[index])
        self.backtrack(index + 1, n, nums, current, ans)
        
        # Backtrack: remove the last added element to explore other subsets
        current.pop()

    def powerSet(self, nums):
        ans = []  # List to store all subsets
        current = []  # Temporary list to store the current subset
        self.backtrack(0, len(nums), nums, current, ans)  # Start the recursive process
        return ans  # Return the list of all subsets

# Main method to test the code
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.powerSet(nums))  # Expected output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Time Complexity
Time Complexity O(2^N): Each element in the array has two choices: either to be included in a subset or not, leading to 2^n possible subsets.

Space Complexity O(N * 2^N): We generate 2^n subsets, and each subset can have up to n elements. Additionally, the recursion stack can go up to a depth of n.


'''
class Solution:
   
    def backtrack(self, index, n, nums, current, ans):
        if index == n:
            ans.append(current[:])  
            return
        self.backtrack(index + 1, n, nums, current, ans)

        current.append(nums[index])
        self.backtrack(index + 1, n, nums, current, ans)
        current.pop()

    def powerSet(self, nums):
        ans = []  
        current = []  
        self.backtrack(0, len(nums), nums, current, ans)  
        return ans  